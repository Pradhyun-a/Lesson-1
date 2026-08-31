class Pet:
    print("Class is running")

pet_object = Pet()

class PetProfile:
    category = "pet"

    def __init__(self, name, animal_type, age, favourite_food):
        self.name = name
        self.animal_type = animal_type
        self.age = age
        self.favourite_food = favourite_food

pet1 = PetProfile("Buddy", "Dog", 3, "Bone")
pet2 = PetProfile("Whiskers", "Cat", 2, "Fish")

print(pet1.category)
print(pet2.category)
print(pet1.name)
print(pet2.favourite_food)
