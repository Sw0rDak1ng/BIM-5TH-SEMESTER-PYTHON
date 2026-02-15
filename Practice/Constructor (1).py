#Default constructor example
'''
class student:
    def __init__(self):
        self.name='Ram'
        self.age=20
s1=student()
print(s1.name,s1.age)'''

#Parameterized Constructor Examples
'''
class student:
    def __init__(self,n,a):
        self.name=n
        self.age=a
s1=student('Ram',20)
print(s1.name,s1.age)'''

#Constructor overloading examples
from multipledispatch import dispatch
class student:
    @dispatch(str,int)
    def __init__(self,n,a):
        self.name=n
        self.age=a
    @dispatch()    
    def __init__(self):
        self.name='Hari'
        self.age=20
    
s1=student('Ram',20)#calls the default constructor
print(s1.name,s1.age)
s2=student('Ram',20) #calls the parameterized constructor
print(s2.name,s2.age)





