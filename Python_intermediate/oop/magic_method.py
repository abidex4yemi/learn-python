import datetime


class Car:
    runs = True
    number_of_wheels = 4

    def __init__(self, name):
        self.name = name

    def start(self):
        if self.runs:
            print(f"{self.name} is started")
        else:
            print(f"{self.name} is broken :)!")

    def __str__(self):
        return f"Car name: {self.name} has {self.number_of_wheels} wheels"

    def __repr__(self):
        return f"Car {self.name}"

    @classmethod
    def get_number_of_wheels(cls):
        print(cls.number_of_wheels)


my_toyota = Car("Toyota")
print(str(my_toyota))
print(repr(my_toyota))

now = datetime.datetime.now()
print(now)
print(repr(now))
