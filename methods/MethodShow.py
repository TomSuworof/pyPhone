from Contact import *
from Messages import Messages
from methods import MethodEdit


def formatted(input_str) -> str:
    return '{:^14}'.format(str(input_str))


def print_table(contacts: list):
    print(Messages.TABLE_SEPARATOR)
    for contact in contacts:
        index = formatted(contacts.index(contact))
        print(index, end='|')
        print(formatted(contact.firstname), end='|')
        print(formatted(contact.lastname), end='|')
        print(formatted(contact.mobile_phone), end='|')
        print(formatted(contact.work_phone), end='|')
        print(formatted(contact.home_phone), end='|')
        print(formatted(contact.birthday))


def show():
    print(Messages.METHOD_SHOW_HELLO_MESSAGE)
    print(Messages.TABLE_TITLE)
    print_table(get_list_of_contacts())
    print(Messages.METHOD_SHOW_COMMANDS_AVAILABLE)

    command = input()
    if command.split(' ')[0] == Messages.COMMAND_EDIT:
        try:
            MethodEdit.edit(int(command.split(' ')[1]))
        except IndexError:
            print(Messages.INDEX_ERROR)

    elif command == Messages.COMMAND_EXIT:
        pass
    else:
        print(Messages.COMMAND_INVALID)
    print(Messages.EXITING_EDIT_MODE)
