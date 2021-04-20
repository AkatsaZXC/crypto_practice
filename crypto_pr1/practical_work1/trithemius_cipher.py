def encryption():
    print("Исходный алфавит: ")
    #  Заполнения алфвавита из строки и проверка на длину каждой строки
    alphabet_list = []
    alphabet_str = "АБВГДЕЁЖЗИйКЛМНОПРСТУФХЦЧШЩЪЫьЭЮЯ-*#"
    for s in alphabet_str:
        alphabet_list.append(s)
    k = 0
    for s in alphabet_list:
        print(f"|{s}|", end=' ')
        k = k + 1
        if k == 6:
            print("\n")
            k = 0
    print()

    key_fraze = input("Введите ключевую фразу: ").upper()
    print("Ключевая фраза: ")
    print(key_fraze)
    print()
    key_fraze_list = list(key_fraze)

    #  Удаление лишних элементов из ключевой фразы
    sorted_key_fraze = list()
    for s in key_fraze_list:
        if s not in sorted_key_fraze:
            sorted_key_fraze.append(s)
    #  Дополнение элементами сортированного ключ.слова алфвавита
    for index, symbol in enumerate(sorted_key_fraze):
        alphabet_list.insert(index, symbol)

    #  Удаление всех повторяющихся элементов из списка
    new_alphabet_list = list()
    for s in alphabet_list:
        if s not in new_alphabet_list:
            new_alphabet_list.append(s)
    #  Вывод нового алфвавита
    print("Новый алфавит: \n")
    k = 0
    for s in new_alphabet_list:
        print(f"|{s}|", end=' ')
        k = k + 1
        if k == 6:
            print("\n")
            k = 0
    print()


def main():
    encryption()


if __name__ == '__main__':
    main()
