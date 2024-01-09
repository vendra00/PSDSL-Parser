import xml.etree.ElementTree as ET


class PhaseParameterType:
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def __str__(self):
        return (f"PhaseParameterType("
                f"Name: {self.name}, "
                f"Class: {self.path})")

    def to_xml(self):
        phase_parameter_type_elem = ET.Element("PhaseParameterType")
        ET.SubElement(phase_parameter_type_elem, "Name").text = self.name
        ET.SubElement(phase_parameter_type_elem, "Class").text = self.path

        return phase_parameter_type_elem
