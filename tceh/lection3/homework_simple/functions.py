def func1(a, b):
    if a > 0 and b > 0:
        return a + b
    elif a < 0 and b < 0:
        return a - b
    else:
        return 0


print(func1(1, 1))
print(func1(-1, -11))
print(func1(1, -1))


def func2(a, b, c):
    return sorted([a, b, c])[1:]


print(func2(1, 2, 3))
print(func2(111, 22, 3))
print(func2(12, -2, 3))


def func3(l, flag):
    if flag:
        return [num for num in l if num % 2 != 0]

    return [num for num in l if num % 2 == 0]


print(func3([1, 2, 3, 4], True))
print(func3([1, 2, 3, 4], False))


def func4(*args, glue=':'):
    return glue.join([elem for elem in args if len(elem) > 3])



print(func4("dasfs", "aaa22", glue="*"))


def func5(*args):
    return [min(args), max(args)]


print(func5(1, 2, 3, 4, 5))


def func6(string, case=True):
    if case:
        return string.upper()

    return string.lower()


print(func6("asdf"))
print(func6("ASDF", False))
