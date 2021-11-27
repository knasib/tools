import os
import src.xmlutility as xmlutility
import src.yamlreader as yamlreader
import src.excelreader as excelreader


class XMLGenerator:
    def __init__(self) -> None:
        pass
 
    def getXmlKeysToUpdate(self):
        keys = yamlreader.getProperties('xml.keys')   
        return keys 

    def generate(self):
        xml = yamlreader.getProperties('xml.root')
        roottemplate = xmlutility.getXMLTemplateElement(xml)
        root = roottemplate.getroot()

        for rowindex in range(excelreader.getSize()):
            element = self.getElementForExcelRow(rowindex)
            root.append(element)

        return xmlutility.pretty(root)  

    def getElementForExcelRow(self, rowindex):
        xml = yamlreader.getProperties('xml.template')
        template = xmlutility.getXMLTemplateElement(xml)
        keys = self.getXmlKeysToUpdate()

        for keyindex in range(len(keys)):
            template.find(keys[keyindex]).text = excelreader.getCellValue(rowindex, keyindex)      

        #print(f"{rowindex}  --> {xmlutility.pretty(template.getroot().find(".//"))}")
        return template.getroot().find(".//")

    def writeToFile(self, filepath, xmlstr):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w') as file:
            file.write(xmlstr)

xmlgenerator = XMLGenerator()
xmlStr = xmlgenerator.generate()
if(yamlreader.getProperties('app.console-output') == True):
    print(xmlStr)

print(f'{yamlreader.getProperties("app.output")} is generated.')
xmlgenerator.writeToFile(yamlreader.getProperties('app.output'), xmlStr)