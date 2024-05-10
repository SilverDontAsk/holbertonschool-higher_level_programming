#!/usr/bin/python3
def load_variable():
    file_path = 'variable_load_5.py'
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('a = '):
                value_str = line.split('=')[1].strip()
                value = eval(value_str)
                return value


if __name__ == "__main__":
    value_of_a = load_variable()
    print(value_of_a)
