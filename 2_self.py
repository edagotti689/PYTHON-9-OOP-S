'''
1. self is used to refer the instance of the class to the method.
2. Based on self only method will get to know for which instace it has to responce.
3. We can give any name in place of self 
'''

class One():
    def add(self):
       print(' \n ID of self is : ',id(self))
       
    def sub(r, a, b):
        print(' \n ID of r is : ',id(r))

ins = One()
ins2 = One()

print(' \n ID of ins is : ',id(ins))
#ins.sub(5,3)
ins.add()
#ins.sub(10,5)
#ins2.sub(100,5)