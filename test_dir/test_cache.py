
import unittest

		
class CacheServerTest(unittest.TestCase):
		"""
		Tests for methods in the <_ast.ClassDef object at 0x7f2c157ca9e8> class.
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
	
		def test_set_session(self):
				
      cacheserver = CacheServer().set_session() 
			
      self.assertIsNone(cacheserver) 

		def test_get_session(self):
				
      cacheserver = CacheServer().get_session() 
			
      self.assertIsNone(cacheserver) 

		def test_is_session_exist(self):
				
      cacheserver = CacheServer().is_session_exist() 
			
      self.assertIsNone(cacheserver) 

		def test_append_session(self):
				
      cacheserver = CacheServer().append_session() 
			
      self.assertIsNone(cacheserver) 
		