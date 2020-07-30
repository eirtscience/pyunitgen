
import unittest

		
class ChannelTest(unittest.TestCase):
		"""
		Tests for methods in the <_ast.ClassDef object at 0x7f2c157b48d0> class.
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
				
      channel = Channel().list_version() 
			
      self.assertIsNone(channel) 

		def test_channel_dump(self):
				
      channel = Channel().channel_dump() 
			
      self.assertIsNone(channel) 
		