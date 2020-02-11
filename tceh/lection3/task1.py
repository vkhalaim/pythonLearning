inp = eval(input('x: '))

try:
    if inp > 10:
        raise IndexError('Too large!')
    if inp % 2 == 0 and inp != 0:
        raise ValueError('Even number!')
    if inp == 0:
        raise TypeError('Zero!')
except (IndexError, ValueError, TypeError) as e:
    print(e)
finally:
    print('Well done!')
    
