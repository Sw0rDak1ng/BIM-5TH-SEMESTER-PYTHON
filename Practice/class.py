class person:
    def __init__(self,n):
     self.name=n

class student(person):
   def __init__(self,n,f):
      super().__init__(n)
      self.faculty=f

s=student('Ram','Bim')
print(s.name,s.faculty)
   