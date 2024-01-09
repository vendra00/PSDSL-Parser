import xml.etree.ElementTree as ET


class PhaseParameter:
    def __init__(self, name, usage_identifier, parameter_type, sort_index=None):
        self.name = name
        self.usage_identifier = usage_identifier
        self.parameter_type = parameter_type
        self.sort_index = sort_index

    def __str__(self):
        return (f"PhaseParameter("
                f"Name: {self.name}, "
                f"UsageIdentifier: {self.usage_identifier}, "
                f"SortIndex: {self.sort_index})")

    def to_xml(self):
        parameter_class_elem = ET.Element("ParameterClass")
        ET.SubElement(parameter_class_elem, "Name").text = self.name
        ET.SubElement(parameter_class_elem, "UsageIdentifier").text = self.usage_identifier
        if self.sort_index is not None:
            ET.SubElement(parameter_class_elem, "SortIndex").text = str(self.sort_index)
        return parameter_class_elem
