class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal created: {self.name}")
    def info(self):
        print(f"{self.name} is an animal.")
class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)
        print(f"{self.name} is classified as a mammal.")
if __name__ == "__main__":
    m = Mammal("Simba")
    m.info()
