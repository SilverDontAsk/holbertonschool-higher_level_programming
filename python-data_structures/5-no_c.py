#!/usr/bin/python3


def no_c(my_string):
    rem_char = "cC"
    mod_str = ""
    for char in my_string:
        if char not in rem_char:
            mod_str += char
    return mod_str
