#!/usr/bin/python3
string = """AbraCadabra
A new string voila!"""
def remove_char(some_string):
	remove_char = ["A", "a"] 
	new_string = ""
	for char in some_string:
        	if char not in remove_char:
            		new_string += char
	return new_string
new_text = remove_char(string)
print(new_text)

