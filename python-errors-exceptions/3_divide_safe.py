#!/usr/bin/python3


def divide_safe(a, b):
    result = None
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return None
    finally:
        print(f"Result: {result}")


if __name__ == "__main__":
    a = 9
    b = 3
    result = divide_safe(a, b)
    print(f"{a} / {b} = {result}")

    b = 0
    result = divide_safe(a, b)
    print(f"{a} / {b} = {result}")
