from utils.Extractors import extract_section, extract_phase_parameters
from utils.Parsers import parse_phase_content, parse_dynamic_phase_parameters
from utils.Utils import read_phase_content
from xml_generators.PhaseDescription import create_phase_description_xml


def main():
    phase_content = read_phase_content('files/phase.psdsl')

    # Extract and process the Phase section
    description_content = extract_section(phase_content, 'Phase')
    properties = parse_phase_content(description_content)
    phase_parameters = extract_phase_parameters(description_content)

    # Extract and process the DynamicPhaseParameters section
    dynamic_phase_parameters_content = extract_section(phase_content, 'DynamicPhaseParameters')
    dynamic_phase_parameters = parse_dynamic_phase_parameters(dynamic_phase_parameters_content)

    # Parse and generate phaseDescription.xml
    description_xml = create_phase_description_xml(properties, phase_parameters, dynamic_phase_parameters.bundles)
    with open('phaseDescription.xml', 'w') as file:
        file.write(description_xml)


if __name__ == "__main__":
    main()
