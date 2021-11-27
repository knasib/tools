import xml.etree.ElementTree as ET
#import yamlreader

def getXMLTemplateElement(xml_string):
    return ET.ElementTree(ET.fromstring(xml_string))

def pretty(element):
    ET.indent(element)
    return ET.tostring(element, encoding='unicode')

#uglyxml = yamlreader.getProperties("xml.template")
#xml = pretty(getXMLTemplateElement(uglyxml))
#print(xml)
