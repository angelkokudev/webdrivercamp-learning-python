#!/usr/bin/python3


def calc_weight(list_=[]):
    calc_weight = sum(x * y for x, y in list_)
    number_weight = sum(y for x, y in list_)
    weight_average = calc_weight / number_weight
    return weight_average


if __name__ == "__main__":
    list_ = [(3, 2), (5, 9), (7, 7)]
    # = ((3 * 2) + (5 * 9) + (7 * 7)) / (2 + 9 + 7)
    result = calc_weight(list_)
    print(f"Weight: {result:0.2f}")
