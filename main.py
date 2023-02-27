import json 

class Product:
    def __init__(self, category, subcategory_1, subcategory_2):
        self.category = category
        self.subcategory_1 = subcategory_1
        self.subcategory_2 = subcategory_2

class TreeNode:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)
        child_node.parent = self

def add_json_to_tree(json_data, parent_node):
    for key, value in json_data.items():
        node = TreeNode(key)
        parent_node.add_child(node)
        if isinstance(value, dict):
            add_json_to_tree(value, node)

def create_product_classes(node, level=1):
    if len(node.children) == 0:  # Create a Product class for terminal nodes
        category = node.parent.parent.parent.data
        subcategory_1 = node.parent.parent.data
        subcategory_2 = node.parent.data
        class_name = node.data
        globals()[class_name] = type(class_name, (Product,), {})
        globals()[class_name].category = category
        globals()[class_name].subcategory_1 = subcategory_1
        globals()[class_name].subcategory_2 = subcategory_2
    else:
        for child in node.children:
            create_product_classes(child, level + 1)

json_data = """
{
  "Biens Consommation": {
    "Articles Menagers": {
      "Meubles": {
        "Canapes": {},
        "Chaises": {},
        "Tables": {}
      },
      "Appareils Electromenagers": {
        "Refrigerateurs": {},
        "Lave-vaisselle": {},
        "Lave-linge": {}
      },
      "Ustensiles Cuisine": {
        "Casseroles Poêles": {},
        "Batteries Cuisine": {},
        "Ustensiles Cuisine": {}
      }
    },
    "Vêtements Accessoires": {
      "Vêtements": {
        "Hauts": {},
        "Pantalons": {},
        "Robes": {}
      },
      "Chaussures": {
        "Baskets": {},
        "Sandales": {},
        "Chaussures habillees": {}
      }
    }
  }
}
"""

def print_tree(node, level=0):
    print("  " * level + str(level) + "-" + str(node.data))
    for child in node.children:
        print_tree(child, level + 1)

import re
import pprint as pp
from unidecode import unidecode

# Define a regular expression pattern to match quoted substrings
pattern = r'"[^"]*"'

json_data_unicode=unidecode(json_data) 
json_data_trim = re.sub(pattern, lambda m: m.group(0).replace(" ", "_").replace("-", "_"), json_data_unicode)
#pp.pprint(json_data, compact=True)
#pp.pprint(json_data_trim)
data = json.loads(json_data_trim)
root_node= TreeNode("root")
add_json_to_tree(data, root_node)


def create_classes(node, parent=None):
    if parent is None:
        class_str = ''
    elif parent.data == 'root':
        class_str = f"class {node.data}():\n"
    else:
        class_str = f"\nclass {node.data}({parent.data}):\n"
    child_class_strs = []
    
    for child_node in node.children:
        child_class_str = create_classes(child_node, parent=node)
        child_class_strs.append(child_class_str)
    
    if child_class_strs:
        child_classes_str = "\n".join(child_class_strs)
        class_str += f"\tpass\n{child_classes_str}"
    
    else:
            class_str += "\tpass\n"
    
    return class_str

class_hierarchy = create_classes(root_node)

#dirty hack to remove extra "pass" entry
index = class_hierarchy.find("class")
if index != -1:
    class_hierarchy = class_hierarchy[index:]#.replace('\n\n','\n')

#class_hierarchy = [line for line in class_hierarchy.split('\n') if line.strip() != ""]

#string_without_empty_lines = ""
#for line in class_hierarchy:
#     string_without_empty_lines += line + "\n"
#class_hierarchy = string_without_empty_lines

def print_parents(cls):
    print("Parents of {}:".format(cls.__name__))
    for parent in cls.__bases__:
        print("  ", parent.__name__)
    print()

print("====================")
print(class_hierarchy)
print_tree(root_node)
