import xml.etree.ElementTree as ET

from utils.Utils import string_to_boolean


def create_phase_description_xml(properties, phase_parameters, dynamic_parameter_classes):
    # Create XML structure based on phaseDescriptionModelSchema.xml
    # This needs to be customized based on the actual schema
    phase_description_elem = ET.Element("PhaseLibDescription")
    parameter_classes_elem = ET.SubElement(phase_description_elem, "ParameterClasses")

    # Add OutputDir element (empty as per your requirement)
    ET.SubElement(phase_description_elem, "OutputDir")

    # Add phaseName element
    phase_name_elem = ET.SubElement(phase_description_elem, "Name")
    phase_name_elem.text = properties.get("phaseName", "")

    # Add description element
    description_elem = ET.SubElement(phase_description_elem, "Description")
    description_elem.text = properties.get("description", "")

    # Add ShortDescription element if it exists in properties
    if "ShortDescription" in properties:
        short_description_elem = ET.SubElement(phase_description_elem, "ShortDescription")
        short_description_elem.text = properties.get("ShortDescription", "")

    # Add SubroutineName element if it exists in properties
    if "subroutineName" in properties:
        subroutine_name_elem = ET.SubElement(phase_description_elem, "SubroutineName")
        subroutine_name_elem.text = properties.get("subroutineName", "")

    # Add PackageName element
    ET.SubElement(phase_description_elem, "PackageName").text = properties.get("packageName", "")

    # Add PhaseLibBaseName element
    ET.SubElement(phase_description_elem, "PhaseLibBaseName").text = properties.get("phaseLibBaseName", "")

    # Handle boolean values
    ET.SubElement(phase_description_elem, "VisibleInNavigator",
                  attrib={"value": string_to_boolean(properties.get("visibleInNavigator", "false"))})
    ET.SubElement(phase_description_elem, "InternalBuildingBlock",
                  attrib={"value": string_to_boolean(properties.get("internalBuildingBlock", "false"))})

    # Add ReportDesignName element if it exists
    if "reportDesignName" in properties:
        ET.SubElement(phase_description_elem, "ReportDesignName").text = properties.get("reportDesignName", "")

    ET.SubElement(phase_description_elem, "SupportExceptions",
                  attrib={"value": string_to_boolean(properties.get("supportExceptions", "false"))})

    # Function to validate and get integer values
    def get_valid_integer(key, min_val=0, max_val=50):
        try:
            value = int(properties.get(key, "0"))
            return str(max(min_val, min(max_val, value)))
        except ValueError:
            return str(min_val)

    # Add MaterialInputMin element
    ET.SubElement(phase_description_elem, "MaterialInputMin").text = get_valid_integer("materialInputMin")

    # Add MaterialInputMax element
    ET.SubElement(phase_description_elem, "MaterialInputMax").text = get_valid_integer("materialInputMax")

    # Add MaterialOutputMin element
    ET.SubElement(phase_description_elem, "MaterialOutputMin").text = get_valid_integer("materialOutputMin")

    # Add MaterialOutputMax element
    ET.SubElement(phase_description_elem, "MaterialOutputMax").text = get_valid_integer("materialOutputMax")

    # Add EquipmentRequirementMin element if it exists
    if "eqRequirementMin" in properties:
        ET.SubElement(phase_description_elem, "EquipmentRequirementMin").text = get_valid_integer("eqRequirementMin")

    # Add EquipmentRequirementMax element if it exists
    if "eqRequirementMax" in properties:
        ET.SubElement(phase_description_elem, "EquipmentRequirementMax").text = get_valid_integer("eqRequirementMax")

    # ATDefinitionPrefix element
    at_def_prefix = properties.get("atDefinitionPrefix", "").strip('"')
    if 1 <= len(at_def_prefix) <= 3:
        ET.SubElement(phase_description_elem, "ATDefinitionPrefix").text = at_def_prefix

    # UsageContext element
    # Adjust this based on how UsageContext is represented in your file
    usage_context = properties.get("usageContext", "").strip('"')
    if usage_context:
        ET.SubElement(phase_description_elem, "UsageContext").text = usage_context

    # Boolean elements
    ET.SubElement(phase_description_elem, "IsETOTriggerPhase",
                  attrib={"value": string_to_boolean(properties.get("etoTriggerPhase", "false"))})
    ET.SubElement(phase_description_elem, "IsServerRunPhase",
                  attrib={"value": string_to_boolean(properties.get("serverRunPhase", "false"))})
    ET.SubElement(phase_description_elem, "IsPauseAwarePhase",
                  attrib={"value": string_to_boolean(properties.get("pauseAwarePhase", "false"))})

    # Add ParameterClasses element if there are PhaseParameters
    if phase_parameters:
        parameter_classes_elem = ET.SubElement(phase_description_elem, "ParameterClasses")
        for param in phase_parameters:
            parameter_class_elem = param.to_xml()
            parameter_classes_elem.append(parameter_class_elem)

    # Add DynamicParameterClasses to your XML
    dynamic_classes_elem = ET.SubElement(phase_description_elem, "DynamicParameterClasses")
    for dpc in dynamic_parameter_classes:
        dpc_elem = dpc.to_xml()
        dynamic_classes_elem.append(dpc_elem)

    return ET.tostring(phase_description_elem, encoding='unicode', xml_declaration=True)
