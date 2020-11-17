import datetime
import calendar

from Contact import get_list_of_contacts
from Messages import Messages
from methods import MethodFind


def show_age_of_contact(firstname: str, lastname: str):
    contacts = MethodFind.find_by_criteria(
        {
            Messages.FIELD_FIRSTNAME: firstname,
            Messages.FIELD_LASTNAME: lastname
        }
    )
    today = datetime.date.today()
    for contact in contacts:
        print(f'- {contact.firstname} {contact.lastname}, {(today - contact.birthday).days // 365}')


def show_age(data: str):
    firstname = data.split(';')[0]
    lastname = data.split(';')[1]
    show_age_of_contact(firstname, lastname)


def get_by_birthday(year=1970) -> list:
    contacts = get_list_of_contacts()
    for contact in contacts:
        contact.set_birthday(str(year) + str(contact.birthday)[4:])
    return sorted(contacts, key=lambda item: item.birthday)


def get_near_by_birthday() -> list:
    contacts = get_by_birthday() + get_by_birthday(1971)
    today = datetime.date.today()
    today = datetime.date(1970, today.month, today.day)
    return list(filter(lambda contact: 0 < (contact.birthday - today).days < 30, contacts))


def show_with_birthday(contacts: list):
    for contact in contacts:
        print(f'- {contact.firstname} {contact.lastname}, {contact.birthday.day} {calendar.month_abbr[contact.birthday.month]}')


def show_age_matched(condition: str):
    contacts = get_list_of_contacts()
    years = int(condition[1:])
    condition = condition[0]
    today = datetime.date.today()
    if condition == '<':
        contacts = list(filter(lambda contact: (today - contact.birthday).days // 365 < years, contacts))
    elif condition == '>':
        contacts = list(filter(lambda contact: (today - contact.birthday).days // 365 > years, contacts))
    elif condition == '=':
        contacts = list(filter(lambda contact: (today - contact.birthday).days // 365 == years, contacts))
    else:
        print(Messages.INPUT_INCORRECT)
    for item in contacts:
        print(f'- {item.firstname} {item.lastname}, {(today - item.birthday).days // 365}')


def age():
    print(Messages.METHOD_AGE_HELLO_MESSAGE)
    data = input()
    if data == Messages.COMMAND_SHOW:
        show_with_birthday(get_by_birthday())
    elif data == Messages.COMMAND_SHOW + '_near':
        near_birthday_boys = get_near_by_birthday()
        if len(near_birthday_boys) > 0:
            show_with_birthday(get_near_by_birthday())
        else:
            print(Messages.NO_NEAR_PARTIES)
    elif data.split(' ')[0] == Messages.COMMAND_SHOW + '_' + Messages.COMMAND_AGE:
        show_age_matched(data.split(' ')[1])
    elif data.split(' ')[0] == Messages.COMMAND_SHOW:
        show_age(data.split(' ')[1])
    elif data == Messages.COMMAND_EXIT:
        print(Messages.METHOD_AGE_BYE_MESSAGE)
