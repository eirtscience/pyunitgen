
import unittest

		
class PyUnitFileTest(unittest.TestCase):
		"""
		Tests for methods in the PyUnitFile class.
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
	
		def test_getModule(self):
				
      pyunitfile = PyUnitFile().getModule() 
			
      self.assertIsNone(pyunitfile) 

		def test_getSourceTree(self):
				
      pyunitfile = PyUnitFile().getSourceTree() 
			
      self.assertIsNone(pyunitfile) 
		