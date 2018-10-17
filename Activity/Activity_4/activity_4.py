#2018.09.05
#Jayson Abad
#CL 3
from .items import users, names
import sys
class Activity4:
    def __init__(self):
        self.start()

    def view_names(self):
        print('\n')
        for k, v in names.items():
            print(k)

    def add(self):
        id = input('id: ')
        name = input('Name: ')
        bdate = input('B-Date: ')
        names[id] = {'name': name, 'birthdate': bdate}
        print('name added')

    def start(self):
        command = True
        back = 'no'
        while command:
            print('\nBirthday Dictionary')
            print('View names')
            print('Add\n')
            com = input('command: ')
            if com.lower() == 'view names':
                self.view_names()
                com = input('\ttype id: ')
                for k, v in names.items():
                    if com.lower() == k.lower():
                        print('%s\'s birthdate is %s'%(v['name'].title(), v['birthdate']))
                        back = input('go back to home?(yes/no): ')
                        if back == 'yes':
                            continue
                        elif back == 'no':
                            sys.exit()
                        else:
                            print('command is unknown')

            if com.lower() == 'add':
                self.add()
            elif back != 'no' and back != 'yes' and com.lower() != 'add' and com.lower() != 'view names':
                print('invalid command')
