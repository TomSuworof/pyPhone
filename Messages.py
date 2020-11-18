class Messages:
    MAIN_HELLO_MESSAGE = '''Welcome to pyPhone'''

    MAIN_COMMANDS_AVAILABLE = \
        '''Commands available:
- add - adding new contact
- show - show all records and editing them
- find - show records matching the conditions
- age - working with contacts' age
- exit - ending work'''

    COMMAND_EXIT = 'exit'

    COMMAND_ADD = 'add'

    COMMAND_SHOW = 'show'

    COMMAND_EDIT = 'edit'

    COMMAND_SET = 'set'

    COMMAND_CLEAR = 'clear'

    COMMAND_DELETE = 'delete'

    COMMAND_FIND = 'find'

    COMMAND_AGE = 'age'

    COMMAND_INVALID = 'I do not know this command'

    METHOD_ADD_HELLO_MESSAGE = '''You chose 'add'
Enter info about record. You can choose any type
- 'firstname';'lastname';'mobile_phone';'birthday'
- 'firstname';'lastname';'mobile_phone'
(birthday should be in format yyyy-mm-dd)
- exit - exiting add-mode'''

    INPUT_INCORRECT = 'Your input is incorrect'

    CONTACT_EXISTS = 'Contact with these firstname and lastname already exists'

    ADDING_CONTACT = 'Adding new contact...'

    METHOD_ADD_BYE_MESSAGE = 'Ok. You are exiting add-mode'

    METHOD_SHOW_HELLO_MESSAGE = '''You chose 'show'
List of your contacts:'''

    METHOD_SHOW_COMMANDS_AVAILABLE = '''You can pick one pick 1 record and edit it or continue surfing
- edit 'index' - editing chosen contact
- exit - exiting edit and viewing mode'''

    TABLE_TITLE = '    Index     |  Firstname   |   Lastname   | Mobile phone |  Work phone  |  Home phone  |   Birthday   '

    TABLE_SEPARATOR = '--------------+--------------+--------------+--------------+--------------+--------------+--------------'

    METHOD_EDIT_HELLO_MESSAGE = '''Now you are in the edit-mode
Methods available
- set 'field=value' - changing value of the entered field to new value
- clear 'field' - clear the entered field
- delete - delete the record
(name of field should be in snake_case)
- exit - exiting from edit-mode'''

    INDEX_ERROR = '''Error. Index more than book-size or was not entered'''

    EXITING_EDIT_MODE = 'You are exiting edit-mode'

    AFTER_DELETING = 'The record has been deleted'

    METHOD_FIND_HELLO_MESSAGE = '''You chose 'find'
Here you can find all records, matches condition entered
Syntax: 
- field=value
- field_1=value_1;field=2=value_2
(fields should be snake_case)
- exit - ending search'''

    RECORDS_WAS_NOT_FOUND = 'Records were not found'

    METHOD_FIND_BYE_MESSAGE = 'Ok. You are exiting search-mode'

    METHOD_AGE_HELLO_MESSAGE = '''You chose 'age'
Here you can work with age of your contacts
- show - printing contacts by birthday
- show_near - printing contacts which birthday in a month
- show_age - printing contacts which age matches with condition (='years', <'years', >'years')
- show 'firstname;lastname' - getting age of your contact with entered firstname and lastname
- exit - ending search through age'''

    NO_NEAR_PARTIES = 'Sorry. You do not have near parties ;('

    METHOD_AGE_BYE_MESSAGE = 'Ok. You are exiting age-mode'

    BYE_MESSAGE = \
        '''Ending work...
Have a nice day!'''

    FIELD_FIRSTNAME = 'firstname'
    FIELD_LASTNAME = 'lastname'
    FIELD_MOBILE_PHONE = 'mobile_phone'
    FIELD_WORK_PHONE = 'work_phone'
    FIELD_HOME_PHONE = 'home_phone'
    FIELD_BIRTHDAY = 'birthday'
    FIELD_NOT_RECOGNIZED = 'Field was not recognised. You are exiting edit-mode'
    FIELD_CAN_NOT_BE_CLEAR = 'Field can not be clear. You are exiting edit-mode'
