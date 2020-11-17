from Messages import Messages
from methods import MethodAdd, MethodShow, MethodFind, MethodAge


class MainActivity:
    if __name__ == '__main__':
        print(Messages.MAIN_HELLO_MESSAGE)
        print(Messages.MAIN_COMMANDS_AVAILABLE)
        command = input()
        while command != Messages.COMMAND_EXIT:
            try:
                if command == Messages.COMMAND_ADD:
                    MethodAdd.add()
                elif command == Messages.COMMAND_SHOW:
                    MethodShow.show()
                elif command == Messages.COMMAND_FIND:
                    MethodFind.find()
                elif command == Messages.COMMAND_AGE:
                    MethodAge.age()
                else:
                    print(Messages.COMMAND_INVALID)
            except IndexError:
                print(Messages.INPUT_INCORRECT)
            print(Messages.MAIN_COMMANDS_AVAILABLE)
            command = input()
        print(Messages.BYE_MESSAGE)
