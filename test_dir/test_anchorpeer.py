
import unittest

		
class AnchorPeerTest(unittest.TestCase):
		"""
		Tests for methods in the <_ast.ClassDef object at 0x7f2c157ca390> class.
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
	
		def test_dump(self):
				
      anchorpeer = AnchorPeer().dump() 
			
      self.assertIsNone(anchorpeer) 

		def test_test_unit(self):
				
      anchorpeer = AnchorPeer().test_unit() 
			
      self.assertEqual(anchorpeer, {"name":4}) 

		def test_test_unit_1(self):
				
      anchorpeer = AnchorPeer().test_unit_1(test1='Chelsea Young',test2='Courtney Holland') 
			
      self.assertTrue(anchorpeer,True)

		def test_test_unit_2(self):
				
      anchorpeer = AnchorPeer().test_unit_2() 
			
      self.assertEqual(anchorpeer, ['1', '2', '3', '4']) 

		def test_test_unit_3(self):
				
      anchorpeer = AnchorPeer().test_unit_3() 
			
      self.assertIsNone(anchorpeer) 

		def test_test_unit_4(self):
				
      anchorpeer = AnchorPeer().test_unit_4() 
			
      self.assertIsNone(anchorpeer) 
		