'''
1. We can inherit a derived class from another derived class, this process is known as multilevel inheritance
2. In multilevel inheritance, we inherit the classes at multiple separate levels.
3. We have three classes A, B and C, where A is the super class, B is its sub(child) class and C is the sub class of B.
'''

class A():
    name = 'sriram'
    def add(self, a, b):
        print('sum is', a + b)

    def sub(self, a, b):
        print('sub is', a - b)

class B(A):
    def colour(self):
        print('Blue')

class C(B):
    pass

ins = C()
ins.colour()
print(ins.name)
