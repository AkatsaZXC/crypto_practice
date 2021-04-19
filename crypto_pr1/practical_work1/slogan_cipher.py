def encryption():
    slogan = input("Выберите слоган:\n")
    slogan = slogan.upper()
    slogan_list = list(slogan)
    print("Ваш слоган:")
    print(slogan)
    print("Заполнение таблицы...")

    alphabet_list = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т',
                     'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
    for symbol in alphabet_list:
        print(f"|{symbol}|", end=" ")

    print('')

    #  Удаление лишних элементов из слогана
    sorted_slogan = list()
    for symbol in slogan_list:
        if symbol not in sorted_slogan:
            sorted_slogan.append(symbol)

    new_alphabet = list(alphabet_list)

    #  Дополнение элементами сортированного слогана нового списка
    for index, symbol in enumerate(sorted_slogan):
        new_alphabet.insert(index, symbol)

    symbols_to_delete = len(sorted_slogan)
    #  Удаление хвоста списка, который равен количеству символов в слогане
    i = 0
    while i < symbols_to_delete:
        new_alphabet.pop()
        i = i + 1

    for symbol in new_alphabet:
        print(f"|{symbol}|", end=" ")

    print('')
    str_to_encrypt = input("Введите строку для шифрования: ")
    str_to_encrypt = str_to_encrypt.upper()
    str_to_encrypt_list = list(str_to_encrypt)
    print("Ваша строка:")
    print(str_to_encrypt)

    #  Получение индексов символов, которые совпадают с символами из начального алфавита
    index_list = list()
    for symbol in str_to_encrypt_list:
        if symbol in alphabet_list:
            index_list.append(alphabet_list.index(symbol))

    #  Замена символов начального алфавита символами измененного, замена происходит по индексу
    print("Зашифрованное послание: ")
    for index in index_list:
        print(f"{new_alphabet[index]}")


def main():
    encryption()


if __name__ == '__main__':
    main()
