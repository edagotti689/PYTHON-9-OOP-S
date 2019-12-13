## Using super we can call parent class methods
class One:
    def __init__(self):
        print('__init__ of One')

    def add(self):
        print(' One add is ')

class Two(One):
    def add(self):
        print(' Two add is ')
        # super().add()
        # ins2 = One()
        # ins2.add()


ins = Two()
ins.add()