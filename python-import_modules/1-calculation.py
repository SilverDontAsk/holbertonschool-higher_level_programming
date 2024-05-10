#!/usr/bin/python3
a = 10
b = 5
from calculator_1 import add, sub, mul, div


if __name__ == "__main__":
    sum_result = add(a, b)
    sub_result = sub(a, b)
    mul_result = mul(a, b)
    div_result = div(a, b)
    print("{} + {} = {}".format(a, b, sum_result))
    print("{} - {} = {}".format(a, b, sub_result))
    print("{} * {} = {}".format(a, b, mul_result))
    print("{} / {} = {}".format(a, b, div_result))
