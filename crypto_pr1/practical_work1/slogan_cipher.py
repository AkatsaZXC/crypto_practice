def cipher():
    slogan = input("Выберите слоган:\n")
    slogan_list = list(slogan)
    print("Ваш слоган:\n")
    print(slogan)
    print("Заполнение таблицы...")

    alphabit_list = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т',
                     'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
    for symbol in alphabit_list:
        print(f"|{symbol}|", end=" ")

    print(' ')

    sorted_slogan = list()
    for s in slogan_list:
        if s not in sorted_slogan:
            sorted_slogan.append(s)
    print(sorted_slogan)


def main():
    cipher()


if __name__ == '__main__':
    main()
