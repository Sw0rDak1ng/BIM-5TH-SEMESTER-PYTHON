class A:
    def test(self):
        print('Inside A ')


class B(A):
    def test(self):
        print('Inside B ')
        super().test()
b=B()
b.test()
