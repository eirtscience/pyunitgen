from pyunitgen.cli import display,display_2,main
import unittest

		
class cliTest(unittest.TestCase):
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
	
		def test_display(self):
			
      cli = display() 
			
      self.assertIsNone(cli) 

		def test_display_2(self):
			
      cli = display_2() 
			
      self.assertIsNone(cli) 

		def test_main(self):
			
      cli = main() 
			
      self.assertIsNone(cli) 
		