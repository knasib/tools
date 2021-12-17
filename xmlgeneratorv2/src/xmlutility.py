import xml.etree.ElementTree as et
# import yamlreader


def get_xml_template_element(xml_string):
    return et.ElementTree(et.fromstring(xml_string))


def pretty(element):
    et.indent(element)
    return et.tostring(element, encoding='unicode')


# ugl_xml = yamlreader.get_properties("xml.template")
# xml = pretty(get_xml_template_element(ugl_xml))
# print(xml)
