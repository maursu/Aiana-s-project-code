def sum_file(a,b, filename = 'sum.txt'):
    result = a + b
    with open(filename, 'w') as file:
        file.write(str(result))

def read_sum(filename='sum.txt'):
    with open(filename, 'r') as file:
        print(file.read())
