#!/usr/bin/python3


def print_list_integer(my_list=[]):
    formatted_str = "\n".join("{:d}".format(num) for num in my_list)
    print(formatted_str)
