from pyunitgen.application.unittestgenerator import checksum,filesum,watch
import unittest

		
class unittestgeneratorTest(unittest.TestCase):
		"""
		Tests for methods in the None class.
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
	
		def test_checksum(self):
			
      unittestgenerator = checksum() 
			
      self.assertIsNone(unittestgenerator) 

		def test_filesum(self):
			
      unittestgenerator = filesum() 
			
      self.assertIsNone(unittestgenerator) 

		def test_watch(self):
			
      unittestgenerator = watch() 
			
      self.assertIsNone(unittestgenerator) 
		