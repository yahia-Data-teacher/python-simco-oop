# coding: utf-8
import re
import json
from unidecode import *

def write_content(content,filename):
        with open(filename, "w", encoding='utf-8') as f:
            f.write(content)
            

def read_json(filename: str = "json_data.json"):
    
    return json.load(open(filename, "rb"))
            
            
def sep():
    print("====================\n")
    
    
def trimspaces(data):
    # Define a regular expression pattern to match quoted substrings
    pattern = r'"[^"]*"'
    # Replace spaces and hyphens with underscore
    #return re.sub(pattern, lambda m: m.group(0).replace(" ", "_").replace("-", "_"), str(unidecode(json.dumps(data))))
    data_s=json.dumps(data)
    return re.sub(pattern, lambda m: m.group(0).replace(" ", "_").replace("-", "_"), data_s)