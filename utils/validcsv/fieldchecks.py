from validvalues import *

def string_is_in_list(input, some_list):
    if input in some_list:
        return True
    else:
        return False
    
def required_fields_are_present(reader):
    input_set = set(reader.fieldnames)
    
    if len(set(REQUIRED_FIELDS).difference(input_set)) > 0: return False
    for one_of_list in ONE_OF_FIELDS:
        if len(set(one_of_list).difference(input_set)) == len(one_of_list): return False
    return True

def fields_missing(reader, required=True):
    if required:
        fields = REQUIRED_FIELDS
        conditionals = ONE_OF_FIELDS
    else:
        fields = OPTIONAL_FIELDS
        conditionals = OPTIONAL_ONE_OF_FIELDS
    
    input_set = set(reader.fieldnames)
    result = list()
    
    missing_set = set(fields).difference(input_set)
    for missing in missing_set: result.append(missing)
    
    for one_of_list in conditionals:
        missing_set = set(one_of_list).difference(input_set)
        if len(missing_set) == len(one_of_list):
            for missing in missing_set: result.append(missing)
            
    return result   

def extra_fields_present(reader):    
    input_set = set(reader.fieldnames)
    
    fields = set(REQUIRED_FIELDS).union(set(OPTIONAL_FIELDS))
    for one_of_list in ONE_OF_FIELDS:
        fields = fields.union(set(one_of_list))
    for one_of_list in OPTIONAL_ONE_OF_FIELDS:
        fields = fields.union(set(one_of_list))
    
    return list(input_set.difference(fields))