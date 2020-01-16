def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i < pivot]
        greater = [i for i in arr[1:] if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)


arr = [1, 5, 2, 8, 11, 44, 11, 2222, 87, 1, 5, 2, 4, 5, 6, 9]

print(quick_sort(arr))