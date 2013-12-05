import utils
import xml.etree.ElementTree as ET


class ConfigXML(object):
    def __init__(self, file_name="../config.xml"):
        """Constructor that sets the file_name of the configuration file.

        Keyword arguments:
        file_name -- name of the configuration file
        (default '../config.xml')

        """
        self.file_name = None
        if utils.exist_path(file_name):
            self.file_name = file_name
        else:
            print "The path " + file_name + "does not exist"
        self.xml_file = ET.parse(self.file_name)

    def get_node(self, attribute, xpath):
        """Return a node value according its attribute and xpath locator

         keyword arguments:
         attribute -- name of the attribute in a specific node
         (e.g. id, name, value)
         xpath -- xpath used to navigate through nodes or elements in
         the XML file (e.g. //parent/child)

        """
        tag = self.xml_file.findall(xpath)
        return tag[0].attrib[attribute]

    def set_node(self, attribute, xpath, value):
        """Set a specific node according its attribute and xpath locator

        keyword arguments:
        attribute -- name of the attribute in a specific node
        (e.g. id, name, value)
        xpath -- xpath used to navigate through nodes or elements in
        the XML file (e.g. //parent/child)
        value -- new value to set a node in the xml

        """
        tag = self.xml_file.findall(xpath)
        tag[0].attrib[attribute] = value
        self.write_xml()

    def write_xml(self):
        """ Write the current xml file variable into config.xml file"""
        element = self.xml_file.getroot()
        var = ET.tostring(element, "utf-8", "xml")
        new_xml_file = open(self.file_name, 'w+')
        new_xml_file.write(var)
        new_xml_file.close()