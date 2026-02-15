#simple inheritance
'''
class Animal:
    def eat(self):
        print('Eating')
class Dog(Animal):
    pass
d=Dog()
d.eat()
#the derived class may also contains it"s own features
class Animal:
    def eat(self):
        print('Eating')
class Dog(Animal):
    def bark(self):
        print("Barking")
        
d=Dog()
d.eat()
d.bark()

#multilevel inheritanceclass Animal:
class Animal:
    def eat(self):
        print('Eating')
class Dog(Animal):
    def bark(self):
        print("Barking")
class Puppy(Dog):
    def play(self):
        print("Playing")
             
p=Puppy()
p.eat()
p.bark()
p.play()

#hiierarchial inheritance

class Animal:
    def eat(self):
        print('Eating')
class Dog(Animal):
    def bark(self):
        print("Barking")
class Tiger(Animal):
    def roar(self):
        print("Roar")
             
d=Dog()
d.bark()
d.eat()
t=Tiger()
t.roar() 

#multiple inheritance
class Tiger:
    def roar(self):
        print("Roar")
class Lion:
      def eat(self):
          print("Eating")
class Liger(Tiger,Lion):
    def play(self):
        print("Playing")
l=Liger()
l.roar()
l.play()
l.eat()'''

#
        




