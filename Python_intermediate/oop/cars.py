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
