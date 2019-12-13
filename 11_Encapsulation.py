'''
1. Encapsulation is wrapping data or functionality(methods accessing data) together into single unit.

2. Giving protection to the class or class members. Using access specifiers/modifiers we can achive it.
'''

class One():
    name = 'sriam'
    def __init__(self, a):
        self.a = a

    def add(self):
        print('sum is ')

    def sub(self):
        print('sub is:')
        cls._add()

ins = One(3)
print('\n ', ins.name)

