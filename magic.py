# 1. create a class funtion using one of the magic methods.

class Magic:
    def __init__(self, name, age, magic, rank, life):
        self.name = name
        self.age = age
        self.magic = magic
        self.rank = rank
        self.life = life

    def attack(self):
        print(f"{self.name} the {self.age} year old {self.magic} has attacked")

    def heal(self):
        print(f"{self.name} the {self.age} year old {self.magic} has healed")

    def revive(self):
        print(f"{self.name} the {self.age} year old {self.magic} has revived")

    def __str__(self):
        return f"{self.name} the {self.age} year old {self.magic} has {self.rank} rank and {self.life} life"

# create a class function that the child class can inherit from the parent class.
class Fire(Magic):
    def __init__(self, name, age, magic, rank, life):
        super().__init__(name, age, magic, rank, life)

    def burn(self):
        print(f"{self.name} the {self.age} year old {self.magic} has burned")   


person = Magic("Harry", "20", "Wizard", "Master", "100")
print(person)

fire = Fire("Ron", "40", "Witch", "Novice", "50")
fire.attack()
fire.burn()

# 3. create a 2-D array and transform it into a transpose matrix.
# use numpy
import numpy as np

def transpose(arr):
    return np.transpose(arr)

arr = [[2,3], [4,6]]
print(transpose(arr))