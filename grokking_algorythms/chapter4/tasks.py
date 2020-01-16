def sum(arr):
    res = 0
    for x in arr:
        res += x

    return res


def sum_recursion(arr):
    if arr == []:
        return 0

    return arr[0] + sum_recursion(arr[1:])


def counter_recursion(arr):
    if arr == []:
        return 0

    return 1 + counter_recursion(arr[1:])

def max_recursion(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]

    sub_max = max_recursion(arr[1:])

    return arr[0] if arr[0] > sub_max else sub_max


def binary_search(arr, low, high, item):
    if high >= low:
        mid = (low + high) // 2
        if arr[mid] == item:
            return mid

    if arr[mid] > item:
        return binary_search(arr, low,  mid - 1, item)
    else:
        return binary_search(arr, mid + 1, high, item)

    return None


sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l = [1, 2, 3, 4, 1, 6, 9, 2]

print(binary_search(sorted_list, 0, len(sorted_list) - 1, 1))