import json

class TreeNode:
    def __init__(self, name, children=None):
        self.name = name
        self.children = children or []

    def add_child(self, child_node):
        self.children.append(child_node)

def create_tree_from_json(json_data):
    node = TreeNode(json_data)
    if isinstance(json_data, dict):
        for child_name, child_data in json_data.items():
            child_node = create_tree_from_json(child_data)
            child_node.name = child_name
            node.add_child(child_node)
    elif isinstance(json_data, list):
        for child_data in json_data:
            child_node = create_tree_from_json(child_data)
            node.add_child(child_node)
    return node

json_data = '''{
  "A1": {
    "B1": {
      "C1": {
        "D1": {},
        "D2": {}
      },
      "C2": {
        "D3": {},
        "D4": {}
      }
    },
    "B2": {
      "C2": {
        "D4": {},
        "D5": {}
      }
    }
  },
  "A2": {
    "B3": {
      "C3": {
        "D6": {},
        "D7": {}
      }
    }
  }
}'''

parsed_json_data = json.loads(json_data)
root_node = create_tree_from_json(parsed_json_data)


def create_classes(node, parent=None):
    if parent is None:
        base_class_str = f"class {node.name}:\n"
        class_str = base_class_str
    else:
        class_str = f"class {node.name}({parent.name}):\n"
    child_class_strs = []
    for child_node in node.children:
        child_class_str = create_classes(child_node, parent=node)
        child_class_strs.append(child_class_str)
    if child_class_strs:
        child_classes_str = "\n".join(child_class_strs)
        class_str += f"    pass\n{child_classes_str}"
    else:
        class_str += "    pass"
    return class_str


class_hierarchy = create_classes(root_node)

print(class_hierarchy)
