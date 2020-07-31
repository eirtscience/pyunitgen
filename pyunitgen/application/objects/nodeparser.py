import ast
from collections import namedtuple
import re
from .nodetype import NodeType, AssertUnitTestCase
from .templates import Templates
from faker import Faker
from .pyunitreport import PyUnitReport, PyUnitReportValidation
from .pyunittype import PyUnitObject
from random import choice

Import = namedtuple("Import", ["module", "name", "alias"])

# TODO: When generating the unittest file make sure to compare existing generate unittest
#      file so you don't overwrite the existing one. When comparing and there are some
#      missing function or method, just create those missing one.


class AstNode:
    def __init__(self, node):
        self.name = node.name

    def __new__(self, node):
        return node


class Node:
    def __init__(self, node, parent=None, includeInternal=None):
        self.node = AstNode(node)
        self.list_children = []
        self.parent = parent
        self.includeInternal = includeInternal
        self.name = None
        self.report = PyUnitReportValidation()
        self.module_name = None
        self.list_import = []
        self.node_module = []
        self.has_class = False
        self.init_children()

    def getParentName(self):
        if isinstance(self.parent, ast.ClassDef):
            if hasattr(self.parent, "name"):
                return self.parent.name
        else:
            if self.parent == None or self.parent.getName() == None:
                return self.parent.module_name
            return self.parent.getName()

    def get_imports(self, node):

        if isinstance(node, ast.Import):
            module = []
        elif isinstance(node, ast.ImportFrom):
            module = node.module.split('.')
        else:
            return

        for n in node.names:
            self.list_import.append(
                Import(module, n.name.split('.'), n.asname))

    def init_children(self):

        for child in self.node.body:
            nodeType = type(child)
            node = None
            # print(nodeType)
            self.get_imports(child)
            if nodeType is ast.ClassDef:
                if not child.name.startswith('_') or self.includeInternal:
                    node = NodeClass(child, parent=self,
                                     includeInternal=self.includeInternal)
                    self.node_module.append(node.getName())
                    self.has_class = True
            elif nodeType is ast.FunctionDef:
                if not child.name.startswith('_') or self.includeInternal:
                    node = NodeFunction(
                        child, parent=self, includeInternal=self.includeInternal)
                    if self.parent == None:
                        # print(child.name)
                        self.node_module.append(node.getName())

            self.get_imports(child)
            if node:
                node.list_import = self.list_import
                self.list_children.append(node)

    def getChildren(self):
        return self.list_children

    def getName(self):
        if hasattr(self.node, "name"):
            return self.node.name

    def getType(self):
        return type(self)

    def hasChildren(self):
        return len(self.list_children)

    def isClass(self):
        return False

    def isFunction(self):
        return False

    def getUnitTest(self, module=None):
        if self.hasChildren():
            classTestComment = 'Tests for functions in the "%s" file.' % module
            list_method = []
            for method in self.getChildren():
                if method.isFunction():
                    if method.getName()[0] != '_':
                        list_method.append(method.getFuncAssertTest())

            methodTests = '\n'.join(list_method)

            return Templates.classTest % (
                module, classTestComment,
                methodTests,
            )


class NodeClass(Node):

    def isClass(self):
        return (type(self) == NodeClass)

    def getUnitTest(self, module=None):
        if self.hasChildren():
            classTestComment = 'Tests for methods in the %s class.' % self.getName()
            list_method = []
            for method in self.getChildren():
                if method.isFunction():
                    if method.getName()[0] != '_':
                        list_method.append(
                            method.getAssertTest())
                elif method.isClass():
                    class_children = method.getUnitTest(module)
                    if class_children:
                        list_method.extend(class_children)

            methodTests = '\n'.join(list_method)

            return Templates.classTest % (
                self.getName(), classTestComment,
                methodTests,
            )


class NodeDecoration:
    pass


class NodeFunction(NodeClass):
    def __init__(self, node, parent=None, includeInternal=None):
        super(NodeFunction, self).__init__(
            node=node, parent=parent, includeInternal=includeInternal)
        self.list_parameter = {}
        self.return_type = None
        self.return_value = None

    def isFunction(self):
        return (type(self) == NodeFunction)

    def getDecorationList(self):
        if self.node.decorator_list:
            for deco in self.node.decorator_list:
                yield deco
        return None

    def getFuncUnitTest(self, module):
        functionTests = Templates.functionTest.format(
            self.getName(), NodeType.re_none % (self.getName()))
        return functionTests

    def getUnitTest(self, module=None):

        moduleTestComment = 'Tests for functions in the %s module.' % module
        functionTests = Templates.functionTest.format(
            self.getName(), NodeType.re_none % (self.getName()))
        functionTests += "\n"

        # print(self.parent)

        return Templates.classTest % (
            module, moduleTestComment,
            functionTests)

    def getDecoration(self):
        return next(self.getDecorationList())

    def getComment(self):
        return ast.get_docstring(self.node, clean=True)

    def getFunctionType(self, res):
        _, k, v = res[0]
        value = v.strip("[ ]")
        key = k.strip("{ }")
        if "," in value:
            value = value.split(",")

        if key.lower() == "boolean":
            if value:
                return True, value
            return True, None

        if key.lower() == "number":
            if value:
                return 1, value
            return 1, None

        if key.lower() == "string":
            if value:
                return "", "'{}'".format(value)
            return "", None

        if key.lower() == "list":
            if value:
                return "", value
            return [], None

        if key.lower() == "dict":
            if value:
                return "", value
            return {}, None

        if key.lower() == "object":
            if value:
                return object, value
            return None, None

        if "apiparam" in key.lower():
            self.return_type = PyUnitObject(key)
            if value:
                return self.return_type, value
            return None, None

    def getReturnType(self):
        comment = self.getComment()
        # print(dir(self.node))
        if comment:
            res = re.findall(
                r"(\@apiReturn)[ ]+(?P<type>[a-zA-Z0-9\{\}\._ ]+)(?P<arg>[a-zA-Z0-9\[\]\{\}\.'\":, _\(\)]+)", comment)
            if res:

                return self.getFunctionType(res)

        return None, None

    def getParameter(self):
        comment = self.getComment()
        list_param = None

        if comment:
            res = re.findall(
                r"(\@apiParam)[ ]+(?P<type>[a-zA-Z0-9=_\{\} ]+)[ ]+(?P<arg>[a-zA-Z0-9\[\]:=_\"]+)", comment)
            # print(res)
            if res:
                list_param = {v.strip("[ ]"): k.strip("{ }")
                              for _, k, v in res}
        return list_param

    def _getFakeDataBy(self, type_of_data=None, default="name"):
        if default is None:
            default = "name"
        faker = Faker()
        if type_of_data == None:
            type_of_data = default

        try:
            return getattr(faker, type_of_data.lower())()
        except AttributeError:
            return default

    def generateParameterData(self, list_param):
        arg_body = []
        faker = Faker()
        # print(list_param)
        boolean_value = choice([True, False])
        for arg_name, arg_type in list_param.items():
            type_of_data = None
            default = None
            value = None
            if "=" in arg_type:
                arg_type, type_of_data = arg_type.split("=")
            if "=" in arg_name:
                arg_name, default = arg_name.split("=")
            if arg_type.lower() == "string":

                if default:
                    default = default.strip("'\"")
                value = self._getFakeDataBy(type_of_data, default=default)
                arg_body.append("{}='{}'".format(
                    arg_name, value))
                self.list_parameter[arg_name] = {
                    "value": value, "type": arg_type.lower()}
            elif arg_type.lower() == "number":
                if default is None:
                    default = "random_number"
                value = self._getFakeDataBy(type_of_data, default=default)
                arg_body.append("{}={}".format(
                    arg_name, value))
                self.list_parameter[arg_name] = {
                    "value": value, "type": arg_type.lower()}
            elif arg_type.lower() == "boolean":
                arg_body.append("{}={}".format(
                    arg_name, boolean_value))
                self.list_parameter[arg_name] = boolean_value
                self.list_parameter[arg_name] = {
                    "value": boolean_value, "type": arg_type.lower()}
            else:
                pass
                # value = getattr(faker, arg_type.lower())()
                # arg_body.append("{}={}".format(
                #     arg_name, value))

        return arg_body

    def method_initialization_name(self):
        return "{}_{}".format(self.getParentName().lower(), self.getName())

    def getAssertTest(self):

        r_type, r_value = self.getReturnType()
        list_param = self.getParameter()
        # print(list_param)
        func_body = None
        faker = Faker()

        # if self.parent:
        #     print(self.getParentName())

        arg_body = []
        # TODO: Change all the return name of the class method for example {}={}.{}({})
        if self.node.decorator_list:
            if self.getDecoration().id in ["classmethod", "staticmethod"]:
                if list_param:
                    arg_body = self.generateParameterData(list_param)
                    func_body = '''
      {}={}.{}({})'''.format(self.getParentName().lower(), self.getParentName(), self.getName(), ",".join(arg_body))

                else:
                    func_body = '''
      {}={}.{}()'''.format(self.getParentName().lower(), self.getParentName(), self.getName())
        else:
            if list_param:

                arg_body = self.generateParameterData(list_param)
                func_body = '''
      {0} = {1}()
      {4}={0}.{2}({3}) '''.format(self.getParentName().lower(), self.getParentName(), self.getName(), ",".join(arg_body), self.method_initialization_name())
            else:
                func_body = '''
      {0} = {1}()
      {3}={0}.{2}() '''.format(self.getParentName().lower(), self.getParentName(), self.getName(), self.method_initialization_name())

        # print(type(r_type))
        # print(self.list_parameter)

        if isinstance(r_type, bool):
            if r_value == "True":
                return Templates.methodTest.format(
                    self.getName(), func_body, AssertUnitTestCase.assert_true.format(self.method_initialization_name(), r_value))
            return Templates.methodTest.format(
                self.getName(), func_body, AssertUnitTestCase.assert_false.format(self.method_initialization_name(), r_value))

        if isinstance(r_type, int) or isinstance(r_type, str) or isinstance(r_type, list) or isinstance(r_type, dict):
            # print(func_body)
            return Templates.methodTest.format(
                self.getName(), func_body, AssertUnitTestCase.assert_equal.format(self.method_initialization_name(), r_value))

        if isinstance(r_type, PyUnitObject):
            parameter = self.list_parameter.get(
                r_type.get_return_object_name())
            value = parameter.get("value")
            if parameter.get("type") == "string":
                value = "'{}'".format(value)

            return Templates.methodTest.format(
                self.getName(), func_body, AssertUnitTestCase.assert_equal.format(value, r_value))

        if r_type is None:
            return Templates.methodTest.format(
                self.getName(), func_body, AssertUnitTestCase.assert_is_none.format(self.method_initialization_name()))

    def getFuncAssertTest(self):

        # print(self.getReturnType())
        r_type, r_value = self.getReturnType()
        list_param = self.getParameter()
        # print(list_param)
        func_body = None
        faker = Faker()

        # if self.parent:
        #     print(self.getParentName())

        arg_body = []

        if self.node.decorator_list:
            if self.getDecoration().id in ["classmethod", "staticmethod"]:
                if list_param:
                    arg_body = self.generateParameterData(list_param)
                    func_body = '''
      {}={}({})'''.format(self.getParentName().lower(), self.getName(), ",".join(arg_body))

                else:
                    func_body = '''
      {}={}()'''.format(self.getParentName().lower(), self.getName())
        else:
            if list_param:
                arg_body = self.generateParameterData(list_param)
                func_body = '''
      {} = {}({}) '''.format(self.getParentName().lower(), self.getName(), ",".join(arg_body))
            else:
                func_body = '''
      {} = {}() '''.format(self.getParentName().lower(), self.getName())

        # print(isinstance(r_type, bool))

        if isinstance(r_type, bool):
            if r_value == "True":
                return Templates.methodTest.format(
                    self.getName(), func_body, AssertUnitTestCase.assert_true.format(self.getParentName().lower(), r_value))
            return Templates.methodTest.format(
                self.getName(), func_body, AssertUnitTestCase.assert_false.format(self.getParentName().lower(), r_value))

        if isinstance(r_type, int) or isinstance(r_type, str) or isinstance(r_type, list) or isinstance(r_type, dict):
            # print(func_body)
            return Templates.methodTest.format(
                self.getName(), func_body, AssertUnitTestCase.assert_equal.format(self.getParentName().lower(), r_value))

        if isinstance(r_type, PyUnitObject):
            parameter = self.list_parameter.get(
                r_type.get_return_object_name())
            value = parameter.get("value")
            if parameter.get("type") == "string":
                value = "'{}'".format(value)

            return Templates.methodTest.format(
                self.getName(), func_body, AssertUnitTestCase.assert_equal.format(value, r_value))

        if r_type is None:
            return Templates.methodTest.format(
                self.getName(), func_body, AssertUnitTestCase.assert_is_none.format(self.getParentName().lower()))
