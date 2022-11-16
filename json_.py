"""JSON"""

#json - (javaScript object Notation) - Единый текстовый формат хранения и передачи данных


# '{
#     "id": 1,
#     "autor": "john"
#     "post": Null
# }'


"""Сериализация -> перевод JSON формата в Python объект"""

# dump() -> метод записывает объект Python в файл в формате JSON
# dumps() -> метод записывает объект Python в строку в формате JSON

"""Десериализация -> перевод Python объекта в JSON"""

# load() -> считывает файл в формате JSON и переводит его в Python объект

# loads() -> считывает файл/текст в формате JSON

"""Различия между Python и JSON"""

# dict - object
# True False - true false
#'' "" - ""
#None - null


import json
"""встроеный модуль кодирования и декодирования данных в json"""

"""json.loads(text)"""


# person = '{"name":"John","age":25}'
# result = json.loads(person)
# result['name'] = 'Alice'

# with open('test.json', 'w+') as file:
#     person = '{"name":"John","age":25}'
#     file.write(person)
#     file.seek(0)
#     data = json.load(file)
#     print(data)



# with open('test.json', 'w+') as file:
#     person = '{"name":"John","age":25}'
#     json.dump(person, file)
#     file.seek(0)
#     data = file.read()
#     print(data)

# person = {'name': "John", "age":25}
# print(type(person))
# json_ = json.dumps(person)
# print(json_)
# print(type(json_))


"""файл CSV"""

# Comma Separated Values -> значения, разделенные запятой или запятыми
"""особый вид файла, который позволяет структурировать большие данные"""

# import csv

# with open('test.csv', 'w+') as file:
#     file.write('This is csv? not json')
#     file.seek(0)
#     read_ = csv.reader(file)
#     for row in read_:
#         print(','.join(row))
