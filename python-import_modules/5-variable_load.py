#!/usr/bin/python3
import importlib.util


def import_variable(module_name, variable_name):
    spec = importlib.util.spec_from_file_location(module_name, "variable_load_5.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if hasattr(module, variable_name):
        value = getattr(module, variable_name)
        print(value)
    else:
        print(f"Variable '{variable_name}' not found in {module_name}.py")

if __name__ == "__main__":
    import_variable("variable_load_5", "a")
