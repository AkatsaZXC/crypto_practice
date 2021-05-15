def encryption():
    str_to_encrypt = input('Введите строку для шифрования: ')
    print("Ваша строка: ")
    print(str_to_encrypt)
    print()
    key = input("Введите ключ: ")
    print("Ваш ключ: ")
    print(key)
    print()

    # Шифрование
    encrypted_str = ""
    for i in str_to_encrypt:
        try:
            # Если ключ является символом
            encrypted_str += chr(ord(i) ^ ord(key))
        except TypeError:
            # Если ключ не символ
            encrypted_str += chr(ord(i) ^ int(key))

    print("Зашифрованне сообщение: ")
    print(encrypted_str)
    print()

    # Расшифрование
    str_to_encrypt = ""
    for j in encrypted_str:
        try:
            # Если ключ является символом
            str_to_encrypt += chr(ord(j) ^ ord(key))
        except TypeError:
            # Если ключ не символ
            str_to_encrypt += chr(ord(j) ^ int(key))

    print("Расшифрованное сообщение: ")
    print(str_to_encrypt)
    print()




def main():
    encryption()


if __name__ == '__main__':
    main()
