import re
def convert_parameter_type_to_name(parameter_type):
    parts = parameter_type.split('_')
    if len(parts) >= 3:
        name_parts = parts[:-2]  # Exclude the last two parts for version and category
        category = parts[-2]  # Second last part is the category like RS, RDL, etc.
        version_parts = parts[-1]  # Last part is the version like 0100, 0300, etc.

        # Reformat the version to have a decimal point
        version = f"{int(version_parts[:2])}.{int(version_parts[2:])}"

        # Combine name parts into a single string with spaces
        name = ' '.join(name_parts)

        # Insert space before each uppercase letter in name except the first one
        name = re.sub(r'(?<!^)(?=[A-Z])', ' ', name)

        # Return the formatted name
        return f"{name} ({category}) [{version}]"
    return parameter_type  # Default return if the format doesn't match
