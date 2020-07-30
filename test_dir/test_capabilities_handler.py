
import unittest

		
class CapabilitiesHandlerTest(unittest.TestCase):
		"""
		Tests for methods in the <_ast.ClassDef object at 0x7f2c1578c080> class.
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
				
      capabilitieshandler = CapabilitiesHandler().getEnableNodeOUsAsStr() 
			
      self.assertIsNone(capabilitieshandler) 

		def test_getPolicies(self):
				
      capabilitieshandler = CapabilitiesHandler().getPolicies() 
			
      self.assertIsNone(capabilitieshandler) 

		def test_getAdminRolePolicies(self):
				
      capabilitieshandler = CapabilitiesHandler().getAdminRolePolicies() 
			
      self.assertIsNone(capabilitieshandler) 
		