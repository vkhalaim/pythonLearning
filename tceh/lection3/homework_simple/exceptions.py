# num = int(input())
#
# if num > 10:
#     raise IndexError('It\'s too big')
# elif num < 0:
#     raise TypeError('Less than zero!')
# elif num % 2 == 0:
#     raise ValueError('Is even!')
#

l = [1, 2, 3, 4, 5, 6, 7, 8]

inp = int(input('Which index do you want?'))

try:
    print(l[inp])
except IndexError:
    print('Out of boundary!')

