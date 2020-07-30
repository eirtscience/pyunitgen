
import unittest

		
class NetworkFileHandlerTest(unittest.TestCase):
		"""
		Tests for methods in the <_ast.ClassDef object at 0x7f2c157b4cc0> class.
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
	
		def test_networkpath(self):
				
      networkfilehandler=NetworkFileHandler.networkpath()
			
      self.assertIsNone(networkfilehandler) 

		def test_create_script_file(self):
				
      networkfilehandler=NetworkFileHandler.create_script_file()
			
      self.assertIsNone(networkfilehandler) 

		def test_create_file(self):
				
      networkfilehandler=NetworkFileHandler.create_file()
			
      self.assertIsNone(networkfilehandler) 

		def test_create_base_file(self):
				
      networkfilehandler=NetworkFileHandler.create_base_file()
			
      self.assertIsNone(networkfilehandler) 

		def test_create_explorer_file(self):
				
      networkfilehandler=NetworkFileHandler.create_explorer_file()
			
      self.assertIsNone(networkfilehandler) 

		def test_create_fabric_file(self):
				
      networkfilehandler=NetworkFileHandler.create_fabric_file()
			
      self.assertIsNone(networkfilehandler) 

		def test_create_directory(self):
				
      networkfilehandler=NetworkFileHandler.create_directory()
			
      self.assertIsNone(networkfilehandler) 
		