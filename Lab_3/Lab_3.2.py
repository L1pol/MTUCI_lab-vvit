
choice = int(input('Выберите (1)создать новый файл или (2)запись в уже имеющийся: '))
if choice == 1:
    a = input('Введите текст: ')
    with open('Lab_3\\user_input.txt', 'w') as file:
        file.write(a)
elif choice == 2:
    b = input('Введите текст: ')
    with open('Lab_3\\user_input.txt', 'a') as file:
        file.write(f"\n{b}")
else:
    print('Ошибка!')