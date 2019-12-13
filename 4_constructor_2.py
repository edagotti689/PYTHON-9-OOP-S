## Using constructor we can create instance variables.
class One():
    def __init__(self, uname, password):
        self.uname = uname
        self.password = password
        print('__INIT__')

    def add(self):
       print(self.uname , self.password)
       
    def sub(self, hostname,port):
        print(self.uname, self.password )

    def mul(self):
        print(self.uname, self.password )

inst = One('admin','admin123')
inst.add()
inst.sub('admin', 23)
inst.mul()