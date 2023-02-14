import ast
import sys

INFERENCE_REQUEST = "InferenceRequest"
MODEL_NAME_ARG = "model_name"

class VariableFinder(ast.NodeVisitor):
    def __init__(self, varname):
        self.varname = varname
        self.value = None

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == self.varname:
                value = ast.literal_eval(node.value)
                self.value = value

class AttributeFinder(ast.NodeVisitor):
    def __init__(self, attrname):
        self.attrname = attrname
        self.value = None

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Attribute) and target.attr == self.attrname:
                value = ast.literal_eval(node.value)
                self.value = value



class ModelNameFinder(ast.NodeVisitor):
    model_names = []

    def visit_Call(self, node):

        if isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name) and node.func.attr == INFERENCE_REQUEST:
            for kw in node.keywords:
                if kw.arg == MODEL_NAME_ARG:
                    if isinstance(kw.value, ast.Str):
                        # Assigned a string directly
                        model_name = kw.value.value
                    elif isinstance(kw.value, ast.Name):
                        # Assigned a variable, need to evaluate
                        model_name = eval_name(kw.value.id)
                    elif isinstance(kw.value, ast.Attribute):
                        # Assigned a class attribute, need to evaluate
                        model_name = eval_attribute(kw.value.attr)
                    else: 
                        print("Unable to parse model name: Unknown type")
                        sys.exit(1)

                    if model_name and model_name not in self.model_names: 
                        self.model_names.append(model_name)

        self.generic_visit(node)

def find_model_name():
    with open(filename, 'r') as f:
        source = f.read()
    tree = ast.parse(source)
    finder = ModelNameFinder()
    finder.visit(tree)
    return finder.model_names

def eval_name(var_name):
    with open(filename, 'r') as f:
        source = f.read()
    tree = ast.parse(source)
    visitor = VariableFinder(var_name)
    visitor.visit(tree)
    return visitor.value

def eval_attribute(var_name):
    with open(filename, 'r') as f:
        source = f.read()
    tree = ast.parse(source)
    visitor = AttributeFinder(var_name)
    visitor.visit(tree)
    return visitor.value

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 model_parser.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    print(find_model_name())
