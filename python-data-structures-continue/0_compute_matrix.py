#!/usr/bin/python3

def compute_matrix(matrix=[]):
    square_matrix = list(map(square_row, matrix))
    return square_matrix

def square_value(x):
    return x ** 2

def square_row(row):
    square_row = list(map(square_value, row))    
    return square_row

if __name__ == "__main__":
    matrix = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]
    print(f"Original: {matrix}")
    print(f"Modified: {compute_matrix(matrix)}")

