import json
import treelib

def generate_class_def(class_name, attrs, superclass_name=None):
    constructor_args = []
    constructor_def = ""
    has_attributes = False

    class_name = class_name.replace(' ', '_').replace('é','e').replace('è','e').replace('ê','e').replace('à','a')
    class_template = f"class {class_name}"

    if superclass_name:
        superclass_name = superclass_name.replace(' ', '_').replace('é','e').replace('è','e').replace('ê','e').replace('à','a')
        class_template += f"({superclass_name})"
    class_template += ":\n"

    for attr_name, attr_type in attrs.items():
        if attr_name != "subclasses":
            has_attributes = True
            constructor_args.append(attr_name)
            constructor_def += f"\n        self.{attr_name} = {attr_name}"
    if has_attributes:
        constructor_template = f"    def __init__(self, {', '.join(constructor_args)}):{constructor_def}"
    else:
        constructor_template = "    pass"
    return class_template + constructor_template + "\n\n"

def generate_class_hierarchy(json_data, superclass_name=None):
    class_defs = ""

    for class_name, class_attrs in json_data.items():

        class_def = generate_class_def(class_name, class_attrs, superclass_name)
        class_defs += class_def

        if "subclasses" in class_attrs:
            subclass_defs = generate_class_hierarchy(class_attrs["subclasses"], class_name)
            class_defs += subclass_defs

    return class_defs


def print_class_hierarchy(json_data):
    tree = treelib.Tree()

    root_node_id = "root"
    root_node_name = "Classes Hierarchy"
    tree.create_node(root_node_name, root_node_id)

    def traverse_json_data(data, parent_node_id):
        for class_name, class_attrs in data.items():
            class_name = class_name.replace(' ', '_').replace('é','e').replace('è','e').replace('ê','e').replace('à','a')
            class_node_id = class_name
            class_node_name = class_name

            # Add the class node to the tree
            tree.create_node(class_node_name, class_node_id, parent=parent_node_id)

            # Traverse any subclasses
            if "subclasses" in class_attrs:
                traverse_json_data(class_attrs["subclasses"], class_node_id)

    traverse_json_data(json_data, root_node_id)

    # Print the tree
    tree.show()



json_data = {
    "Biens Consommation": {
        "cost": "",
        "price": "",
        "profit": "",
        "subclasses": {
            "Articles Menagers": {
                "subclasses": {
                    "Meubles":{
                        "materiaux": "",
                        "coleur": "",
                        "dimension": "",
                        "subclasses": {
                            "Canapes":{},
                            "Chaises":{ },
                            "Tables": {}
                        }
                    },
                    "Appareils Electromenagers": {
                        "marque" : "",
                        "capacites": "",
                        "subclasses": {
                            "Refrigerateurs": {
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
                            "Casseroles Poêles": {
                                "diametre" : ""
                            },
                            "Batteries Cuisine": {
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
                            "Hauts": {},
                            "Pantalons": {},
                            "Robes" : {}
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

class_hierarchy_code = generate_class_hierarchy(json_data)
print(class_hierarchy_code)


print("====================\n")
print_class_hierarchy(json_data)

