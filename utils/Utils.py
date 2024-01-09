import xml.etree.ElementTree as ET


def create_dynamic_class_name(parameter_type):
    # Split the parameter type into parts
    parts = parameter_type.split('_')
    if len(parts) < 3:
        # If the parameter type does not have enough parts, return it as-is
        return parameter_type

    # Extract the base name, customer abbreviation, and version
    base_name = parts[0]
    customer_abbr = parts[1]
    version = parts[2]

    # Format the base name (e.g., "DecimalPropertyDefinition" -> "Decimal")
    formatted_name = base_name
    # Add specific formatting rules as needed, for example:
    # if base_name.endswith("PropertyDefinition"):
    #     formatted_name = base_name.replace("PropertyDefinition", "")

    # Format the version (e.g., "0100" -> "1.0")
    version_number = float(version) / 100 if version.isdigit() else version

    # Combine the parts into the final name
    final_name = f"{formatted_name} ({customer_abbr}) [{version_number}]"
    return final_name


def string_to_boolean(value):
    # Assuming the value is a string like 'true' or 'false'
    return "true" if value.strip().lower() == "true" else "false"


def create_xml_element(tag, text=None, attrib=None):
    elem = ET.Element(tag)
    if text:
        elem.text = text
    if attrib:
        for key, value in attrib.items():
            elem.set(key, value)
    return elem


def read_phase_content(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content
