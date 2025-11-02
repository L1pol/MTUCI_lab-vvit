try:
    a = int(input('Выберите способ чтения 1 или 2: '))
    if a == 1:
        with open('Lab 3\example.txt', 'r') as file:
            content = file.read()
        print(content)

    elif a == 2:
        with open('Lab 3\example.txt', 'r') as file:
            for line in file:
                print(line)

    else:
        print('Ошибка!')
except FileNotFoundError:
    print( 'Ошибка: Файл не найден!')