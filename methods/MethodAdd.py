from Contact import *
from Messages import Messages


def add_new_contact(contact: Contact):
    contacts = get_list_of_contacts()
    contacts.append(contact)
    load_contacts_to_file(list(set(contacts)))


def add():
    print(Messages.METHOD_ADD_HELLO_MESSAGE)
    contact = Contact()
    input_str = input()
    if input_str == Messages.COMMAND_EXIT:
        print(Messages.METHOD_ADD_BYE_MESSAGE)
    elif input_str.count(';') < 2:
        print(Messages.INPUT_INCORRECT)
    else:
        data = input_str.split(';')
        data_is_correct = True
        firstname = data[0]
        lastname = data[1]
        mobile_phone = data[2]

        data_is_correct = contact.set_firstname(firstname) and data_is_correct

        data_is_correct = contact.set_lastname(lastname) and data_is_correct

        data_is_correct = contact.set_mobile_phone(mobile_phone) and data_is_correct

        if len(data) == 4 and data[3] != '' and data_is_correct:
            data_is_correct = contact.set_birthday(data[3])

        if data_is_correct:
            print(contact)
            print(Messages.ADDING_CONTACT)
            add_new_contact(contact)
        else:
            print(Messages.INPUT_INCORRECT)
