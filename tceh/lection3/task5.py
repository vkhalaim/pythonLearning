def filtering(arr, flag):
    if flag:
        return list(filter(lambda x: x % 2 != 0, arr))

    return list(filter(lambda x: x % 2 == 0, arr))


print(filtering([1, 2, 3, 4, 5, 6, 7, 8], False))
