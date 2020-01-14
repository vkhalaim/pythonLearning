def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(0, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index


def selection_sort(arr):
    sorted_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        sorted_arr.append(arr.pop(smallest))

    return sorted_arr

arr2 = [1, 4, 5, 2, 2, 4, 5, 6, 0]
new_arr = selection_sort(arr2)
print(new_arr)