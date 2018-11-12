class Person(object):


    def __init__(self, f_name, l_name):
        super(Person, self).__init__()
        self.first_name = f_name
        self.second_name = l_name
        self.__name = "Jayson"

    def print_name(self):
        print(self.first_name + " " + self.second_name)
        print(self.__name)


    def calculate_weight(self):
        weight = 45
        return weight
