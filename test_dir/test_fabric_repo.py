
import unittest

		
class FabricRepoTest(unittest.TestCase):
		"""
		Tests for methods in the <_ast.ClassDef object at 0x7f2c157cac18> class.
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
	
		def test_create_installer_script(self):
				
      fabricrepo = FabricRepo().create_installer_script() 
			
      self.assertIsNone(fabricrepo) 

		def test_getRepoByVersion(self):
				
      fabricrepo = FabricRepo().getRepoByVersion() 
			
      self.assertIsNone(fabricrepo) 
		