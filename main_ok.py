#########

import json
import treelib

def generate_class_def(class_name: str, attrs:dict, superclass_name:str,superclass_args:list):    
    
    if superclass_args is None:
        superclass_args = []
    constructor_args = []
    constructor_def = ""
    has_attributes = False

    class_template = f"class {class_name}"

    if superclass_name:        
        class_template += f"({superclass_name})"
    
    class_template += ":\n"

    for attr_name, attr_val in attrs.items():
        if attr_name != "subclasses":
            has_attributes = True
            constructor_args.append(attr_name)
            constructor_def += f"\n\t\tself.{attr_name} = {attr_name}"
    
    if has_attributes:
        constructor_template = f"\tdef __init__(self, {', '.join(constructor_args+superclass_args)}):"

        if len(superclass_args)>0:
            constructor_template +=f"\n\t\tsuper().__init__({', '.join(superclass_args)})"

        constructor_template +=constructor_def
    
    else:
        if len(superclass_args)>0:
            constructor_template = f"\tdef __init__(self, {', '.join(superclass_args)}):"
            constructor_template +=f"\n\t\tsuper().__init__({', '.join(superclass_args)})"
      
        else:    
            constructor_template = "\tpass"

    return class_template + constructor_template + "\n\n"

#########

def generate_class_hierarchy(json_dict :dict, superclass_name:str=None,superclass_args:list=[]):
    class_defs = ""

    for class_name, class_attrs in json_dict.items():

        class_def = generate_class_def(class_name, class_attrs, superclass_name,superclass_args)
        class_defs += class_def

        if "subclasses" in class_attrs:
            super_attr = (list(class_attrs.keys())+superclass_args)
            super_attr.remove("subclasses")
            subclass_defs = generate_class_hierarchy(class_attrs["subclasses"], class_name, super_attr)
            class_defs += subclass_defs

    return class_defs

#########

def generate_tree_hierarchy(json_dict):
    # define the tree
    global tree 
    tree = treelib.Tree()

    # define the root node
    root_node_id = "root"
    root_node_name = "Product Classes Hierarchy"
    tree.create_node(root_node_name, root_node_id)

    #traverse json data and creathe other node
    recusive_tree_from_json(json_dict, root_node_id)

    return tree

#########

# Retrieves class names and attributes from json file recursively and stores them in a Treelib
def recusive_tree_from_json(json_dict, parent_node_id):
    for class_name, class_attrs in json_dict.items():            
            class_node_id = class_name
            class_node_name = class_name

            # Add the class node to the tree
            tree.create_node(class_node_name, class_node_id, parent=parent_node_id)

            # Traverse any subclasses
            if "subclasses" in class_attrs:
                recusive_tree_from_json(class_attrs["subclasses"], class_node_id)

#########
                             
json_data = """
{
    "Biens Consommation": {
        "cost": "",
        "price": "",
        "marque": "",
        "subclasses": {
            "Articles Menagers": {
                "subclasses": {
                    "Meubles":{
                        "materiaux": "",
                        "couleur": "",
                        "dimension": "",
                        "subclasses": {
                            "Canapes":{},
                            "Chaise":{},
                            "Table": {}
                        }
                    },
                    "Appareils Electromenagers": {
                        "capacites": "",
                        "subclasses": {
                            "Refrigerateur": {
                                "efficacite" : ""
                            },
                            "Lave-vaisselle": {
                                "programme" : ""
                            },
                            "Lave-linge": {
                                "programme" : ""
                            }
                        }
                    },
                    "Ustensiles Cuisine": {
                        "materiaux" : "",
                        "subclasses": {
                            "Casserole Poêle": {
                                "diametre" : ""
                            },
                            "Batterie Cuisine": {
                                "nombre_pieces" : ""
                            }
                        }
                    }
                }
            },
            "Vêtements Accessoires": {
                "subclasses": {
                    "Vêtements": {
                        "taille" : "",
                        "couleur" : "",
                        "matiere" : "",
                        "subclasses": {
                            "Haut": {},
                            "Pantalon": {},
                            "Robe" : {}
                        }
                    },
                    "Accessoires": {
                        "couleur" : ""
                    },
                    "Chaussures": {
                        "pointure" : ""
                    }
                }
            }
        }
    }
}
"""

#########

def sep():
    print("====================\n")

#########

def trimspaces(input):
    # Define a regular expression pattern to match quoted substrings
    pattern = r'"[^"]*"'
    # Replace spaces and hyphens with underscore
    return re.sub(pattern, lambda m: m.group(0).replace(" ", "_").replace("-", "_"), input)

#########

from unidecode import unidecode
import re

json_data = trimspaces(str(unidecode(json_data)))

json_dict = json.loads(json_data)

sep()

class_hierarchy_code = generate_class_hierarchy(json_dict)

sep()

#########

def write_content(content,filename):
    with open(filename, "w") as f:
        f.write(content)

write_content(class_hierarchy_code, "product_classes.py")

#########

print(class_hierarchy_code)

#########

generate_tree_hierarchy(json_dict).show()
