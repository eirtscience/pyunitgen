
import unittest

		
class ConsoleTest(unittest.TestCase):
		"""
		Tests for methods in the <_ast.ClassDef object at 0x7f2c1577f588> class.
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
	
		def test_get_string(self):
				
      console=Console.get_string()
			
      self.assertIsNone(console) 

		def test_get_int(self):
				
      console=Console.get_int()
			
      self.assertIsNone(console) 

		def test_get_bool(self):
				
      console=Console.get_bool()
			
      self.assertIsNone(console) 

		def test_get_file(self):
				
      console=Console.get_file()
			
      self.assertIsNone(console) 

		def test_choice(self):
				
      console=Console.choice()
			
      self.assertIsNone(console) 

		def test_get_list_input(self):
				
      console=Console.get_list_input()
			
      self.assertIsNone(console) 

		def test_run(self):
				
      console=Console.run()
			
      self.assertIsNone(console) 

		def test_error(self):
				
      console=Console.error()
			
      self.assertIsNone(console) 
		