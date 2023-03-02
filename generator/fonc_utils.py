import re
import json

def write_content(content,filename):
        with open(filename, "w") as f:
            f.write(content)
            

def read_json(filename: str = "json_data.json"):
    return json.load(open(filename, "r", encoding='utf-8'))
            
            
def sep():
    print("====================\n")
    
    
def trimspaces(input):
    # Define a regular expression pattern to match quoted substrings
    pattern = r'"[^"]*"'
    # Replace spaces and hyphens with underscore
    return re.sub(pattern, lambda m: m.group(0).replace(" ", "_").replace("-", "_"), json.dumps(input))