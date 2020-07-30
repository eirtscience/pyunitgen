
import unittest

		
class CommonTest(unittest.TestCase):
		"""
		Tests for methods in the <_ast.ClassDef object at 0x7f2c15688be0> class.
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
	
		def test_getEnableNodeOUsAsStr(self):
				
      common = Common().getEnableNodeOUsAsStr() 
			
      self.assertIsNone(common) 

		def test_getPolicies(self):
				
      common = Common().getPolicies() 
			
      self.assertIsNone(common) 

		def test_getAdminRolePolicies(self):
				
      common = Common().getAdminRolePolicies() 
			
      self.assertIsNone(common) 
		