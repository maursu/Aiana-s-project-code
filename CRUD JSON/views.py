import json

FILE_PATH = 'data.json'

def get_data():
    with open (FILE_PATH,'r+') as file:
        return json.load(file)

def post_data():
    
    ls = get_data()
    ls.append({
        'id': int(input('Введите id продукта: ')),
        'name': input('Введите название продукта: '),
        'price': input('Введите цену на продукт: ')
    })
    with open(FILE_PATH, 'w+') as file:
        json.dump(ls,file)
    return 'CREATED'

def update_data():
    data = get_data()
    id = int(input('Введите id продукта: '))
    update = list(filter(lambda x: x['id'] == id, data))
    if not update:
        return 'нет такого продукта!'
    index_ = data.index(update[0])
    data[index_]['name'] = input('Введите новое название продукта')
    data[index_]['price'] = input('Введите новую цену на продукт')
    with open(FILE_PATH, 'w+') as file:
        json.dump(data, file)
    return 'UPDATED'



def delete_data():
    data = get_data()
    id = int(input('Введите id продукта: '))
    delete = list(filter(lambda x: x['id'] == id, data))
    if not delete:
        return "Нет такого продукта"
    index_ = data.index(delete[0])
    data.pop(index_)
    json.dump(data, open(FILE_PATH, 'w'))
    
    return 'DELETED'

post_data()
