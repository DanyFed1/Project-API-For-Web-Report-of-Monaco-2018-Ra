import xml.etree.ElementTree as ET
def to_xml(data):
    """
    Convert a list of dictionaries or a single dictionary to an XML string.
    Example:
        to_xml([{'name': 'John', 'age': 30}, {'name': 'Jane', 'age': 25}])
        b'<data><item><name>John</name><age>30</age></item><item><name>Jane</name><age>25</age></item></data>'

        to_xml({'name': 'John', 'age': 30})
        b'<driver><name>John</name><age>30</age></driver>'
    """
    if isinstance(data, list):
        root = ET.Element('data')
        for item in data:
            element = ET.SubElement(root, 'item')
            for key, value in item.items():
                child = ET.SubElement(element, key)
                child.text = str(value)
    else:
        root = ET.Element('driver')
        for key, value in data.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
    return ET.tostring(root, encoding='utf-8', method='xml')
