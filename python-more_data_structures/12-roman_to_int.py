#!/usr/bin/python3
def roman_to_int(roman_string):
    deciphered_number = 0
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    if "CM" in roman_string:
        deciphered_number += 900
        roman_string = roman_string.replace("CM", "")
    if "CD" in roman_string:
        deciphered_number += 400
        roman_string = roman_string.replace("CD", "")
    if "XC" in roman_string:
        deciphered_number += 90
        roman_string = roman_string.replace("XC", "")
    if "XL" in roman_string:
        deciphered_number += 40
        roman_string = roman_string.replace("XL", "")
    if "IX" in roman_string:
        deciphered_number += 9
        roman_string = roman_string.replace("IX", "")
    if "IV" in roman_string:
        deciphered_number += 4
        roman_string = roman_string.replace("IV", "")

    for i in roman_string:
        if i == "M":
            deciphered_number += 1000
        elif i == "D":
            deciphered_number += 500
        elif i == "C":
            deciphered_number += 100
        elif i == "L":
            deciphered_number += 50
        elif i == "X":
            deciphered_number += 10
        elif i == "V":
            deciphered_number += 5
        elif i == "I":
            deciphered_number += 1 
    
    return deciphered_number
