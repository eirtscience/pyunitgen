import ast
import re
from .nodetype import NodeType, AssertUnitTestCase
from .templates import Templates
from faker import Faker


class Node:
    pass


class NodeClass:
    pass


class NodeDecoration:
    pass


class NodeFunction:
    def __init__(self, node, caller_class=None):
        self.node = node
        self.name = node.name
        self.caller = caller_class

    def getDecorationList(self):
        if self.node.decorator_list:
            for deco in self.node.decorator_list:
                yield deco
        return None

    def getDecoration(self):
        return next(self.getDecorationList())

    def getName(self):
        return self.node.name

    def getComment(self):
        return ast.get_docstring(self.node, clean=True)

    def getReturnType(self):
        comment = self.getComment()
        # print(dir(self.node))
        if comment:
            res = re.findall(
                r"(\@apiReturn)[ ]+(?P<type>[a-zA-Z0-9\{\} ]+)(?P<arg>[a-zA-Z0-9\[\]\{\}\.'\":, ]+)", comment)
            print(res)
            if res:

                _, k, v = res[0]

                value = v.strip("[ ]",)
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

        return None, None

    def getParameter(self):
        comment = self.getComment()
        list_param = None

        # m = re.match(r"(?P<first_name>\w+)[ ]+(?P<last_name>\w+)",
        #              "Malcolm    Reynolds")

        # print(m.groupdict())

        if comment:
            res = re.findall(
                r"(\@apiParam)[ ]+(?P<type>[a-zA-Z0-9\{\} ]+)[ ]+(?P<arg>[a-zA-Z0-9\[\]]+)", comment)
            print(res)
            if res:
                list_param = {v.strip("[ ]"): k.strip("{ }")
                              for _, k, v in res}
        return list_param

    def getAssertTest(self):

        r_type, r_value = self.getReturnType()
        list_param = self.getParameter()
        print(list_param)
        func_body = None
        faker = Faker()

        if self.caller:
            print(self.caller.name)

        arg_body = []

        if self.node.decorator_list:
            if self.getDecoration().id in ["classmethod", "staticmethod"]:
                if list_param:

                    for arg_name, arg_type in list_param.items():
                        if arg_type.lower() == "string":
                            arg_body.append("{}='{}'".format(
                                arg_name, faker.name()))
                        elif arg_type.lower() == "number":
                            arg_body.append("{}='{}'".format(
                                arg_name, faker.random_number()))
                    func_body = '''
      {}={}.{}({})'''.format(self.caller.name.lower(), self.caller.name, self.name, ",".join(arg_body))

                else:
                    func_body = '''
      {}={}.{}()'''.format(self.caller.name.lower(), self.caller.name, self.name)
        else:
            if list_param:

                for arg_name, arg_type in list_param.items():
                    if arg_type.lower() == "string":
                        arg_body.append("{}='{}'".format(
                            arg_name, faker.name()))
                    elif arg_type.lower() == "number":
                        arg_body.append("{}='{}'".format(
                            arg_name, faker.random_number()))
                func_body = '''
      {} = {}().{}({}) '''.format(self.caller.name.lower(), self.caller.name, self.name, ",".join(arg_body))
            else:
                func_body = '''
      {} = {}().{}() '''.format(self.caller.name.lower(), self.caller.name, self.name)

        print(isinstance(r_type, bool))

        if isinstance(r_type, bool):
            if r_value == "True":
                return Templates.methodTest.format(
                    self.name, func_body, AssertUnitTestCase.assert_true.format(self.caller.name.lower(), r_value))
            return Templates.methodTest.format(
                self.name, func_body, AssertUnitTestCase.assert_false.format(self.caller.name.lower(), r_value))

        if isinstance(r_type, int):
            print(func_body)
            return Templates.methodTest.format(
                self.name, func_body, AssertUnitTestCase.assert_equal.format(self.caller.name.lower(), r_value))

        if r_type is None:
            return Templates.methodTest.format(
                self.name, func_body, AssertUnitTestCase.assert_is_none.format(self.caller.name.lower()))
