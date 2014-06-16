from fieldchecks import *
from valuechecks import *
from validvalues import *

'''
This is a nifty thing:
The dictionary is keyed on field names. So you can look up with FIELD_VALIDATION_RULES[fieldname]
What you get is a tuple with potentially two methods to call: The first is the method to call to validate, second to fix, third is conditional set
examples:
FIELD_VALIDATION_RULES['title'][0]('This is my title') will validate the title I gave it ("This is my title")
FIELD_VALIDATION_RULES['publication_date'][0]('2000-1-1T12:00') will validate the given date string ("2000-1-1T12:00")
FIELD_VALIDATION_RULES['publication_date'][1]('2000-1-1T12:00') will attempt to fix the given date string...

This includes optional fields. If the field is used, then it does need to be valid.
'''
FIELD_VALIDATION_RULES = {'title': (is_valid_something, None, None),
                          'description': (is_valid_something, None, None),
                          'publication_date': (is_valid_date, fix_date, None),
                          'metadata_contact_org_name': (is_valid_something, None, None),
                          'metadata_contact_email': (is_valid_email, None, None),
                          'originator_contact_org_name': (is_valid_something, None, 'originator_contact'), 
                          'originator_contact_person_name': (is_valid_something, None, 'originator_contact'), 
                          'originator_contact_position_name': (is_valid_something, None, 'originator_contact'),
                          'originator_contact_email': (is_valid_email, None, 'originator_contact_method'), 
                          'originator_contact_phone': (is_valid_something, None, 'originator_contact_method'),
                          'metadata_uuid': (is_valid_something, fix_uuid, None),
                          'metadata_date': (is_valid_date, input_todays_date, None),
                          'resource_url': (is_valid_url, None, 'resource_url_method'),
			  'resource_access_instruction': (is_valid_something, None, 'resource_url_method'),}
                          

OPTIONAL_FIELD_VALIDATION_RULES = {'originator_contact_fax': (is_valid_phone, None, None),
                                   'originator_contact_url': (is_valid_url, None, None),
                                   'elevation_units': (is_valid_unit_of_length, fix_length_unit, None),
                                   'temporal_start_date': (is_valid_date, fix_date, None),
                                   'temporal_end_date': (is_valid_date, fix_date, None),
                                   'resource_languages': (is_valid_language_code, fix_language_code, None),
                                   'resource_url': (is_valid_url, None, None),
                                   'distributor_contact_org_name': (is_valid_something, None, 'distributor_contact'),
                                   'distributor_contact_person_name': (is_valid_something, None, 'distributor_contact'),
                                   'distributor_contact_position_name': (is_valid_something, None, 'distributor_contact'),
                                   'distributor_contact_email': (is_valid_email, None, 'distributor_contact_method'),
                                   'distributor_contact_phone': (is_valid_phone, None, 'distributor_contact_method'),
                                   'distributor_contact_fax': (is_valid_phone, None, None),
                                   'distributor_contact_url': (is_valid_url, None, None),                                   
                                   'metadata_language': (is_valid_language_code, fix_language_code, None),
                                   'metadata_contact_phone': (is_valid_phone, None, None),
                                   'metadata_contact_fax': (is_valid_phone, None, None),
                                   'metadata_contact_url': (is_valid_url, None, None),
                                   'north_bounding_latitude': (is_valid_latitude, None, None),
                                   'south_bounding_latitude': (is_valid_latitude, None, None),
                                   'east_bounding_longitude': (is_valid_longitude, None, None),
                                   'west_bounding_longitude': (is_valid_longitude, None, None),}

CONDITIONAL_SET_LIMITS = {'originator_contact': (3, 'One of [originator_contact_org_name, originator_contact_person_name, originator_contact_position_name] must be populated.'),
                          'originator_contact_method': (2, 'One of [originator_contact_email, originator_contact_phone] must be populated.'),
                          'distributor_contact': (3, 'One of [distributor_contact_org_name, distributor_contact_person_name, distributor_contact_position_name] must be populated.'),
                          'distributor_contact_method': (2, 'One of [distributor_contact_email, distributor_contact_phone] must be populated.'),
			  'resource_url_method':(2, 'One of [resource_url, resource_access_instruction] must be populated.')}
def validate_fields(reader):
    report = list()
    
    # Check that required fields are present
    if not required_fields_are_present(reader):
        result = False
        missing_fields = fields_missing(reader, required=True)
        for missing in missing_fields:
            report.append('The required field: ' + missing + ' is not present.')
        extra_fields = extra_fields_present(reader)
        if len(extra_fields) > 0:
            report.append('The following extra fields were found in your document. Should any of them be renamed?')
            for extra in extra_fields:
                report.append('\t' + extra)
        
        # Do not bother with any more validation
        return False, report
    else:
        return True, report

def validate_row(index, row, fields):
    result = True
    report = list()
    conditional_failures = dict()
    optional_condition_failures = dict()
    for field in fields:
        if field in FIELD_VALIDATION_RULES:
            validation = FIELD_VALIDATION_RULES[field]
            # Use tuple in FIELD_VALIDATION_RULES to validate the row's field content
            if not validation[0](row[field]):
                # Did not validate.
                if validation[2] != None:
                    # Content is part of a conditional set
                    try:
                        # Increment the counter on the conditional set
                        conditional_failures[validation[2]] = conditional_failures[validation[2]] + 1
                    except KeyError:
                        # Start the counter on the conditional set
                        conditional_failures[validation[2]] = 1
                else:
                    if validation[1] != None:
                        # A fix method is given, try to repair
                        repaired = validation[1](row[field])
                        if repaired == None:
                            # Could not be fixed.
                            result = False
                            report.append('ERROR: Row #' + str(index) + ': ' + field + ' contains invalid content which could not be repaired.')
                        else:
                            # Content was fixed.
                            row[field] = repaired
                    elif get_default_value(field) != None:
                        # There is a default value available
                        row[field] = get_default_value(field)
                    else:
                        # There is no method for fixing this content
                        result = False
                        report.append('ERROR: Row #' + str(index) + ': ' + field + ' contains invalid content.')
        # Should find a way to do this and satisfy DRY.......
        if field in OPTIONAL_FIELD_VALIDATION_RULES:
            validation = OPTIONAL_FIELD_VALIDATION_RULES[field]
            if not validation[0](row[field]):
                if validation[2] != None:
                    try:
                        optional_condition_failures[validation[2]] = optional_condition_failures[validation[2]] + 1
                    except KeyError:
                        optional_condition_failures[validation[2]] = 1
                else:
                    if validation[1] != None:
                        repaired = validation[1](row[field])
                        if repaired == None:
                            report.append('WARNING: Row #' + str(index) + ': ' + field + ' contains invalid content which could not be repaired.')
                        else:
                            row[field] = repaired
                    elif get_default_value(field) != None:
                        row[field] = get_default_value(field)
                    else:
                        report.append('WARNING: Row #' + str(index) + ': ' + field + ' contains invalid content.')
    for conditional_set in conditional_failures:
        if conditional_failures[conditional_set] >= CONDITIONAL_SET_LIMITS[conditional_set][0]:
            # A conditional set was failed entirely
            result = False
            report.append('ERROR: Row #' + str(index) + ': ' + CONDITIONAL_SET_LIMITS[conditional_set][1])
    for optional_condition_set in optional_condition_failures:
        if optional_condition_failures[optional_condition_set] >= CONDITIONAL_SET_LIMITS[optional_condition_set][0]:
            # An optional conditional set was failed entirely
            report.append('WARNING: Row #' + str(index) + ': ' + CONDITIONAL_SET_LIMITS[optional_condition_set][1])
    
    print "CSV Validation - Row #" + str(index) + ": " + str(result)
    if not result:
        for item in report: print item        
    return result, report

def validate(reader):
    '''
    Attempts to validate a csv.DictReader object.
    Within bounds, it will try and adjust the original to be valid
    
    Always returns three variables
    If the DictReader can be validated: True, Report, List of valid dictionaries
    If not: False, Report, empty list
    
    The Report will always be a list of strings describing problems in the reader
    '''
    result = True
    report = list()
    output = list()
    
    # Check that required fields are present
    if not required_fields_are_present(reader):
        result = False
        missing_fields = fields_missing(reader, required=True)
        for missing in missing_fields:
            report.append('The required field: ' + missing + ' is not present.')
        extra_fields = extra_fields_present(reader)
        if len(extra_fields) > 0:
            report.append('The following extra fields were found in your document. Should any of them be renamed?')
            for extra in extra_fields:
                report.append('\t' + extra)
        
        # Do not bother with any more validation
        return False, report, list(reader)
    
    # Check that field content is valid
    for index, row in enumerate(reader):
        conditional_failures = dict()
        optional_condition_failures = dict()
        for field in reader.fieldnames:
            if field in FIELD_VALIDATION_RULES:
                validation = FIELD_VALIDATION_RULES[field]
                # Use tuple in FIELD_VALIDATION_RULES to validate the row's field content
                if not validation[0](row[field]):
                    # Did not validate.
                    if validation[2] != None:
                        # Content is part of a conditional set
                        try:
                            # Increment the counter on the conditional set
                            conditional_failures[validation[2]] = conditional_failures[validation[2]] + 1
                        except KeyError:
                            # Start the counter on the conditional set
                            conditional_failures[validation[2]] = 1
                    else:
                        if validation[1] != None:
                            # A fix method is given, try to repair
                            repaired = validation[1](row[field])
                            if repaired == None:
                                # Could not be fixed.
                                result = False
                                report.append('ERROR: Row #' + str(index) + ': ' + field + ' contains invalid content which could not be repaired.')
                            else:
                                # Content was fixed.
                                row[field] = repaired
                        elif get_default_value(field) != None:
                            # There is a default value available
                            row[field] = get_default_value(field)
                        else:
                            # There is no method for fixing this content
                            result = False
                            report.append('ERROR: Row #' + str(index) + ': ' + field + ' contains invalid content.')
            # Should find a way to do this and satisfy DRY.......
            if field in OPTIONAL_FIELD_VALIDATION_RULES:
                validation = OPTIONAL_FIELD_VALIDATION_RULES[field]
                if not validation[0](row[field]):
                    if validation[2] != None:
                        try:
                            optional_condition_failures[validation[2]] = optional_condition_failures[validation[2]] + 1
                        except KeyError:
                            optional_condition_failures[validation[2]] = 1
                    else:
                        if validation[1] != None:
                            repaired = validation[1](row[field])
                            if repaired == None:
                                report.append('WARNING: Row #' + str(index) + ': ' + field + ' contains invalid content which could not be repaired.')
                            else:
                                row[field] = repaired
                        elif get_default_value(field) != None:
                            row[field] = get_default_value(field)
                        else:
                            report.append('WARNING: Row #' + str(index) + ': ' + field + ' contains invalid content.')
        for conditional_set in conditional_failures:
            if conditional_failures[conditional_set] >= CONDITIONAL_SET_LIMITS[conditional_set][0]:
                # A conditional set was failed entirely
                result = False
                report.append('ERROR: Row #' + str(index) + ': ' + CONDITIONAL_SET_LIMITS[conditional_set][1])
        for optional_condition_set in optional_condition_failures:
            if optional_condition_failures[optional_condition_set] >= CONDITIONAL_SET_LIMITS[conditional_set][0]:
                # An optional conditional set was failed entirely
                report.append('WARNING: Row #' + str(index) + ': ' + CONDITIONAL_SET_LIMITS[optional_condition_set][1])
        
        # Append the adjusted content to the output
        output.append(row)
        
    # Notify of any extra fields
    extra_fields = extra_fields_present(reader)
    if len(extra_fields) > 0:
        report.append('The following extra fields were found in your document. Should any of them be renamed? Data contained in them will not be used in your metadata documents.')
        for extra in extra_fields:
            report.append('\t' + extra)
                        
    if result == True:
        return result, report, output
    else:
        return result, report, output
