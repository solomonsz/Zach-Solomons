
class Pet(object):
    def __init__(self,name,age,animal):
        self.name = name
        self.age = age
        self.is_hungry = False
        self.animal = animal
        self.mood = "happy"
    def eat(self):
        print("%s is eating" % self.name)
        if self.is_hungry:
            self.is_hungry = False
        else:
            print(" %s may have eaten too much" % self.name)
            self.mood = "lethargic"


pet = Pet("Dom",4,"dog")
pet.is_hungry = True
print("Is my pet hungry? %s" % pet.is_hungry)
pet.eat()
print("How about now? %s" % pet.is_hungry)
