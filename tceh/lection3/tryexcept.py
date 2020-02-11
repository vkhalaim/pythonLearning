try:
    print(1 / 0)
except:
    print("0!!!")

try:
    print(1 / 0)
except Exception:
    print("0!!!")

# Catching specific exceptions

try:
    print(1 / 0)
except ZeroDivisionError:
    print('Exception!')

# Catching exception instance

try:
    print(1 / 0)
except ZeroDivisionError as e:
    print('Exception! Stop it!')
    print(e)

# Mismatched exception will not be captured

try:
    d = {'key': 23}
    print(d['does not exist'])
except KeyError as e:
    print("Got it!", e)

# Raising exception

try:
    raise ValueError("Message!")
except ValueError as e:
    print(e)

# try/except/else

try:
    print("Fine")
except KeyError:
    print("Nope.")
else:
    print("Else")

# try/except/finally

try:
    print(1 / 0)
except ZeroDivisionError:
    print("0!")
finally:
    print("Finally!")

