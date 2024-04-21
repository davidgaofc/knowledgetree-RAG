from build.ktree import Tree, TreeNode
from build.query import Query
from template import Template
from build.ktree import Tree, TreeNode
from openai import OpenAI
import re

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="",
)

my_tree = Tree("root")
my_tree.insert_unknowns()

template = Template()

import re


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




def prompt_model(text):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": text}
        ]
    )
    return completion

def update_tree(concept):
    #query with 3 hop limit
    cur_node = "root"
    cur_depth = 3
    for i in range(3):
        # print(template.query_template.format(tree_structure=my_tree.print_tree(cur_node, cur_depth), target=concept))
        query = prompt_model(template.query_template.format(tree_structure=my_tree.print_tree(cur_node, cur_depth), target=concept))
        query = parse_string(query.choices[0].message.content)

        if(query['Continue'] == False):
            break
        else:
            cur_node = query['Node']
            cur_depth = query['Levels']

    place = prompt_model(template.placement_template.format(tree_structure=my_tree.print_tree(cur_node, cur_depth), concepts=concept))
    place = parse_string(place.choices[0].message.content)
    for rep, edge in place['Response']:
        my_tree.swap_unknown_with_node(rep, concept, edge=edge)
        my_tree.insert_unknowns()

    # print("Tree updated with new concept:", concept)
    # print(my_tree.print_tree("root", 5))



def tree_operations(user_input):
    #extract new concepts
    print("Extracting new concepts from user input...")
    temp = prompt_model(template.extraction_template.format(user_query=user_input))
    concepts = parse_string(temp.choices[0].message.content)
    print("concepts:", concepts['Concepts'])

    #add new concepts to tree
    for concept in concepts['Concepts']:
        update_tree(concept)


def process_input(user_input, kg=False):
    #prompt llm with kg prompt or basic
    if(user_input == "tree"):
        return my_tree.print_tree("root", 5)
    elif kg:
        print('begin tree ops ...')
        tree_operations(user_input)

        my_prompt = template.prompt_template.format(tree_structure=my_tree.print_tree("root", 5), question=user_input)
        return prompt_model(my_prompt).choices[0].message.content
    else:
        return prompt_model(user_input).choices[0].message.content


def chat_interface():
    print("Welcome to the chat! Type 'quit' to exit. Type 'tree' to see the current knowledge graph.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'quit':
            print("Exiting chat. Goodbye!")
            break

        response = process_input(user_input, kg=True)
        print(f"ChatBot: {response}")


if __name__ == "__main__":
    chat_interface()