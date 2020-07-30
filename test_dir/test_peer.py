
import unittest

		
class PeerTest(unittest.TestCase):
		"""
		Tests for methods in the <_ast.ClassDef object at 0x7f2c156e1a90> class.
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
	
		def test_getHostname(self):
				
      peer = Peer().getHostname() 
			
      self.assertIsNone(peer) 

		def test_getChainCodeInternPort(self):
				
      peer = Peer().getChainCodeInternPort() 
			
      self.assertIsNone(peer) 

		def test_getChainCodeAddress(self):
				
      peer = Peer().getChainCodeAddress() 
			
      self.assertIsNone(peer) 

		def test_create_couchdb(self):
				
      peer = Peer().create_couchdb() 
			
      self.assertIsNone(peer) 

		def test_getCouchDbHostname(self):
				
      peer = Peer().getCouchDbHostname() 
			
      self.assertIsNone(peer) 

		def test_getCouchDb(self):
				
      peer = Peer().getCouchDb() 
			
      self.assertIsNone(peer) 
		