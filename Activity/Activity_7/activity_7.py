

class Activity7:

    def __init__(self):
        self.list_of_files = { 'code.txt':'code.txt', 'message.txt':'message.txt' }
        self.sub_command = { 'append':'append', 'write':'write', 'count':'count', 'view':'view' }
        self.words = []
        self.state = 0
        self.run()

    def read_file(self, filename):
        with open(filename) as f:
            char = f.read()
            return char

    def write_file(self, filename, message):
        with open(filename, 'w') as f:
            f.write(message+" ")

    def append_file(self, filename, message):
        with open(filename, 'a') as f:
            f.write(message+" ")

    def count_char(self, filename):
        count = 0
        string = ""
        with open(filename) as f:
            char = f.read()
            for c in char:
                if c != " " or c != "\t" or c != "\n":
                    string += c
                if c == " " or c == "\t" or c == "\n":
                    self.words.append(string)
                    string = ""
        for word in self.words:
            count += 1
        return count

    def main_command(self):
        print("List of Files")
        print("1. %s"% self.list_of_files['code.txt'])
        print("2. %s"% self.list_of_files['message.txt'])
        self.com = input("Choose your file: ")

    def sub_commands(self):
        print("Command")
        print("1. %s"%self.sub_command['append'])
        print("2. %s"%self.sub_command['write'])
        print("3. %s"%self.sub_command['count'])
        print("4. %s"%self.sub_command['view'])
        self.sub_com = input(">>")

    def run(self):
        self.main_command()
        if(self.com == self.list_of_files['code.txt']):
            state = 1
            while(state == 1):
                self.sub_commands()
                if(self.sub_com == self.sub_command['append']):
                    self.text = input("Enter text: ")
                    self.append_file(self.list_of_files['code.txt'], self.text)
                elif(self.sub_com == self.sub_command['write']):
                    self.text = input("Enter text: ")
                    self.write_file(self.list_of_files['code.txt'], self.text)
                elif(self.sub_com == self.sub_command['count']):
                    print("Number of words: %s"%self.count_char(self.list_of_files['code.txt']))
                elif(self.sub_com == self.sub_command['view']):
                    print(self.read_file(self.list_of_files['code.txt']))
        elif(self.com == self.list_of_files['message.txt']):
            state = 1
            while(state == 1):
                self.sub_commands()
                if(self.sub_com == self.sub_command['append']):
                    self.text = input("Enter text: ")
                    self.append_file(self.list_of_files['message.txt'], self.text)
                elif(self.sub_com == self.sub_command['write']):
                    self.text = input("Enter text: ")
                    self.write_file(self.list_of_files['message.txt'], self.text)
                elif(self.sub_com == self.sub_command['count']):
                    print("Number of words: %s"%self.count_char(self.list_of_files['message.txt']))
                elif(self.sub_com == self.sub_command['view']):
                    print(self.read_file(self.list_of_files['message.txt']))
