arr = ['to-delete', 2, 1, 'to-delete', 5, 2, 1, 'to-delete', 'df']
# list before deleting elements
print(arr)

for i in arr:
    if i == 'to-delete':
        arr.remove(i)
# list after deleting elements
print(arr)
