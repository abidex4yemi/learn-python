class Vehicle:
    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel

    def is_eco_friendly(self):
        if self.fuel == "gas":
            return False
        else:
            return True


class Car(Vehicle):
    def __init__(self, make, model, fuel="solar", num_wheels=4):
        super().__init__(make, model, fuel="solar")
        self.num_wheels = num_wheels


toyota = Vehicle("Toyota", "corrola s")
print(toyota.is_eco_friendly())

tesla = Car("Tesla", "model s")
print(tesla.is_eco_friendly())
