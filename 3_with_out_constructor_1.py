## Using constructor we can create instance variables.
class One():
    def add(self, uname, password):
       print('\n ADD ', uname , password)
       
    def sub(self, uname, password, hostname,port):
        print(uname, password )

    def mul(self, uname, password):
        print(uname, password )

inst = One()
inst.add(10,20)
inst.sub(10,20,'admin', 23)
inst.mul(10,20)