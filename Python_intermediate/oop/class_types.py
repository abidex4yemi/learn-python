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

    @classmethod
    def get_number_of_wheels(cls):
        print(cls.number_of_wheels)


# Instanting a class
toyota = Car("Toyota")

# Calling instance method
toyota.start()
toyota.start()

# Calling class methods
toyota.get_number_of_wheels()
Car.get_number_of_wheels()

# checking type and instances
print(isinstance(42, int))
print(isinstance("Hello world", str))
print(isinstance(toyota, Car))

# Don't use this in production code
print(isinstance(True, int))

print(True + True)
print(set({0, 1, False, True}))
print(issubclass(Car, object))
print(issubclass(int, object))
