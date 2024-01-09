import xml.etree.ElementTree as ET
class DynamicPhaseParameters:
    def __init__(self, max_number, bundles):
        self.max_number = max_number
        self.bundles = bundles

    def __str__(self):
        return f"DynamicPhaseParameters(MaxNumber: {self.max_number}, Bundles: {self.bundles})"

    def to_xml(self):
        dpp_elem = ET.Element("DynamicParameterClasses")
        ET.SubElement(dpp_elem, "MaximumNumber").text = str(self.max_number)
        for bundle in self.bundles:
            bundle_elem = bundle.to_xml()
            dpp_elem.append(bundle_elem)
        return dpp_elem
