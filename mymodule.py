#This is mymodule.py
def powNumber(a):
    return a ** 2


def factorial(a):
    f = 1
    for i in range(1, a + 1):
        f *= i
    return f


def primeNumber(a):
    for i in range(2, a):
        if a % i == 0:
            return False
    return True if a > 1 else False