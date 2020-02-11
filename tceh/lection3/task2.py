l = [1, 2, 4, 5, 9, 2, 1, 5, 6]

index = eval(input("Enter array index: "))

try:
    print(l[index])
    print('Everything is fine!')
except IndexError as e:
    print('Sorry! ' + str(e))