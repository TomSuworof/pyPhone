from Contact import get_list_of_contacts
from Messages import Messages
from methods.MethodShow import print_table
import re


def find_by_firstname(firstname: str, contacts) -> list:
    return list(filter(lambda contact: re.search(firstname, contact.firstname, re.IGNORECASE), contacts))


def find_by_lastname(lastname: str, contacts) -> list:
    return list(filter(lambda contact: re.search(lastname, contact.lastname, re.IGNORECASE), contacts))


def find_by_mobile_phone(mobile_phone: str, contacts) -> list:
    return list(filter(lambda contact: mobile_phone in contact.mobile_phone, contacts))


def find_by_work_phone(work_phone: str, contacts) -> list:
    return list(filter(lambda contact: work_phone in contact.work_phone, contacts))


def find_by_home_phone(home_phone: str, contacts) -> list:
    return list(filter(lambda contact: home_phone in contact.home_phone, contacts))


def find_by_birthday(birthday: str, contacts) -> list:
    return list(filter(lambda contact: birthday in str(contact.birthday), contacts))


def find_by_criteria(criteria: dict) -> list:
    contacts = get_list_of_contacts()
    was_search = False
    if Messages.FIELD_FIRSTNAME in criteria.keys():
        contacts = find_by_firstname(criteria[Messages.FIELD_FIRSTNAME], contacts)
        was_search = True
    if Messages.FIELD_LASTNAME in criteria.keys():
        contacts = find_by_lastname(criteria[Messages.FIELD_LASTNAME], contacts)
        was_search = True
    if Messages.FIELD_MOBILE_PHONE in criteria.keys():
        contacts = find_by_mobile_phone(criteria[Messages.FIELD_MOBILE_PHONE], contacts)
        was_search = True
    if Messages.FIELD_WORK_PHONE in criteria.keys():
        contacts = find_by_work_phone(criteria[Messages.FIELD_WORK_PHONE], contacts)
        was_search = True
    if Messages.FIELD_HOME_PHONE in criteria.keys():
        contacts = find_by_home_phone(criteria[Messages.FIELD_HOME_PHONE], contacts)
        was_search = True
    if Messages.FIELD_BIRTHDAY in criteria.keys():
        contacts = find_by_birthday(criteria[Messages.FIELD_BIRTHDAY], contacts)
        was_search = True
    if not was_search or len(contacts) == 0:
        print(Messages.RECORDS_WAS_NOT_FIND)
    else:
        return contacts


def find():
    print(Messages.METHOD_FIND_HELLO_MESSAGE)
    print(Messages.TABLE_TITLE)
    data = input()
    if data == Messages.COMMAND_EXIT:
        print(Messages.METHOD_FIND_BYE_MESSAGE)
    else:
        key_value_pairs = data.split(';')
        criteria = {pair.split('=')[0]: pair.split('=')[1] for pair in key_value_pairs}
        print_table(find_by_criteria(criteria))
