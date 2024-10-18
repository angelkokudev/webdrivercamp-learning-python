#!/usr/bin/python3


def max_value(d):
    if d:
        max_value = int()
        max_key = None
        for key, value in d.items():
            if value > max_value:
                max_value = value
                max_key = key
        return max_key
    else:
        return None


if __name__ == "__main__":
    dict_ = {'Apple': 13, 'Pear': 1, 'Plum': 20, 'Grape': 10}
    max_key = max_value(dict_)
    print(f"Max number - {max_key}")

    max_key = max_value(None)
    print(f"Max number - {max_key}")
