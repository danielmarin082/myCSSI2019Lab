pet = {
"name": "Pupper",
"animal": "dog",
"species": "labrador",
"age": 5
}
class Pet(object):
    def __init__(self, name, age, animal):
        self.name = name
        self.age = age
        self.animal = animal
        self.is_hungry = False
        self.mood = "happy"
        self.location = "room1"
    def eat(self):
        print("> %s is eating..." % self.name)
        if self.is_hungry:
            self.is_hungry = False
        else:
            print("> %s may have eaten too much." % self.name)
            self.mood = "lethargic"
    def move(self):
        print("> %s is moving..." % self.name)
        if self.is_moving:
            self.is_moving = True
my_pet = Pet("Kirby", 10, "dog")
my_pet.is_hungry = True
print("Are you hungry Kirb? %s" % my_pet.is_hungry)
my_pet.eat()
print("How about now? %s" % my_pet.is_hungry)
print("Kirb is feeling %s" % my_pet.mood)
# print("My pet %s is %s years old" % (my_pet.name, my_pet.age))
# my_pet = Pet("Fancy", 1)
# print("My pet %s is %s years old" % (my_pet.name, my_pet.age))
# my_pet = Pet("Pincher", 3)
# print("My pet %s is %s years old" % (my_pet.name, my_pet.age))
