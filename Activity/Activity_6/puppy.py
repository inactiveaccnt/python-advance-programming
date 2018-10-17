from .dog import Dog

class Puppy(Dog):

    def __init__(self, name, breed, age):
        super().__init__(name, age)
        self.breed = breed

    def sit(self):
        print('%s is now sitting.'%self.breed)
