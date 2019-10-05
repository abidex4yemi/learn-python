class Car:
    def __init__(self, name, runs=True):
        self.name = name
        self.runs = runs

    def start(self):
        if self.runs:
            print(f"{self.name} is started")
        else:
            print(f"{self.name} is broken :)!")


toyota = Car("Toyota")
toyota.start()
toyota.runs = False
toyota.start()
