from pyunitgen.application.objects.pyunitreport import PyUnitReport,PyUnitReportValidation
import unittest

		
class PyUnitReportTest(unittest.TestCase):
		"""
		Tests for methods in the PyUnitReport class.
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
	
		def test_add(self):
			
      pyunitreport = PyUnitReport().add() 
			
      self.assertIsNone(pyunitreport) 

		def test_getReport(self):
			
      pyunitreport = PyUnitReport().getReport() 
			
      self.assertIsNone(pyunitreport) 
		