def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def calc(a, b, func):
    return func(a, b)


res = calc(2, 3, add)
print(res)
print(calc(2, 3, sub))
print(calc(2, 3, mul))
print(calc(2, 3, div))
