import re, urllib2
from datetime import datetime
from validvalues import *

def matches_expression(input, regex):
    try:
        match = re.match(regex, input)
    except:
        # Exception raised here probably means invalid RegEx
        return False
    
    # If there was no match, match will be None
    if match == None: return False
    # If these lengths are different, then the RegEx only matched PART of the input's content.
    if len(match.group(0)) != len(input): return False
    
    # Passed: 
    return True

def is_valid_something(input):
    # Simply to test whether or not a field has any content in it.
    if len(input) > 0:
        return True
    else:
        return False
    
def is_valid_date(input):
    # Date is valid if it matches a RegEx meant to capture ISO 8601 format
    date_regex = '^[1-2][0-9]{3}-[0-1][0-9]-[0-3][0-9]T[0-2][0-9]:[0-6][0-9]:[0-6][0-9]$'
    return matches_expression(input, date_regex)
    
def is_valid_email(input):
    # Email is valid if it matches a RegEx meant to capture email addresses
    email_regex = '^.+@.+\..+$'
    return matches_expression(input, email_regex)

def is_valid_phone(input):
    # Phone is valid if it matches a RegEx meant to capture phone numbers
    phone_regex = '^\+?[0-9]?-?\(?[0-9]{3}\)?[-\ ]?[0-9]{3}-?[0-9]{4}$'
    return matches_expression(input, phone_regex)

def is_valid_coordinate(input):
    # Coordinate is valid if it is a number
    try:
        float(input)
    except:
        return False
    else:
        return True

def is_valid_latitude(input):
    # Latitude is valid if it is a valid coordinate, and it is within -90 > 90
    if is_valid_coordinate(input):
        if float(input) >= -90 and float(input) <= 90:
            return True
        else:
            return False
    else:
        return False

def is_valid_longitude(input):
    # Longitude is valid if it is a valid coordinate, and it is within -180 > 180
    if is_valid_coordinate(input):
        if float(input) >= -180 and float(input) <= 180:
            return True
        else:
            return False
    else:
        return False

def is_valid_url(input):
    # URL is valid if I get a response from it
    req = urllib2.Request(input)
    try:
        urllib2.urlopen(req)
    except:
        return False
    else:
        return True

def is_valid_language_code(input):
    if input in VALID_LANGUAGE_CODES:
        return True
    else:
        return False

def is_valid_unit_of_length(input):
    if input in VALID_LENGTH_UNITS:
        return True
    else:
        return False

# Methods for adjusting content that isn't quite right    
def fix_date(input):
    for format in COMMON_DATE_INPUT_FORMATS:
        try:
            result = datetime.strptime(input, format)
        except:
            continue
        else:
            result = result.isoformat()
            if is_valid_date(result):
                return result
    return None

def input_todays_date(input):
        today = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        return datetime.strptime(today, "%Y-%m-%d %H:%M:%S").isoformat()
    
def fix_language_code(input):
    result = input.lower()
    
    if result in COMMON_LANGUAGE_MISTAKES:
        result = COMMON_LANGUAGE_MISTAKES[result]
    
    if is_valid_language_code(result):
        return result
    else:
        return None

def fix_length_unit(input):
    result = input.lower()
    
    if result in COMMON_LENGTH_MISTAKES:
        result = COMMON_LENGTH_MISTAKES[result]
    
    if is_valid_unit_of_length(result):
        return result
    else:
        return None
    
def fix_uuid(input):
    result = str(uuid.uuid4())
    if is_valid_something(result):
        return result
    else:
        return None
    
# Method for assigning default values
def get_default_value(fieldname):
    result = None
    if fieldname in DEFAULT_VALUES:
        result = DEFAULT_VALUES[fieldname]
    
    return result
