
import unittest

		
class ChainCodeTest(unittest.TestCase):
		"""
		Tests for methods in the <_ast.ClassDef object at 0x7f2c1575f198> class.
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
	
		def test_getIntantiate(self):
				
      chaincode = ChainCode().getIntantiate() 
			
      self.assertIsNone(chaincode) 

		def test_getChainCodeOrg(self):
				
      chaincode = ChainCode().getChainCodeOrg() 
			
      self.assertIsNone(chaincode) 

		def test_getChainCodeQueryRequest(self):
				
      chaincode = ChainCode().getChainCodeQueryRequest() 
			
      self.assertIsNone(chaincode) 

		def test_getChainCodeQueryResponse(self):
				
      chaincode = ChainCode().getChainCodeQueryResponse() 
			
      self.assertIsNone(chaincode) 
		