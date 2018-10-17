#2018.08.22
#Jayson Abad
#Computer Laboratory 3
class Activity_2_0:
    def __init__(self):
        super(Activity_2_0, self).__init__()
        self.name = ""
        self.age = 0
        self.year = 0
        self.askquestion()
        self.message()
        pass#to pass errors

    def askquestion(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        pass#to pass errors

    def message(self):
        print("Your name is %s"%self.name)
        print("Your age is %s"%self.age)
        print("You will turn 100 when %s"%(2018+100-self.age))
        pass#to pass errors
################################################################################
#2018.08.22
#Jayson Abad
#Computer Laboratory 3
class Activity_2_1_1:
    def __init__(self, index):
        super(Activity_2_1_1, self).__init__()
        self.bicycle = ['trek', 'bmx', 'redline', "mark one"]
        self.cars = ['toyota', 'BMW', 'Honda']
        self.access(index)
        self.change(index)
        self.inserting()
        self.appending()
        self.display()
        self.removing(index)
        self.display()
        self.condition()
        pass#to pass errors

    def access(self, index):
        print(self.bicycle[index].title())
        print(self.bicycle[index].upper())
        print(self.bicycle[index].lower())
        print(self.bicycle[-1])
        pass#to pass errors

    def change(self, index):
        self.bicycle[index] = "ducati"
        pass#to pass errors

    def inserting(self):
        self.bicycle.insert(2, "mark six")
        pass#to pass errors

    def appending(self):
        self.bicycle.append("mark two")
        self.bicycle.append("mark three")
        self.bicycle.append("mark four")
        self.bicycle.append("mark five")
        pass#to pass errors

    def removing(self, index):
        self.bicycle.remove("mark two")
        self.bicycle.pop(index)
        pass#to pass errors

    def display(self):
        print(self.bicycle)
        pass#to pass errors

    def condition(self):
        print("#"*100)
        print(self.cars)
        if self.cars == 'toyota':
            print("True")
            pass#to pass errors
        elif 'BMW' not in self.cars:
            print("True")
            pass#to pass errors
        else:
            print("False")
            pass#to pass errors
        pass#to pass errors
################################################################################
#2018.08.22
#Jayson Abad
#Computer Laboratory 3
class Activity_2_1:
    def __init__(self):
        super(Activity_2_1, self).__init__()
        self.number = 0
        self.check = 0
        self.activity_2_1_10()
        self.activity_2_1_20()
        pass#to pass errors

    def activity_2_1_10(self):
        self.number = int(input("Enter a number: "))
        self.check = int(input("Enter second number: "))
        if (self.number % 2) == 0:
            if (self.number % 4) == 0:
                print("%s is a multiple of 4"%self.number)
            else:
                print("%s is Even."%self.number)
        elif (self.number % 2) == 1:
            print("%s is Odd."%self.number)
        else:
            pass
        pass
        
    def activity_2_1_20(self):
        if (self.number%self.check) == 0:
            print("%s divides %s evenly"%(self.check, self.number))
        else:
            print("%s does not divides %s evenly"%(self.check, self.number))
        pass#to pass errors
################################################################################
