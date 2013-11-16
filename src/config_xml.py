import xml.etree.ElementTree as ET


class ConfigXML():
    def __init__(self, file_name):
        self.file_name = file_name
        self.xml_file = ET.parse(file_name)

    def get_node(self, attribute, xpath):
        tag = self.xml_file.findall(xpath)
        return tag[0].attrib[attribute]

    def set_node(self, attribute, xpath, value):
        tag = self.xml_file.findall(xpath)
        tag[0].attrib[attribute] = value
        self.write_xml()

    def write_xml(self):
        element = self.xml_file.getroot()
        var = ET.tostring(element, "utf-8", "xml")
        new_xml_file = open(self.file_name, 'w+')
        new_xml_file.write(var)
        new_xml_file.close()