import datetime
import json

from Messages import Messages


def from_dict(dictionary: dict):
    firstname = dictionary['firstname']
    lastname = dictionary['lastname']
    mobile_phone = dictionary['mobile_phone']
    work_phone = dictionary['work_phone']
    home_phone = dictionary['home_phone']
    birthday = dictionary['birthday']
    return Contact(firstname,
                   lastname,
                   mobile_phone,
                   work_phone,
                   home_phone,
                   birthday)


def to_dict(contact) -> dict:
    contact_as_dict = {
        'firstname': contact.firstname,
        'lastname': contact.lastname,
        'mobile_phone': contact.mobile_phone,
        'work_phone': contact.work_phone,
        'home_phone': contact.home_phone,
        'birthday': str(contact.birthday)
    }
    return contact_as_dict


def get_list_of_contacts() -> list:
    with open('phoneBook.json', 'r') as phone_book:
        contacts = list(json.load(phone_book))
    return [from_dict(contact) for contact in contacts]


def load_contacts_to_file(contacts: list):
    contacts = [to_dict(contact) for contact in contacts]
    with open('phoneBook.json', 'w') as phone_book:
        phone_book.write(json.dumps(contacts))


class Contact:
    firstname: str
    lastname: str
    mobile_phone: str
    work_phone: str
    home_phone: str
    birthday: datetime.date = None

    def __init__(self,
                 firstname: str = None,
                 lastname: str = None,
                 mobile_phone: str = None,
                 work_phone: str = None,
                 home_phone: str = None,
                 birthday: str = None
                 ):
        self.firstname = firstname or ''
        self.lastname = lastname or ''
        self.mobile_phone = mobile_phone or ''
        self.work_phone = work_phone or ''
        self.home_phone = home_phone or ''
        birthday = str(birthday)
        if birthday != 'None':
            birthday_data = [int(x) for x in birthday.split('-')]
            birthday = datetime.date(
                birthday_data[0],
                birthday_data[1],
                birthday_data[2]
            )
            self.birthday = birthday

    def __str__(self):
        return f'''
- {Messages.FIELD_FIRSTNAME}: {self.firstname}
- {Messages.FIELD_LASTNAME}: {self.lastname}
- {Messages.FIELD_MOBILE_PHONE}: {self.mobile_phone}
- {Messages.FIELD_WORK_PHONE}: {self.work_phone}
- {Messages.FIELD_HOME_PHONE}: {self.home_phone}
- {Messages.FIELD_BIRTHDAY}: {self.birthday}
'''

    def set_firstname(self, firstname: str):
        if firstname.isalpha():
            self.firstname = firstname.capitalize()
            return True
        else:
            return False

    def set_lastname(self, lastname: str):
        if lastname.isalpha():
            self.lastname = lastname.capitalize()
            return True
        else:
            return False

    def set_mobile_phone(self, phone: str):
        if phone.isalnum() and len(phone) == 11:
            self.mobile_phone = phone
            return True
        else:
            return False

    def set_work_phone(self, phone: str):
        if phone.isalnum() and len(phone) == 11:
            self.work_phone = phone
            return True
        else:
            return False

    def set_home_phone(self, phone: str):
        if phone.isalnum() and len(phone) == 11:
            self.home_phone = phone
            return True
        else:
            return False

    def set_birthday(self, date: str):
        birthday_str = date.split('-')
        year = int(birthday_str[0])
        month = int(birthday_str[1])
        day = int(birthday_str[2])
        try:
            self.birthday = datetime.date(year, month, day)
            return True
        except ValueError:
            return False
