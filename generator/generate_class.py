def _superclass_name(superclass_name,class_template):#
    """

    :param superclass_name:
    :param class_template:
    :return:
    """
    if superclass_name:
        class_template += f"({superclass_name})"
        return class_template
    else :
        return class_template

def _subclasses(attrs={},constructor_args=[], constructor_def=None):
    for attr_name in attrs.keys():
        if attr_name != "subclasses":
            has_attributes = True
            constructor_args.append(attr_name)
            constructor_def += f"\n\t\tself.{attr_name} = {attr_name}"

    return constructor_args,constructor_def

def _has_attributes(has_attributes=False, superclass_args=None, constructor_args=[], constructor_def=''):
    if has_attributes:
        constructor_template = f"\tdef __init__(self, {', '.join(constructor_args + superclass_args)}):"

        if len(superclass_args) > 0:
            constructor_template += f"\n\t\tsuper().__init__({', '.join(superclass_args)})"

        constructor_template += constructor_def
    else:
        if len(superclass_args) > 0:
            constructor_template = f"\tdef __init__(self, {', '.join(superclass_args)}):"
            constructor_template += f"\n\t\tsuper().__init__({', '.join(superclass_args)})"

        else:
            constructor_template = "\tpass"
    return constructor_template
def generate_class_def(class_name: str, attrs: dict, superclass_name: str, superclass_args: list = []):

    constructor_args = []
    constructor_def = ""
    has_attributes = False

    class_template = f"class {class_name}"
    
    # need more details
    class_template =_superclass_name(superclass_name,class_template)

    class_template += ":\n"

    constructor_def, constructor_args=_subclasses(attrs,constructor_args,constructor_def)

    constructor_template=_has_attributes(has_attributes, superclass_args, constructor_args, constructor_def)

    return class_template + constructor_template + "\n\n"

"""
class Generator:
    def __init__(self,class_name: str, attrs: dict, superclass_name: str, superclass_args: list):
        self.class_name=class_name
        self.attrs=attrs
        self.superclass_name=superclass_name
        self.superclass_args=superclass_args

    def superclass_name(self) -> str:
        if self.superclass_name:
            self.class_template += f"({self.superclass_name})"
            return self.class_template
"""
