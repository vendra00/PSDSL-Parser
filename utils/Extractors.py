from model.DynamicParameterClass import DynamicParameterClass
from model.PhaseParameter import PhaseParameter
import re

from utils.Converters import convert_parameter_type_to_name
from utils.Utils import create_dynamic_class_name


def extract_section(content, section_name):
    # Adjust the regular expression to handle nested structures
    section_pattern = re.compile(rf"{section_name}\s*{{(.*?^\}})", re.DOTALL | re.MULTILINE)
    match = section_pattern.search(content)
    return match.group(1).strip() if match else ""


def extract_phase_parameters(content):
    parameters = []
    sort_index = 1

    for line in content.split('\n'):
        line = line.strip()
        if "PhaseParameter {" in line:
            # print(f"Processing line: {line}")

            parts = line.split()
            usage_identifier, parameter_type = None, None

            for i, part in enumerate(parts):
                if part == 'usageIdentifier:':
                    usage_identifier = parts[i + 1].strip('"')
                elif part == 'parameterType:':
                    parameter_type = parts[i + 1].strip('"')

            if usage_identifier and parameter_type:
                # Transform parameterType into the desired name format
                name = convert_parameter_type_to_name(parameter_type)
                parameter = PhaseParameter(name, usage_identifier, parameter_type, sort_index)
                parameters.append(parameter)
                sort_index += 1

    return parameters


def extract_dynamic_parameter_classes(content):
    dynamic_classes = []
    dynamic_phase_parameters_section = extract_section(content, 'DynamicPhaseParameters')

    if dynamic_phase_parameters_section:
        max_number_match = re.search(r"maximumNumber:\s*(\d+)", dynamic_phase_parameters_section)
        max_number = int(max_number_match.group(1)) if max_number_match else None

        dynamic_bundles = re.findall(r"DynamicPhaseBundle\s*{([^}]*)}", dynamic_phase_parameters_section, re.DOTALL)
        for bundle in dynamic_bundles:
            parameters = extract_parameters_from_bundle(bundle)

            # Assuming the first parameter in each bundle is used to name the dynamic class
            if parameters:
                name = create_dynamic_class_name(parameters[0]['parameterType'])
                usage_identifier = parameters[0]['usageIdentifier']
                dynamic_class = DynamicParameterClass(name, usage_identifier, max_number, parameters)
                dynamic_classes.append(dynamic_class)

    # Debug output to check the data of each DynamicParameterClass object
    for dynamic_class in dynamic_classes:
        print(
            f"DynamicParameterClass(Name: {dynamic_class.name}, UsageIdentifier: {dynamic_class.usage_identifier}, "
            f"MaxNumber: {dynamic_class.max_number}, DependentClasses: ["
            f"{', '.join(str(dep) for dep in dynamic_class.dependent_classes)}])")
    return dynamic_classes


def extract_parameters_from_bundle(bundle_content):
    parameters = []
    parameter_matches = re.findall(r"Parameter\s*{([^}]*)}", bundle_content, re.DOTALL)
    for param_content in parameter_matches:
        usage_identifier_match = re.search(r"usageIdentifier:\s*\"(.*?)\"", param_content)
        parameter_type_match = re.search(r"parameterType:\s*\"(.*?)\"", param_content)
        if usage_identifier_match and parameter_type_match:
            usage_identifier = usage_identifier_match.group(1)
            parameter_type = parameter_type_match.group(1)
            parameter = PhaseParameter(usage_identifier, usage_identifier, parameter_type)
            parameters.append(parameter)
    return parameters
