import sys
import csv

class Todo():

    def __init__(self):
        self.file_name = 'todo_list.csv'

    def main_menu(self):
        print('                           ')
        print('===========================')
        print('       COMMAND YOUR        ')
        print('           TODOs           ')
        print('                           ')
        print('         Commands:         ')
        print('                           ')
        print(' -l Lists all the tasks    ')
        print(' -a Adds a new tasks       ')
        print(' -r Removes a task         ')
        print(' -c Checks a task          ')
        print(' -u Unchecks a task        ')
        print(" Type 'exit' to quit       ")
        print('===========================')

    def ok_argument(self):
        arguments = ['-l', '-a', '-r', '-c', '-u', 'exit']
        if sys.argv[1] not in arguments:
            print('Unsupported argument')
            self.main_menu()

    def controller_l(self):
        if len(sys.argv) == 2:
            print(self.load_list())
        else:
            print('Too many arguments were given, only give 1!')

    def controller_a(self):
        if len(sys.argv) == 2:
            print('Unable to add: No task is provided')
        else:
            self.add_to_list(sys.argv[2])

    def controller_c(self):
        if len(sys.argv) == 2:
            print('Unable to check: No index is provided')
        elif sys.argv[2] == '0':
            print('Unable to check: Index out of range')
        else:
            self.check_task()

    def controller_u(self):
        if len(sys.argv) == 2:
            print('Unable to uncheck: No index is provided')
        elif sys.argv[2] == '0':
            print('Unable to uncheck: Index out of range')
        else:
            self.uncheck_task()

    def controller_r(self):
        if len(sys.argv) == 2:
            print('Unable to remove: No index is provided')
        elif sys.argv[2] == '0':
            print('Unable to remove: Index out of range')
        else:
            self.remove_from_list(sys.argv[2])

    def main(self):
        self.missing_file()
        if len(sys.argv) == 1:
            self.main_menu()
        else:
            self.ok_argument()
            if sys.argv[1] == '-l':
                self.controller_l()
            elif sys.argv[1] == '-a':
                self.controller_a()
            elif sys.argv[1] == '-r':
                self.controller_r()
            elif sys.argv[1] == '-c':
                self.controller_c()
            elif sys.argv[1] == '-u':
                self.controller_u()
            elif sys.argv[1] == 'exit':
                print('Goodbye!')
                exit()

    def load_list(self):
        f = open(self.file_name)
        todo_list = csv.reader(f, delimiter = ';')
        output = ''
        number = 1
        for i in todo_list:
            output += (str(number) + ' - ' + self.checked_or_not(i[0]) + ' '+ i[1] + '\n')
            number += 1
        f.close()
        if output == '':
            return 'No todos for today! :)'
        else:
            return output

    def checked_or_not(self, x):
        if x == 'True':
            return '[x]'
        else:
            return '[ ]'

    def add_to_list(self, new_todo_element):
        f = open(self.file_name, 'a')
        f.write('False;' + new_todo_element + '\n')
        f.close()

    def check_task(self):
        f = open(self.file_name)
        check_task = csv.reader(f, delimiter = ';')
        output = []
        try:
            task_number = int(sys.argv[2])
            for i in check_task:
                output.append(i)
            if output[task_number-1][0] == 'True':
                print('Task already checked!')
            elif output[task_number-1][0] == 'False':
                    output[task_number-1][0] = 'True'
            f.close()
            self.write_task(output)
        except ValueError:
                print('Unable to check: Index is not a number')
        except IndexError:
                print('Unable to check: Index is out of bound')

    def write_task(self, input):
        f = open(self.file_name, 'w')
        for i in input:
            f.write(i[0] + ';' + i[1] + '\n')
        f.close()

    def uncheck_task(self):
        f = open(self.file_name)
        uncheck_task = csv.reader(f, delimiter = ';')
        output = []
        try:
            task_number = int(sys.argv[2])
            for i in uncheck_task:
                output.append(i)
            if output[task_number-1][0] == 'True':
                output[task_number-1][0] = 'False'
            elif output[task_number-1][0] == 'False':
                print('Task already unchecked!')
            f.close()
            self.write_task(output)
        except ValueError:
                print('Unable to uncheck: Index is not a number')
        except IndexError:
                print('Unable to uncheck: Index is out of bound')

    def remove_from_list(self, remove_n_task):
        f = open(self.file_name)
        remove_line = f.readlines()
        try:
            remove_line.remove(remove_line[int(remove_n_task)-1])
        except ValueError:
                print('Unable to remove: Index is not a number')
        except IndexError:
                print('Unable to remove: Index is out of bound')
        f.close()
        f = open(self.file_name, 'w')
        for i in remove_line:
            f.write(i)
        f.close()



    def create_file(self):
            f = open('todo_list.csv', 'a')
            f.close()

    def missing_file(self):
        try:
            f = open(self.file_name, 'a')
            f.close()
        except FileNotFoundError:
            self.create_file()

todo = Todo()
todo.main()
