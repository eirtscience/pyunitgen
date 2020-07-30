
import unittest

		
class OrganizationTest(unittest.TestCase):
		"""
		Tests for methods in the <_ast.ClassDef object at 0x7f2c1577f908> class.
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
	
		def test_getId(self):
				
      organization = Organization().getId() 
			
      self.assertIsNone(organization) 

		def test_isAdmin(self):
				
      organization = Organization().isAdmin() 
			
      self.assertIsNone(organization) 

		def test_getCaCertificate(self):
				
      organization = Organization().getCaCertificate() 
			
      self.assertIsNone(organization) 

		def test_create_certificate(self):
				
      organization = Organization().create_certificate() 
			
      self.assertIsNone(organization) 

		def test_addAllPeers(self):
				
      organization = Organization().addAllPeers() 
			
      self.assertIsNone(organization) 

		def test_peerLen(self):
				
      organization = Organization().peerLen() 
			
      self.assertIsNone(organization) 

		def test_getmspdir(self):
				
      organization = Organization().getmspdir() 
			
      self.assertIsNone(organization) 

		def test_getlist_policies(self):
				
      organization = Organization().getlist_policies() 
			
      self.assertIsNone(organization) 

		def test_getDomain(self):
				
      organization = Organization().getDomain() 
			
      self.assertIsNone(organization) 

		def test_getNotDomainName(self):
				
      organization = Organization().getNotDomainName() 
			
      self.assertIsNone(organization) 

		def test_getAdminEmail(self):
				
      organization = Organization().getAdminEmail() 
			
      self.assertIsNone(organization) 

		def test_getAnchorPeer(self):
				
      organization = Organization().getAnchorPeer() 
			
      self.assertIsNone(organization) 

		def test_getGossipPeer(self):
				
      organization = Organization().getGossipPeer() 
			
      self.assertIsNone(organization) 

		def test_getGossipPeerBootstrapByPeerId(self):
				
      organization = Organization().getGossipPeerBootstrapByPeerId() 
			
      self.assertIsNone(organization) 

		def test_getConfigurationPath(self):
				
      organization = Organization().getConfigurationPath() 
			
      self.assertIsNone(organization) 

		def test_getPeerPem(self):
				
      organization = Organization().getPeerPem() 
			
      self.assertIsNone(organization) 

		def test_getCaPem(self):
				
      organization = Organization().getCaPem() 
			
      self.assertIsNone(organization) 

		def test_dump(self):
				
      organization = Organization().dump() 
			
      self.assertIsNone(organization) 
		