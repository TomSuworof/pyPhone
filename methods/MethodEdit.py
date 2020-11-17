from Contact import *
from Messages import Messages


def set_new_value(field: str, new_value: str, index: int):
    contacts = get_list_of_contacts()
    contact = contacts[index]
    if field == Messages.FIELD_FIRSTNAME:
        contact.set_firstname(new_value)
    elif field == Messages.FIELD_LASTNAME:
        contact.set_lastname(new_value)
    elif field == Messages.FIELD_MOBILE_PHONE:
        contact.set_mobile_phone(new_value)
    elif field == Messages.FIELD_WORK_PHONE:
        contact.set_work_phone(new_value)
    elif field == Messages.FIELD_HOME_PHONE:
        contact.set_home_phone(new_value)
    elif field == Messages.FIELD_BIRTHDAY:
        contact.set_birthday(new_value)
    else:
        print(Messages.FIELD_NOT_RECOGNIZED)

    print(contact)
    contacts[index] = contact
    load_contacts_to_file(contacts)


def clear_field(field: str, index):
    contacts = get_list_of_contacts()
    contact = contacts[index]
    if field == Messages.FIELD_FIRSTNAME or field == Messages.FIELD_LASTNAME:
        print(Messages.FIELD_CAN_NOT_BE_CLEAR)
        return
    elif field == Messages.FIELD_MOBILE_PHONE:
        contact.mobile_phone = ''
    elif field == Messages.FIELD_WORK_PHONE:
        contact.work_phone = ''
    elif field == Messages.FIELD_HOME_PHONE:
        contact.home_phone = ''
    elif field == Messages.FIELD_BIRTHDAY:
        contact.birthday = str(None)
    else:
        print(Messages.FIELD_NOT_RECOGNIZED)

    print(contact)
    contacts[index] = contact
    load_contacts_to_file(contacts)


def delete_record(index: int):
    contacts = get_list_of_contacts()
    contacts.remove(contacts[index])
    load_contacts_to_file(contacts)
    print(Messages.AFTER_DELETING)


def edit(index: int):
    print(Messages.METHOD_EDIT_HELLO_MESSAGE)
    command = input()
    if command.split(' ')[0] == Messages.COMMAND_SET:
        set_new_value(command.split(' ')[1].split('=')[0], command.split(' ')[1].split('=')[1], index)
    elif command.split(' ')[0] == Messages.COMMAND_CLEAR:
        clear_field(command.split(' ')[1], index)
    elif command == Messages.COMMAND_DELETE:
        delete_record(index)
    elif command == Messages.COMMAND_EXIT:
        print(Messages.EXITING_EDIT_MODE)
    else:
        print(Messages.COMMAND_INVALID)
