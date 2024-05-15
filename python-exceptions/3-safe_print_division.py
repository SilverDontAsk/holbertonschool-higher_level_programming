#!/usr/bin/python3
def safe_print_division(a, b):
    dec_result = None
    try:
        result = a / b
        dec_result = "{:.1f}".format(result)
        return dec_result
    except ZeroDivisionError:
        return "None"
    finally:
        if dec_result is not None:
            print("Inside result: {}".format(dec_result))
        else:
            print("Inside result: {}".format(dec_result))
