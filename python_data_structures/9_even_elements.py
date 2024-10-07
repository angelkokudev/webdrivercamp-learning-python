#!/usr/bin/python3
my_list = [5, 4, 3, 2, 1]
value = []
for number in my_list:
	if number %2 == 0: 
		value.append(True)
	else:
		value.append(False)
value = tuple(value)
print(my_list)
print(value)
