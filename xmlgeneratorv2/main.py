import os
import src.xmlutility as xml_utility
import src.yamlreader as yamlreader
import src.excelreader as excelreader
from src.exceptions.keynotfoundexception import KeyNotFoundException


class XMLGenerator:
    def __init__(self) -> None:
        pass

    def get_xml_keys_to_update(self):
        keys = yamlreader.get_properties('xml.keys')
        return keys

    def get_xml_template(self):
        xml = yamlreader.get_properties('xml.template')
        template = xml_utility.get_xml_template_element(xml)
        return template

    def validate_keys(self, keys, template):
        for key_index in range(len(keys)):
            if template.find(keys[key_index]) is None:
                print(
                    f'Key: `{keys[key_index]}` is not present in defined template. Update the application.yaml file '
                    f'under xml.keys with key number[{key_index+1}]')
                exit(4)

    def generate(self):
        keys = self.get_xml_keys_to_update()
        root_template = self.get_xml_template()
        self.validate_keys(keys, root_template)
        root = root_template.getroot()

        for row_index in range(excelreader.get_size()):
            element = self.get_element_for_excel_row(row_index, keys, root_template)
            root.append(element)
        return xml_utility.pretty(root)

    def get_element_for_excel_row(self, row_index, keys, template):
        for key_index in range(len(keys)):
            template.find(keys[key_index]).text = str(excelreader.get_cell_value(row_index, key_index))

        # print(f"{row_index}  --> {xml_utility.pretty(template.getroot().find(".//"))}")
        return template.getroot().find(".//")

    def write_to_file(self, filepath, xml_str):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w') as file:
            file.write(xml_str)


xml_generator = XMLGenerator()
xmlStr = xml_generator.generate()
if yamlreader.get_properties('app.console-output'):
    print(xmlStr)

print(f'{yamlreader.get_properties("app.output")} is generated.')
xml_generator.write_to_file(yamlreader.get_properties('app.output'), xmlStr)
