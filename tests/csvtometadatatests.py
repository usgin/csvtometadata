import unittest
from csvtometadata import *
from constants import *

class CsvToMetadataTests(unittest.TestCase):
    def setUp(self):
        self.example_reader = csv_to_dict_reader(EXAMPLE_FILE_PATH)
        self.example_file_path = EXAMPLE_FILE_PATH
        self.adjusted_example_file_path = ADJUSTED_EXAMPLE_FILE_PATH
        
    def test_validatecsv(self):
        result, report, response = validatecsv(self.adjusted_example_file_path)
        self.assertTrue(result)
        self.assertEqual(report, ['The following extra fields were found in your document. Should any of them be renamed? Data contained in them will not be used in your metadata documents.', '\toriginators', '\tresource_id_protocol'])
        
        result, report, response = validatecsv(self.example_file_path)
        self.assertFalse(result)
        self.assertEqual(report, ['The required field: metadata_contact_org_name is not present.', 'The following extra fields were found in your document. Should any of them be renamed?', '\tmetadata_contact_name', '\toriginators', '\tresource_id_protocol'])
        

        
