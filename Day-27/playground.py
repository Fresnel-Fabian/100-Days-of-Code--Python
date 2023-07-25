def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)


add(1, 3, 5, 7)


def cal(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["mul"]
    print(n)


cal(5, add=5, mul=10)

class Car:

    def __init__(self, **kwargs):
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.maker = kwargs.get("maker")


my_car = Car(model="DBX", color="black")
print(my_car.color)
print(my_car.model)
print(my_car.maker)