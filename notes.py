# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

from os import fchdir
from tkinter import N


class Dog:
    # functions that start with __ are not intended to be called
    def __init__(self, n = "", fc = "", a = 0, ff = "",):
    # """"Creates an instance of the dog class and sets attributes"""
    
        self.name = n
        self.fur_colour = fc
        self.age = a
        self.favourite_food = ff
        self.fetch_count = 0

    def __str__(self) -> str:
        """"Return a string representation of a dog"""

        s = "Dogs name is " + self.name + "/n"
        s += "amd age is " + str(self.age) + "/n"
        s += " and fur colour is " + self.fur_colour + "/n"
        s += "and they have played fetch " + str(self.fetch_count) + "/n"

        return s
    
    def play_fetch(self, num_times):
        self.fetch_count += num_times

mydog = Dog("logan", "black", 7, "salmon")
chrisdog = Dog("luna", "balck and white", 6, "tortillas")

print(mydog)
print(chrisdog)

mydog.play_fetch(20)
chrisdog.play_fetch(3)

print(mydog)
# print((chrisdog.name) has played fetch 

