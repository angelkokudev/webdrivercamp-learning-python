#!/usr/bin/python3
import random
random_num = random.randint(-10000, 10000)
last_digit= int(str(random_num)[-1])
if last_digit == 0:
	print(f"{random_num} - the last digit {last_digit} is zero")
elif last_digit % 2 == 0:
	print(f"{random_num} - the last digit {last_digit} is even")
else:
	print(f"{random_num} - the last digit {last_digit} is odd")
