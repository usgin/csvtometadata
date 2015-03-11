import unittest, os, csv
from lxml import etree
from csvtometadata.utils.readcsv import *
from csvtometadata.utils.validcsv.validvalues import *
from csvtometadata.utils.validcsv.fieldchecks import *
from csvtometadata.utils.validcsv.valuechecks import *
from csvtometadata.utils.validcsv import validate
from constants import *

class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.example_reader = csv_to_dict_reader(EXAMPLE_FILE_PATH)
        self.valid_reader = csv_to_dict_reader(VALID_FILE_PATH)
        self.invalid_reader = csv_to_dict_reader(INVALID_FILE_PATH)
        self.invalid_content_reader = csv_to_dict_reader(INVALID_CONTENT_FILE_PATH)
        
    def test_required_fields_are_present(self):
        self.assertTrue(required_fields_are_present(self.valid_reader))
        self.assertFalse(required_fields_are_present(self.invalid_reader))
            
    def test_fields_missing(self):
        self.assertEqual(fields_missing(self.valid_reader), [])
        expected_outcome = ['title','originator_contact_org_name', 'originator_contact_person_name', 'originator_contact_position_name']
        for missing in fields_missing(self.invalid_reader):
            self.assertTrue(missing in expected_outcome)
        
        self.assertEqual(fields_missing(self.valid_reader, required=False), [])
        self.assertEqual(fields_missing(self.invalid_reader, required=False), ['resource_type'])
            
    def test_extra_fields_present(self):
        self.assertEqual(extra_fields_present(self.valid_reader), [])
        self.assertEqual(extra_fields_present(self.invalid_reader), ['pandas'])
            
    def test_matches_expression(self):
        # Test for Success
        self.assertTrue(matches_expression('hello', 'hello'))
        
        # Test for Failure
        self.assertFalse(matches_expression('input', 'output'))
        
        # Test for sub-match
        self.assertFalse(matches_expression('hello', 'ell'))
        
        # Poorly formed expression
        self.assertFalse(matches_expression('hello', '/?!11~~..++'))
        
    def test_is_valid_date(self):
        # Only ISO 8601 formatted dates should pass
        self.assertTrue(is_valid_date('2009-11-17T10:00:00'))
        self.assertFalse(is_valid_date('11/12/2009'))
        self.assertFalse(is_valid_date('something else'))
        
    def test_is_valid_email(self):
        self.assertTrue(is_valid_email('ryan.clark@azgs.az.gov'))
        self.assertTrue(is_valid_email('ryan@azgs.com'))
        self.assertFalse(is_valid_email('ryan.clark@azgs'))
        self.assertFalse(is_valid_email('garbage'))
    
    def test_is_valid_phone(self):
        self.assertTrue(is_valid_phone('1-234-234-2345'))
        self.assertTrue(is_valid_phone('234-234-2345'))
        self.assertTrue(is_valid_phone('12345678910'))
        self.assertTrue(is_valid_phone('2345678910'))
        self.assertTrue(is_valid_phone('(520) 770-3500'))
        self.assertFalse(is_valid_phone('not correct'))
        self.assertFalse(is_valid_phone('234-5678'))
        
    def test_is_valid_coordinate(self):
        self.assertTrue(is_valid_coordinate('1'))
        self.assertTrue(is_valid_coordinate('1.2'))
        self.assertFalse(is_valid_coordinate('not valid'))
        
    def test_is_valid_latitude(self):
        self.assertTrue(is_valid_latitude('45'))
        self.assertTrue(is_valid_latitude('-45'))
        self.assertTrue(is_valid_latitude('90'))
        self.assertTrue(is_valid_latitude('-90'))
        self.assertFalse(is_valid_latitude('91'))
        self.assertFalse(is_valid_latitude('-91'))
        
    def test_is_valid_longitude(self):
        self.assertTrue(is_valid_longitude('45'))
        self.assertTrue(is_valid_longitude('-45'))
        self.assertTrue(is_valid_longitude('180'))
        self.assertTrue(is_valid_longitude('-180'))
        self.assertFalse(is_valid_longitude('181'))
        self.assertFalse(is_valid_longitude('-181'))
        
    def test_is_valid_url(self):
        self.assertTrue(is_valid_url('http://www.azgs.az.gov'))
        self.assertFalse(is_valid_url('azgs.az.gov'))
        self.assertFalse(is_valid_url('goobledeegook'))
    
    def test_is_valid_language_code(self):
        for code in VALID_LANGUAGE_CODES:
            self.assertTrue(is_valid_language_code(code))
        self.assertFalse(is_valid_language_code('English'))
        
    def test_is_valid_unit_of_length(self):
        for unit in VALID_LENGTH_UNITS:
            self.assertTrue(is_valid_unit_of_length(unit))
        self.assertFalse(is_valid_unit_of_length('balderdash'))
    
    def test_fix_date(self):
        formats = ['1/1/2000',
                   '1/1/2000T00:00',
                   'Jan. 1 2000',
                   'Jan. 1, 2000',                   
                   'Jan 1 2000',
                   'Jan 1, 2000',
                   'January 1 2000',
                   'January 1, 2000',
                   '1-1-2000',
                   '1-1-2000T00:00',
                   '1-1-2000 00:00',
                   '1/1/2000 00:00',
                   '1/2000',
                   'Jan. 2000',
                   'Jan 2000',
                   'January 2000',
                   '2000-01-01T00:00']
        for format in formats:
            self.assertEqual(fix_date(format), '2000-01-01T00:00:00')
        self.assertEqual(fix_date('You cannot fix this'), None)
        
    def test_fix_language_code(self):
        self.assertEqual(fix_language_code('English'), 'eng')
        self.assertEqual(fix_language_code('ENG'), 'eng')
        self.assertEqual(fix_language_code('You cannot fix this'), None)
    
    def test_fix_length_unit(self):
        self.assertEqual(fix_length_unit('Feet'), 'ft')
        self.assertEqual(fix_length_unit('mEtErs'), 'm')
        self.assertEqual(fix_length_unit('You cannot fix this'), None)
            
    def test_get_default_value(self):
        for value in DEFAULT_VALUES:
            self.assertEqual(get_default_value(value), DEFAULT_VALUES[value])
        self.assertEqual(get_default_value('bad fieldname'), None)
    
    def test_validate(self):
        is_valid, report, result = validate(self.valid_reader)
        self.assertTrue(is_valid, 'Valid document did not pass validation.')
        self.assertEqual(result, [{'surface_elevation': '869.000000', 'metadata_contact_city': '', 'resource_access_instruction': 'Access the imaginary resource through dreams.', 'metadata_contact_fax': '', 'resource_languages': 'eng', 'resource_id': 'http://resource.usgin.org/uri-gin/dlio/OFR-2001-09', 'metadata_contact_org_name': 'Arizona Geological Survey', 'metadata_contact_street_address': '', 'north_bounding_latitude': '75.000000', 'distributor_contact_city': 'Tucson', 'originator_contact_phone': '(520) 770-3500', 'distributor_contact_person_name': '', 'originator_contact_city': 'Tucson', 'metadata_language': 'eng', 'publication_date': '2010-01-01T00:00:00', 'keywords_spatial': 'North America | Arizona', 'metadata_date': '2010-08-19T12:00:00', 'south_bounding_latitude': '17.000000', 'distributor_contact_zip': '85701', 'metadata_uuid': '165d8100-abd3-11df-94e2-0800200c9a66', 'title': 'Metadata Record Showcase', 'metadata_contact_state': '', 'originator_contact_person_name': 'Geologist, A. | Igneous, Rocky', 'metadata_contact_phone': '', 'originator_contact_org_name': 'Arizona Geological Survey', 'distributor_contact_street_address': '416 W. Congress St., Suite 100', 'originator_contact_url': 'http://www.azgs.az.gov/contact.shtml', 'datum_elevation': '0', 'distributor_contact_email': 'metadata@usgin.org', 'interval_depth_top': '0', 'interval_depth_bottom': '7825', 'keywords_thematic': 'test | dummy', 'bibliographic_citation': 'Grunberg, Wolfgang, Stephen Richard and Jordan Hastings. Metadata Record Showcase. 0 pp. Tucson, 2010.', 'distributor_contact_phone': '', 'distributor_contact_fax': '', 'metadata_contact_zip': '', 'metadata_contact_person_name': '', 'description': 'This is a test metadata record.', 'resource_lineage_statement': '', 'distributor_contact_org_name': '', 'metadata_contact_email': 'metadata@azgs.az.gov', 'distributor_contact_url': 'http://lab.usgin.org', 'metadata_contact_position_name': '', 'distributor_contact_position_name': '', 'keywords_temporal': 'Cenozoic | Phanerozoic', 'originator_contact_state': 'AZ', 'west_bounding_longitude': '-64.000000', 'distributor_contact_state': 'AZ', 'temporal_start_date': '', 'resource_quality_statement': 'This resource has not been validated.', 'resource_constraints_statement': 'Creative Commons License: Attribution + ShareAlike (cc-by-sa)', 'originator_contact_fax': ' (520) 770-3505', 'originator_contact_email': '', 'metadata_contact_url': '', 'elevation_units': 'ft', 'originator_contact_street_address': '416 W. Congress St., Suite 100', 'related_resource': '', 'temporal_end_date': '', 'originator_contact_position_name': '', 'east_bounding_longitude': '-180.000000', 'originator_contact_zip': '85701', 'resource_url': '', 'resource_type': 'Document: Text'}])
        
        is_valid, report, result = validate(self.invalid_reader)
        self.assertFalse(is_valid)
        self.assertEqual(report, ['The required field: title is not present.', 'The required field: originator_contact_position_name is not present.', 'The required field: originator_contact_person_name is not present.', 'The required field: originator_contact_org_name is not present.', 'The following extra fields were found in your document. Should any of them be renamed?', '\tpandas'])
        
        is_valid, report, result = validate(self.invalid_content_reader)
        self.assertFalse(is_valid)
        self.assertEqual(report, ['ERROR: Row #0: title contains invalid content.', 'ERROR: Row #0: publication_date contains invalid content which could not be repaired.', 'WARNING: Row #0: originator_contact_fax contains invalid content.', 'WARNING: Row #0: temporal_start_date contains invalid content which could not be repaired.', 'WARNING: Row #0: temporal_end_date contains invalid content which could not be repaired.', 'WARNING: Row #0: resource_url contains invalid content.', 'WARNING: Row #0: distributor_contact_fax contains invalid content.', 'WARNING: Row #0: metadata_contact_phone contains invalid content.', 'WARNING: Row #0: metadata_contact_fax contains invalid content.', 'WARNING: Row #0: metadata_contact_url contains invalid content.', 'ERROR: Row #0: One of [originator_contact_org_name, originator_contact_person_name, originator_contact_position_name] must be populated.', 'WARNING: Row #0: One of [distributor_contact_org_name, distributor_contact_person_name, distributor_contact_position_name] must be populated.'])
        