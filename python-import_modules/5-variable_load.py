#!/usr/bin/python3
import importlib.util


file_path = 'variable_load_5.py'

spec = importlib.util.spec_from_file_location('module_name', file_path)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

print(module.a)
