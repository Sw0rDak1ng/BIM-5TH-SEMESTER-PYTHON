class Animal:
    def makesound(self):
        print('Animal is making sound.')

class Dog(Animal):
    def makesound(self):
        print('Dog is barking.')

        #  super().makesound()

d=Dog()
d.makesound()