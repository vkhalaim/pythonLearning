arr = [3, 2, 4, 1, 5, 8]
# trivial solution
arr.sort()

print(arr)

# bubble sort
arr = [3, 2, 4, 1, 5, 8]
i = 0
j = 0

while i < len(arr):
    j = 0
    while j < len(arr):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    i += 1

print(arr)
