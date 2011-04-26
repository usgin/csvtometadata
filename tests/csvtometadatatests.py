import unittest
from csvtometadata import *
from constants import *

class CsvToMetadataTests(unittest.TestCase):
    def setUp(self):
        self.example_reader = csv_to_dict_reader(EXAMPLE_FILE_PATH)
        self.example_file_path = EXAMPLE_FILE_PATH
        self.adjusted_example_file_path = ADJUSTED_EXAMPLE_FILE_PATH
        self.output_path = OUTPUT_PATH
        
    def test_validatecsv(self):
        result, report, response = validatecsv(self.adjusted_example_file_path)
        self.assertTrue(result)
        self.assertEqual(report, ['The following extra fields were found in your document. Should any of them be renamed? Data contained in them will not be used in your metadata documents.', '\toriginators', '\tresource_id_protocol'])
        
        result, report, response = validatecsv(self.example_file_path)
        self.assertFalse(result)
        self.assertEqual(report, ['The required field: metadata_contact_org_name is not present.', 'The following extra fields were found in your document. Should any of them be renamed?', '\tmetadata_contact_name', '\toriginators', '\tresource_id_protocol'])
    
    def test_transformcsv(self):
        # This just runs the damn thing against the valid file.
        transformcsv(VALID_FILE_PATH, self.output_path)
        
        # Then tries to validate the outcome
        # validate_output(self.output_path)
        
    def tearDown(self):
        for the_file in os.listdir(self.output_path):
            file_path = os.path.join(self.output_path, the_file)
            
            if os.path.isfile(file_path):
                os.unlink(file_path)

