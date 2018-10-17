
class Dog(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print("%s is now sitting."%self.name)
        print("%s age is %s"%(self.name, self.age))
