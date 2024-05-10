#!/usr/bin/python3
import sys


def add_args(args):
    result = sum(int(arg) for arg in args)
    print(result)


if __name__ == "__main__":
    add_args(sys.argv[1:])
