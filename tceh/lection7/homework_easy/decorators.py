import time


def decline_wrapper(func):
    def inner(*args, **kwargs):
        print(func.__name__ + " is cancelled!")

    return inner


def calculate_time_wrapper(func):
    def inner():
        t1 = time.time()
        func()
        t2 = time.time()

        print('Function was working for ' + str(t2 - t1) + ' seconds!')

    return  inner


@decline_wrapper
def say_hi():
    print("Hi")


@decline_wrapper
def calculate_to_console(x, y):
    return x + y


say_hi()
calculate_to_console(1, 2)


@calculate_time_wrapper
def slow():
    res = []
    for i in range(10000000):
        res.append(i)

    return res


@calculate_time_wrapper
def fast():
    return [i for i in range(10000000)]

slow()
fast()


def count_wrapper(func):
    def inner(*args, **kwargs):
        inner.calls += 1
        func()

    inner.calls = 0    
    return inner



@count_wrapper
def do_nothing():
    pass


@count_wrapper
def do_nothing_2():
    pass


do_nothing()
do_nothing()
do_nothing()
do_nothing()
do_nothing()
print(do_nothing.calls)

do_nothing_2()
print(do_nothing_2.calls)


def logger(func):
    print('Decorator is created')

    def inner(*args, **kwargs):
        print('function is started!')
        print(func(*args, **kwargs))
        print('function is executed')

    return inner


@logger
def calculate_power(num, power):
    return num ** power


calculate_power(2, 2)


def handle_exception(func):
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(e)

    return inner


@handle_exception
def division(a, b):
    return a / b


division(1, 2)
division(1, 0)
division(1, '0')
