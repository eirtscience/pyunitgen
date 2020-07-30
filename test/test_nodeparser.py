from pyunitgen.application.objects.nodeparser import AstNode,Node,NodeClass,NodeDecoration,NodeFunction
import unittest

		
class NodeTest(unittest.TestCase):
		"""
		Tests for methods in the Node class.
		"""

		@classmethod
		def setUpClass(cls):
			pass #TODO

		@classmethod
		def tearDownClass(cls):
			pass #TODO

		def setUp(self):
			pass #TODO

		def tearDown(self):
			pass #TODO
	
		def test_getParentName(self):
			
      node = Node().getParentName() 
			
      self.assertIsNone(node) 

		def test_get_imports(self):
			
      node = Node().get_imports() 
			
      self.assertIsNone(node) 

		def test_init_children(self):
			
      node = Node().init_children() 
			
      self.assertIsNone(node) 

		def test_getChildren(self):
			
      node = Node().getChildren() 
			
      self.assertIsNone(node) 

		def test_getName(self):
			
      node = Node().getName() 
			
      self.assertIsNone(node) 

		def test_getType(self):
			
      node = Node().getType() 
			
      self.assertIsNone(node) 

		def test_hasChildren(self):
			
      node = Node().hasChildren() 
			
      self.assertIsNone(node) 

		def test_isClass(self):
			
      node = Node().isClass() 
			
      self.assertIsNone(node) 

		def test_isFunction(self):
			
      node = Node().isFunction() 
			
      self.assertIsNone(node) 

		def test_getUnitTest(self):
			
      node = Node().getUnitTest() 
			
      self.assertIsNone(node) 


class NodeClassTest(unittest.TestCase):
		"""
		Tests for methods in the NodeClass class.
		"""

		@classmethod
		def setUpClass(cls):
			pass #TODO

		@classmethod
		def tearDownClass(cls):
			pass #TODO

		def setUp(self):
			pass #TODO

		def tearDown(self):
			pass #TODO
	
		def test_isClass(self):
			
      nodeclass = NodeClass().isClass() 
			
      self.assertIsNone(nodeclass) 

		def test_getUnitTest(self):
			
      nodeclass = NodeClass().getUnitTest() 
			
      self.assertIsNone(nodeclass) 


class NodeFunctionTest(unittest.TestCase):
		"""
		Tests for methods in the NodeFunction class.
		"""

		@classmethod
		def setUpClass(cls):
			pass #TODO

		@classmethod
		def tearDownClass(cls):
			pass #TODO

		def setUp(self):
			pass #TODO

		def tearDown(self):
			pass #TODO
	
		def test_isFunction(self):
			
      nodefunction = NodeFunction().isFunction() 
			
      self.assertIsNone(nodefunction) 

		def test_getDecorationList(self):
			
      nodefunction = NodeFunction().getDecorationList() 
			
      self.assertIsNone(nodefunction) 

		def test_getFuncUnitTest(self):
			
      nodefunction = NodeFunction().getFuncUnitTest() 
			
      self.assertIsNone(nodefunction) 

		def test_getUnitTest(self):
			
      nodefunction = NodeFunction().getUnitTest() 
			
      self.assertIsNone(nodefunction) 

		def test_getDecoration(self):
			
      nodefunction = NodeFunction().getDecoration() 
			
      self.assertIsNone(nodefunction) 

		def test_getComment(self):
			
      nodefunction = NodeFunction().getComment() 
			
      self.assertIsNone(nodefunction) 

		def test_getFunctionType(self):
			
      nodefunction = NodeFunction().getFunctionType() 
			
      self.assertIsNone(nodefunction) 

		def test_getReturnType(self):
			
      nodefunction = NodeFunction().getReturnType() 
			
      self.assertIsNone(nodefunction) 

		def test_getParameter(self):
			
      nodefunction = NodeFunction().getParameter() 
			
      self.assertIsNone(nodefunction) 

		def test_getAssertTest(self):
			
      nodefunction = NodeFunction().getAssertTest() 
			
      self.assertIsNone(nodefunction) 

		def test_getFuncAssertTest(self):
			
      nodefunction = NodeFunction().getFuncAssertTest() 
			
      self.assertIsNone(nodefunction) 
		