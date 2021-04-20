def encryption():
    print("Исходная таблица: ")
    alphabet_list = [['А', 'Б', 'В', 'Г', 'Д', 'Е'],
                     ['Ё', 'Ж', 'З', 'И', 'Й', 'К'],
                     ['Л', 'М', 'Н', 'О', 'П', 'Р'],
                     ['С', 'Т', 'У', 'Ф', 'Х', 'Ц'],
                     ['Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь'],
                     ['Э', 'Ю', 'Я', '-', '-', '-']]
    print()
    #  Вывод алфавита в коносоль
    for i in range(len(alphabet_list)):
        for j in range(len(alphabet_list[i])):
            print(alphabet_list[i][j], end=' ')
        print()
    fraze = input("Напишите ключевое слово:\n").upper()
    fraze_list = list(fraze)
    print("Ваше ключевое слово: ", end=' ')
    print(fraze)

    #  Удаление повторяющихся символов в ключевом слове
    sorted_fraze = list()
    for s in fraze_list:
        if s not in sorted_fraze:
            sorted_fraze.append(s)
    '''Дополнение элементами сортированного ключ. слова исходного алфавита,
    удаля повторяющиеся буквы'''

    str_to_encrypt = input("Введите строку для шифрования: ").upper()
    print("Ваша строка", end=' ')


def main():
    encryption()


if __name__ == '__main__':
    main()
