from itertools import cycle


def encryption():
    alphabet_str = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    key_fraze = input("Введите ключевую фразу: ").upper()
    print("Ключевая фраза: ")
    print(key_fraze)
    print()

    str_to_encrypt = input("Введите строку для шифрования: ").upper()
    print("Ваша строка: ")
    print(str_to_encrypt)
    print()

    output = ""
    key_fraze *= len(str_to_encrypt) // len(key_fraze) + 1
    for index, symbol in enumerate(str_to_encrypt):
        temp = ord(symbol) + ord(key_fraze[index])
        output += chr(temp % 33 + ord('А'))
    print("Зашифрованная фраза: ")
    print(output)
    print()


def main():
    encryption()


if __name__ == '__main__':
    main()
