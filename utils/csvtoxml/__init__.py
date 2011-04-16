from lxml import etree

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
        if content.find('|') != -1:
            # There are pipe delimited things in here
            for item in content.split('|'):
                etree.SubElement(record, field).text = item.strip()
        else:
            etree.SubElement(record, field).text = row[field].strip()
    
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

def perform_transform(intermediate, transformation):
    try:
        result = transformation(intermediate)
    except Exception, ex:
        raise ex
    else:
        return result