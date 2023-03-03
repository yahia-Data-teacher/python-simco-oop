# coding: utf-8

import json
from unidecode import unidecode

import generator
def main():
    json_data= generator.read_json("json_data.json")
    json_data = generator.trimspaces(json_data)

    json_dict = json.loads(json_data)

    generator.sep()

    class_hierarchy_code = generator.generate_class_hierarchy(json_dict)

    generator.sep()

    #########

    

    generator.write_content(class_hierarchy_code, "product_classes.py")

    #########

    print(class_hierarchy_code)

    #########

    generator.generate_tree_hierarchy(json_dict).show()
                             

if __name__ == '__main__':

    
    main()
