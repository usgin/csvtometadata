from lxml import etree
import os

CURRENT_XSLT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'xslt', 'starting-point.xslt')

def create_intermediate_xml(row, row_num=None):
    '''
    row is an input dictionary.
    I wonder if there will be problems if content is not valid UTF-8
    '''
    
    record = etree.Element("record")
    if row_num != None:
        record.attrib['rowId'] = str(row_num)
    for field in row:
        content = row[field]
        # Remove wierd characters (I don't completely understand the ord() function yet)
        content = ''.join(char if ord(char) < 128 else '' for char in content)
        
        if content.find('|') != -1:
            # There are pipe delimited things in here
            for item in content.split('|'):
                etree.SubElement(record, field).text = item.strip()
        else:
            try:
                etree.SubElement(record, field).text = content.strip()
            except ValueError, err:
                pass
            
    return record

def build_transform(xslt_path):
    try:
        file_tree = etree.parse(open(xslt_path))
    except Exception, ex:
        raise ex
    
    try:
        transform = etree.XSLT(file_tree)
    except Exception, ex:
        raise ex
    else:
        return transform

PARSED_XSLT = build_transform(CURRENT_XSLT_PATH)

def perform_transform(intermediate, transformation):
    try:
        result = transformation(intermediate)
    except Exception, ex:
        raise ex
    else:
        return result

def transform_valid_row(valid_row, xslt_path=None):
    if xslt_path == None:
        transformation = PARSED_XSLT
    else:
        transformation = build_transform(xslt_path)
    
    intermediate = create_intermediate_xml(valid_row)
    result = perform_transform(intermediate, transformation)
    return str(result)
        
def transform_valid_csv(valid_dict_reader, xslt_path):
    result = list()
    
    transformation = build_transform(xslt_path)
    row_num = 1
    for row in valid_dict_reader:
        intermediate = create_intermediate_xml(row, row_num)
        out = perform_transform(intermediate, transformation)
        result.append(str(out))
        row_num = row_num + 1
    return result
        