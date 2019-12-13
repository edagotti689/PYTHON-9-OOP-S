'''
1. Using @staticmethod decorator we can create static method. For Static method self argument doesn't required.
2. Using @classmethod decorator we can create Class method. For class method we have to give cls argument.
'''
class One():
    name = 'sriram'
    @staticmethod
    def add():
        print(' Staticmethod')

    @classmethod
    def sub(k, n):
        print(' id of One ', id(One),' id of k ', id(k))
        k.name = n
        print('class variable name is', k.name)

inst = One()
#One.sub('kumar')
inst.sub('Balu')






