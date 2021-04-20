def encryption():
    square_list = [['*', 1, 2, 3, 4, 5, 6],
                   [1, 'А', 'Б', 'В', 'Г', 'Д', 'Е'],
                   [2, 'Ё', 'Ж', 'З', 'И', 'Й', 'К'],
                   [3, 'Л', 'М', 'Н', 'О', 'П', 'Р'],
                   [4, 'С', 'Т', 'У', 'Ф', 'Х', 'Ц'],
                   [5, 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь'],
                   [6, 'Э', 'Ю', 'Я', '.', '!', '-'],
                   ]
    print("Исходный квадрат: ")
    print()

    #  Вывод квадрата в консоль
    for i in range(len(square_list)):
        for j in range(len(square_list[i])):
            print(square_list[i][j], end=' ')
        print()

    print("Желаете заполнить квадрат своим алфавитом?[Y/N]")
    result = input()
    result = result.upper()

    if result == 'Y':
        alphabet_str = input("Введите алфавит:\n")
        #  Отрезать часть строки, если она больше 36
        alphabet_str = alphabet_str[:36].upper()
        alphabet_list = list(alphabet_str)
        print("Ваш алфавит:")
        for s in alphabet_list:
            print(f"{s}", end='')
        print()
        print("Новый квадрат: ")

    elif result == 'N':
        pass
    else:
        print('Выход')
        exit()


def main():
    encryption()


if __name__ == '__main__':
    main()
