class Animal:
    def __init__(self, name, age, gender, species, temperament):
        self.name = name
        self.age = age
        self.gender = gender
        self.species = species
        self.temperament = temperament
        self.adoptedBy = None
    def __str__(self):
        return f"Animal:\nName: {self.name}\nAge: {self.age}\nGender: {self.gender}\nType: {self.species}\nTemperament: {self.temperament}\n"
animal1 = Animal("Zoe", 4, "F", "Cat", "Sleepy")
animal2 = Animal("Max", 5, "M", "Dog", "Friendly")
animal3 = Animal("Garfield", 1, "M", "Fish", "Aggresive")
animal4 = Animal("Zephyr", 3, "F", "Bird", "Intelligent")
unadopted = [animal1, animal2, animal3, animal4]
adopted = []
print("Welcome!\n\nAnimals available for adoption:\n")
for animal in unadopted:
    print(str(animal))
username = None
while True:
    if input("Would you like to adopt an animal? [y/n]: ").lower()[0] == "y":
        if not username:
            username = input("Please enter your name: ")
        adopt = input("What animal would you like to adopt? ")
        names = []
        for animal in unadopted:
            names.append(animal.name)
        if adopt in names:
            adopting = unadopted.pop(names.index(adopt))
            adopting.adoptedBy = username
            adopted.append(adopting)
            print(f"Successfully adopted {adopting.name}!")
    else:
        break