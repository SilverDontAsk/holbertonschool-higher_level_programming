#!/usr/bin/python3
import sys
ascii_alphabet = ''
for i in range(97, 123):
    if chr(i) not in ['q', 'e']:
        ascii_alphabet += chr(i)

print("{}".format(ascii_alphabet), end='')
