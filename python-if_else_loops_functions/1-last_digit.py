#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERe
i = abs(number) % 10 * (-1 if number < 0 else 1)
if i > 5:
    print(f"Last digit of {number} is {i} and is greater than 5")
elif i == 0:
    print(f"Last digit of {number} is {i} and is 0")
else:
    print(f"Last digit of {number} is {i} and is less than 6 and not 0")
