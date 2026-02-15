class A:
    def printSth(self):
        print("sth")


class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

d=D()
d.printSth()