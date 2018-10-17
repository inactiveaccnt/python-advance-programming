

class FileAndException:

    def __init__(self):
        pass

    def read_file(self, filename):
        with open(filename) as f_obj:
            contents = f_obj.read()
            print(contents)

    def write_file(self, filename, message):
        with open(filename, 'w') as f_obj:
            f_obj.write(message)

    def exception_handling(self):
        try:
            print(1/0)
        except ZeroDivisionError as err:
            print("%s can't divide"%err)
