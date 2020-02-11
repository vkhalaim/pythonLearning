
def max_of_three(x, y, c):
    min_num = min(x, y, c)

    l = [x, y, c]
    l.pop(l.index(min_num))

    return l

print(max_of_three(5, 6, 7))