# pyPhone
This is my phone book, made for homework at university

Method hierarchy:
- add - adding new contact
  - 'firstname';'lastname';'mobile_phone';'birthday'
  - 'firstname';'lastname';'mobile_phone'
  (birthday should be in format yyyy-mm-dd)
  - exit - exiting add-mode
- show - show all records and editing them
  - edit 'index' - editing chosen contact
    - set 'field=value' - changing value of the entered field to new value
    - clear 'field' - clear the entered field
    - delete - delete the record
    (name of field should be in snake_case)
    - exit - exiting from edit-mode
  - exit - exiting edit and viewing mode- find - show records matching the conditions
- find - show records matching the conditions
  - field=value
  - field_1=value_1;field=2=value_2
  (fields should be snake_case)
  - exit - ending search
- age - working with contacts' age
  - show - printing contacts by birthday
  - show_near - printing contacts which birthday in a month
  - show_age - printing contacts which age matches with condition (='years', <'years', >'years')
  - show 'firstname;lastname' - getting age of your contact with entered firstname and lastname
  - exit - ending search through age
- exit - ending work
