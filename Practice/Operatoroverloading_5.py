# wap to overload + operator to add two complex numbers.
class complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def __add__(self,other):
        real=self.real+other.real
        imag=self.imag+other.imag
        return complex(real,imag)
    
c1=complex(2,3)
c2=complex(3,2)
c3=c1+c2
print(c3.real,c3.imag)