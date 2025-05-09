class Animal:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} the Animal has been constructed.")
    def __del__(self):
        print(f"{self.name} the Animal has been destructed.")
class Mammal(Animal):
    def __init__(self, name, warm_blooded=True):
        super().__init__(name)
        self.warm_blooded = warm_blooded
        print(f"{self.name} is classified as a Mammal.")
if __name__ == "__main__":
    print("--- Starting Program ---")
    lion = Mammal("Simba")
    print("--- End of Program ---")
