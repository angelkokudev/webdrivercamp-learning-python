#!/usr/bin/python3


def int_print(value):
    try:
        if isinstance(value, int):
            print(f"{value}")
            return True
    except not_int:
        return False


if __name__ == "__main__":
    value = 42
    if not (int_print(value)):
        print(f"{value} is not an integer")

    value = -100
    if not (int_print(value)):
        print(f"{value} is not an integer")

    value = "Webdriver Camp"
    if not (int_print(value)):
        print(f"{value} is not an integer")
