#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for c in '.?:':
        text = text.replace(c, f'{c}\n\n')

    lines = text.split('\n')
    for i, line in enumerate(lines):
        if line:
            print(line.strip())
            if i < len(lines) - 1:
                print()
