import unittest, os, csv
from lxml import etree
from csvtometadata.utils.readcsv import *
from constants import *

class ReaderTests(unittest.TestCase):
    def setUp(self):
        self.example_file_path = EXAMPLE_FILE_PATH
        self.template_file_path = TEMPLATE_RECORD_PATH
        self.invalid_file_path = '/does/not/exist/file.crap'
        
    def test_dict_reader(self):
        # Test file returns what I expect it to
        expected_output = csv.DictReader(open(self.example_file_path))
        actual_output = csv_to_dict_reader(self.example_file_path)
        expected_list = list(expected_output)
        self.assertEqual(actual_output.fieldnames, expected_output.fieldnames)
        for row_num, row in enumerate(actual_output):
            self.assertEqual(row, expected_list[row_num])
        # Invalid file raises exception
        self.assertRaises(IOError, csv_to_dict_reader, csv_file_path=self.invalid_file_path)