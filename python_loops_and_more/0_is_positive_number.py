#!/usr/bin/python3
import random
random_num = random.randint(-10, 10)
x = random_num
if x < 0:
    print(f"{x} is negative")
elif x > 0:
    print(f"{x} is positive")
elif x == 0:
    print(f"{x} is zero")
