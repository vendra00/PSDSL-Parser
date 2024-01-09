import xml.etree.ElementTree as ET


class DynamicParameterClass:
    def __init__(self, name, usage_identifier, max_number, dependent_classes):
        self.name = name
        self.usage_identifier = usage_identifier
        self.max_number = max_number
        self.dependent_classes = dependent_classes

    def __str__(self):
        return (f"DynamicParameterClass(Name: {self.name}, "
                f"UsageIdentifier: {self.usage_identifier}, "
                f"MaxNumber: {self.max_number}, "
                f"DependentClasses: {self.dependent_classes})")

    def to_xml(self):
        dynamic_class_elem = ET.Element("DynamicParameterClass")
        ET.SubElement(dynamic_class_elem, "Name").text = self.name
        ET.SubElement(dynamic_class_elem, "UsageIdentifier").text = self.usage_identifier
        ET.SubElement(dynamic_class_elem, "MaximumNumber").text = str(self.max_number)
        for dep_class in self.dependent_classes:
            dep_class_elem = dep_class.to_xml()
            dynamic_class_elem.append(dep_class_elem)
        return dynamic_class_elem
