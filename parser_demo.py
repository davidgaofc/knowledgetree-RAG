import re
myresponse = "blah blah blah blah Continue - True; Node - node_name; Levels - number_of_levels;"
# myresponse = "Response - [(X1, edge_name), (X2, edge_name), ...];"
# myresponse = "Concepts - [concept1, concept2, ...];"

temp = myresponse.split("Concepts - ")

def parse_string(input_string):
    # Create a dictionary to hold the parsed data
    parsed_data = {}

    # Pattern to match key-value pairs
    pairs_pattern = r'(\w+)\s*-\s*([^;]+);'
    # Pattern to match lists inside brackets (including tuples)
    list_pattern = r'\[(.*?)\]'

    # Find all key-value pairs
    pairs = re.findall(pairs_pattern, input_string)

    # Process each pair
    for key, value in pairs:
        # Trim whitespace and check if value is a list or tuple
        value = value.strip()
        if re.match(list_pattern, value):
            # Extract list or tuple items
            list_contents = re.search(list_pattern, value).group(1)
            if '(' in list_contents:
                # Handle tuples within the list
                items = re.findall(r'\((.*?)\)', list_contents)
                parsed_data[key] = [tuple(item.split(',')) for item in items]
            else:
                # Handle simple lists
                items = list_contents.split(',')
                parsed_data[key] = [item.strip() for item in items]
        else:
            # Handle simple values (booleans, numbers, strings)
            if value.lower() in ['true', 'false']:
                parsed_data[key] = value.lower() == 'true'
            elif value.isdigit():
                parsed_data[key] = int(value)
            else:
                parsed_data[key] = value

    return parsed_data

print(parse_string(myresponse))