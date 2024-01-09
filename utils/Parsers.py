from model.DynamicPhaseBundle import DynamicPhaseBundle
from model.DynamicPhaseParameters import DynamicPhaseParameters
from model.PhaseParameter import PhaseParameter
from utils.Utils import create_dynamic_class_name
import re


def parse_phase_description(content):
    # Extract and parse the data as per the schema
    # This is a simplified example; adjust based on your specific schema
    properties = dict(re.findall(r"(\w+):\s*(.+)", content))
    return properties


def parse_phase_content(phase_content):
    # Extract key-value pairs from the phase content
    properties = dict(re.findall(r"(\w+):\s*(.+)", phase_content))
    return properties


def parse_dynamic_phase_parameters(content):
    # Extract the maximum number and the bundles
    max_number_match = re.search(r"maximumNumber:\s*(\d+)", content)
    max_number = int(max_number_match.group(1)) if max_number_match else None

    bundle_matches = re.findall(r"DynamicPhaseBundle\s*{([^}]*)}", content, re.DOTALL)
    bundles = [parse_dynamic_phase_bundle(match) for match in bundle_matches]

    return DynamicPhaseParameters(max_number, bundles)


def parse_dynamic_phase_bundle(bundle_content):
    # Extract parameters from each bundle
    param_matches = re.findall(r"Parameter\s*{([^}]*)}", bundle_content)
    parameters = [parse_phase_parameter(match) for match in param_matches]

    return DynamicPhaseBundle(parameters)


def parse_phase_parameter(param_content):
    # Extract details for each parameter
    usage_identifier_match = re.search(r"usageIdentifier:\s*\"([^\"]+)\"", param_content)
    parameter_type_match = re.search(r"parameterType:\s*\"([^\"]+)\"", param_content)

    if usage_identifier_match and parameter_type_match:
        usage_identifier = usage_identifier_match.group(1)
        parameter_type = parameter_type_match.group(1)
        name = create_dynamic_class_name(parameter_type)  # Assumes this function is defined
        return PhaseParameter(name, usage_identifier, parameter_type)
    return None
