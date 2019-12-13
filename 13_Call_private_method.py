class A():
    def add1(self):
        b = 20
        print(b)

    def __sub(self):
        print('private')

ins = A()

# To call Pravate method
ins._A__sub()
