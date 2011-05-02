import os, uuid, glob, urllib2
from StringIO import StringIO
from lxml import etree
from xmlvalidator import *
from utils.validcsv import validate
from utils.readcsv import csv_to_dict_reader
from utils.csvtoxml import transform_valid_csv, CURRENT_XSLT_PATH

rule_string = urllib2.urlopen('http://services.usgin.org/validation/ruleset/1/list/').read()
exec rule_string
minimum_rules = UsginMinRules()

ns = {'gmd': 'http://www.isotc211.org/2005/gmd',
      'srv': 'http://www.isotc211.org/2005/srv',
      'gco': 'http://www.isotc211.org/2005/gco',
      'gml': 'http://www.opengis.net/gml',
      'xlink': 'http://www.w3.org/1999/xlink',
      'xsi': 'http://www.w3.org/2001/XMLSchema-instance'}

def validatecsv(filepath):
    reader = csv_to_dict_reader(filepath)
    return validate(reader)

def save_metadata(record_to_save, place_to_save_it):
    # Record should have a file identifier - find it.
    try:
        file_ish = StringIO(record_to_save)
        record = etree.parse(file_ish)
        fileId = record.xpath('//gmd:fileIdentifier/gco:CharacterString', namespaces=ns)[0]
    except Exception, ex:
        raise ex
    
    # This should really be handled at the validation level. By this point should have fileIdentifier
    if fileId.text == None:
        id = str(uuid.uuid4())
    else:
        id = fileId.text
        
    filepath = os.path.join(place_to_save_it, id + '.xml')
    
    try:
        file = open(filepath, 'w')
        file.write(record_to_save)
        file.close()
    except Exception, ex:
        raise ex
    
    validate_output(filepath)
    
def validate_output(file):
    try:
        result, report = record_is_valid(file, minimum_rules)
    except ValidationException, ex:
        raise ex
    if result == False:
        print 'FAILED VALIDATION: ' + file
        for item in report: print item
    else:
        print 'PASSED VALIDATION: ' + file
            
def transformcsv(csv_filepath, output_folder_path):
    result, report, output = validatecsv(csv_filepath)
    if result == True:
        output = transform_valid_csv(output, CURRENT_XSLT_PATH)
        for metadata_record in output:
            save_metadata(metadata_record, output_folder_path)
    else:
        print 'CSV DOCUMENT FAILED VALIDATION'
    
    for report_entry in report: print report_entry