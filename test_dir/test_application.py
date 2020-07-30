
import unittest

		
class ApplicationTest(unittest.TestCase):
		"""
		Tests for methods in the <_ast.ClassDef object at 0x7f2c15705f98> class.
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
	
		def test_list_version(self):
				
      application = Application().list_version() 
			
      self.assertIsNone(application) 

		def test_dump_application(self):
				
      application = Application().dump_application() 
			
      self.assertIsNone(application) 
		