from views import *

print('Что вы хотите сделать? POST/DELETE/UPDATE/GET/EXIT')

while True:
    operation = input('Введите действие ').upper()
    if operation == 'GET':
        print(get_data())
    elif operation == 'POST':
        print(post_data())
    elif operation == 'UPDATE':
        print(update_data())
    elif operation == 'DELETE':
        print(delete_data())
    elif operation == 'EXIT':
        break
    else:
        print('Такой операции нет')
    
