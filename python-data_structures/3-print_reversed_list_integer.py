#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    reversed_str = "\n".join("{:d}".format(num) for num in reversed(my_list))
    print(reversed_str)
