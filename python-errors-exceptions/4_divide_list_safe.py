#!/usr/bin/python3


def divide_list_safe(list_1, list_2, list_len):
    result = []
    try:
        for item in range(list_len):
            if item >= len(list_1) or item >= len(list_2):
                print("out of range")
                result.append(0)
            else:
                item_1 = list_1[item]
                item_2 = list_2[item]
                if not isinstance(item_1, (int, float)):
                    print("wrong type")
                    result.append(0)
                elif not isinstance(item_2, (int, float)):
                    print("wrong type")
                    result.append(0)
                elif list_2[item] == 0:
                    print("division by 0")
                    result.append(0)
                else:
                    result.append(list_1[item] / list_2[item])
    except Exception:
        pass
    finally:
        return result


if __name__ == "__main__":
    list_1 = [9, 2, 6]
    list_2 = [3, 2, 2]
    res = divide_list_safe(list_1, list_2, max(len(list_1), len(list_2)))
    print(res)
    print(10*"_")
    print()

    list_1 = [9, 2, 6, 10]
    list_2 = ["one", 0, 1, 2, 7]
    res = divide_list_safe(list_1, list_2, max(len(list_1), len(list_2)))
    print(res)
