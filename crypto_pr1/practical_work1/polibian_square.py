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
        if len(alphabet_str) < 36:
            print("Введите не менее 36 символов")
            exit()
        alphabet_str = alphabet_str[:36].upper()
        alphabet_list = list(alphabet_str)
        print("Ваш алфавит:")
        for s in alphabet_list:
            print(f"{s}", end='')
        print()

        #  Создание словаря с ключами для шифрования
        alphabet_dict = {}
        keys = [11, 12, 13, 14, 15, 16, 21, 22, 23, 24, 25, 26, 31, 32, 33, 34, 35, 36, 41, 42, 43, 44, 45, 46, 51, 52,
                53, 54, 55, 56, 61, 62, 63, 64, 65, 66]
        #  Заполнение словаря ключами из keys и элементами из alphabet_list
        i = 0
        for k in keys:
            alphabet_dict[k] = alphabet_list[i]
            i = i + 1
        print()

        fraze = input("Введите фразу для шифрования")



    elif result == 'N':
        pass
    else:
        print('Выход')
        exit()


def main():
    encryption()


if __name__ == '__main__':
    main()
