import xml.etree.ElementTree as ET


class DynamicPhaseBundle:
    def __init__(self, parameters):
        self.parameters = parameters

    def __str__(self):
        return f"DynamicPhaseBundle(Parameters: {self.parameters})"

    def to_xml(self):
        bundle_elem = ET.Element("DynamicParameterClass")
        for param in self.parameters:
            param_elem = param.to_xml()
            bundle_elem.append(param_elem)
        return bundle_elem
