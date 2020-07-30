
import unittest

		
class GeneratorTest(unittest.TestCase):
		"""
		Tests for methods in the Generator class.
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
	
		def test_generateUnitTest(self):
				
      generator=Generator.generateUnitTest()
			
      self.assertIsNone(generator) 
		