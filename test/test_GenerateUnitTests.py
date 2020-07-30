from pyunitgen.application.objects.GenerateUnitTests import generate_unittest,generate_unittest_for,main
import unittest

		
class GenerateUnitTestsTest(unittest.TestCase):
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
	
		def test_generate_unittest(self):
			
      generateunittests = generate_unittest() 
			
      self.assertIsNone(generateunittests) 

		def test_generate_unittest_for(self):
			
      generateunittests = generate_unittest_for() 
			
      self.assertIsNone(generateunittests) 

		def test_main(self):
			
      generateunittests = main() 
			
      self.assertIsNone(generateunittests) 
		