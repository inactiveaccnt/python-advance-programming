#2018.09.12
#Jayson Abad
#CL 3
class Activity5:

    def __init__(self):
        self.result = []
        self.limit = int(input('Enter a number: '))
        self.fibonacci(0, 1, 1, self.limit)
        self.printResult()

    def fibonacci(self, num1, num2, num3, limit):
        self.result.append(num1)
        if num3 != limit:
            self.fibonacci(num2, num1 + num2, num3 + 1, limit)
        else:
            return

    def factorial(self, limit):
        if limit == 0:
            return 1
        else:
            return limit * self.factorial(limit - 1)

    def printResult(self):
        print('Fibonacci: %s' %self.result)
        print('Factorial: %s' %self.factorial(self.limit))
