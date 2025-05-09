class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal class: {self.name} has been created.")
    def __del__(self):
        print(f"Animal class: {self.name} is being destroyed.")
class Mammal(Animal):
    def __init__(self, name, warm_blooded=True):
        super().__init__(name)
        self.warm_blooded = warm_blooded
        print(f"Mammal subclass: {self.name}, warm-blooded={self.warm_blooded}")
if __name__ == "__main__":
    m = Mammal("Simba")