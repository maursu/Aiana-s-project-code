"""Работа с файлами в питоне"""

#open(путь_до_файла, режим) -> функция, которая позволяет открыть файл и работать с ним.

# file = open('/home/Desctop/.../.../test.py') - абсолютный путь
# file = open('test.txt') # относительный путь


"""Режимы"""

# 1. r(read) -> Открывает файл для чтения каретка будет находиться в начале файла при его открытии. Это режим по умолчанию, если такого файла нет, то произойдет ошибка

# file = open('test.txt','r') 

# 2. w(write) -> Открывает файл для записи. Перезаписывает файл (сначала все удалаяет потом записывает). позволяет создать файл, если такого еще нет.

# file = open('test2.txt', 'w')

#3. a(append) -> Открывает файл для добавления. Указатель находится в конце файла. Создаст файл, если такого файла еще нет

# file = open('test.txt','a')

#4. x(exclusive) -> Создает уникальный файл.

#5. t(text) -> Открывает файл в текстовом виде. Считается режимом по умолчанию.

#6. b(binary) -> открывает файл в бинарном виде
#rb - чтение в бинарном виде
#wb - запись в бинарном виде
#ab - дозапись в бинарном виде

# 7. + -> Открывает файл как в режиме чтения, так и в режиме записи

#w+ , r+ ...

"""У РЕЖИМОВ ЕСТЬ МЕТОДЫ!!!"""


"""МЕТОДЫ РЕЖИМА 'r' """

#1.read() -> если не указать параметр, то чтение будет от начала файла и до конца -> str
#2. readline() -> метод считывает одну строку за раз

#3. realines() -> считывает все строки и сохраняет в переменной списка -> list

# file = open('test.txt', 'r')

# data = file.read()

# print(data)

# file.close()

# file.tell() -> возвращает индекс, где назодится указатель

# file.seek(int) -> Перемещает указатель на указанный int

# f = open('test.txt', 'r')
# print(f.readline())
# print('====================')
# print(f.tell())
# f.seek(0)
# print(f.read(10))
# print(f.close())


# file = open('test.txt','r')

# data = file.readline()
# data2 = file.readline(3)
# print(data+data2)

# file.close()

# f = open('test.txt', 'r')
# for line in f:
#     print(line)
# f.close()

# f = open('test.txt', 'r')

# print(f.readlines())

# f.close()


"""Методы режима 'w' """

#1. write('string') # любые данные для записи должны передваться в формате строки
#2. writelines(list)

# f = open('test2.txt', 'w')

# f.write('hello')
# f.writelines(['asdfas','asdfasdljhweoi','aslkf']) можно передвать строки тюплы дикты, в случае диктов запишет только ключ
# f. close()

# try:
#     file = open('test.txt', 'w')
#     file.write('hello world')
# finally:
#     file.close()


"""Контекстный менеджер - открывает файл и при любом раскладе файл будет закрыт"""


# with open('twst.txt', 'r') as f:
#     ....


# with open('test2.txt', 'w') as file:
#     file.write('Hello with open')


# with open('test2.txt', 'w') as f:
#     f.writelines(['This is str\n','Hello\n','world'])

"""r+, w+, a+"""


# with open('test.txt', 'r+') as f:
#     f.write('r+ mode')
#     data = f.readlines()
#     print(data)


# with open('test.txt', 'w+') as file:
#     file.write('w+ mode')
#     file.seek(0)
#     data = file.read()

#     print(data)


# with open ("test.txt", 'a+') as file:
#     file.write(' a mode')
#     file.seek(0)
#     data = file.readlines()
#     print(data)


""" x+ -> Открывае файл в режиме записи и чтения"""


# with open('test3.txt', 'x+') as f:
#     print(f) 
#     f.write('New file')
#     f.seek(0)
#     print(f.readline())


# with open('task5.txt', 'r') as f:
#     minimum = min([int(i) for i in f])
#     f.seek(0)
#     maximum = max([int(i) for i in f])

# with open('task6.txt', 'w+') as file:
#     file.write(str(minimum)+'-'+str(maximum))
#     file.seek(0)
#     print(file.read())



# def longest_words(filename: str):
#     with open(filename, 'r') as file:
#         data = []
#         for i in file:
#             data.extend(i.split())
#         len_max = max([len(i) for i in data])
#         words = list(filter(lambda e: len(e) == len_max, data))
#         if len(words) == 1:
#             print(words[0])
#         else:
#             print(words)



# longest_words('article.txt')