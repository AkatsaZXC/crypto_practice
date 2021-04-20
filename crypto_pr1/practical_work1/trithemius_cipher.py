def encryption():
    print("Исходный алфавит: ")
    alphabet_list = []
    alphabet_str = "АБВГДЕЁЖЗИйКЛМНОПРСТУФХЦЧШЩЪЫьЭЮЯ---"
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


def main():
    encryption()


if __name__ == '__main__':
    main()
