def add(*args):
    sum1 = 0
    for e in args:
        sum1 += e
    return sum1


def add2(*args):
    return sum(args)


def calc(n=1, **kwargs):
    for key, value in kwargs.items():
        print(key, value)
    print(kwargs)
    print(kwargs["a"])
    n += kwargs["a"]
    n *= kwargs["b"]
    print(f"'n' é {n}")

print(add(1,2))
print(add2(1, 2))
calc(3, a=1, b=2)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"] # Evitar este uso pois gera exceção caso chamado
        self.model = kwargs.get("model") # Preferir este uso que retorna 'None'


my_car = Car(make="VW", model="gol")
my_car2 = Car(make="Hyundai")
print(my_car.make, my_car2.model)
