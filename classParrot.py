class Parrot:
    species = "bird"
    def _init_(self, name, age):
        self.name = name
        self.age = age

parrot1 = Parrot("Blue", 10)
parrot2 = Parrot("Woo", 15)
print("Parrot1 is a", parrot1.species)
print("Parrot2 is also a", parrot2.species)
print(parrot1.name, "is", parrot1.age, "years old")
print(parrot2.name, "is", parrot2.age, "years old")
