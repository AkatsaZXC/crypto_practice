import rsa


def encryption():
    # Генерация пары ключей
    (pubkey, privkey) = rsa.newkeys(2048)

    message_for_encryption = bytes(input("Введите сообщение для шифрования: "), encoding='utf-8')

    # Подписка сообщения цифровой подписью
    signature = rsa.sign(message_for_encryption, privkey, 'SHA-256')

    check = input("Желаете изменить сообщение?(Y/N): ").upper()
    if check == 'Y':
        print("Введите сообщение: ", end="")
        new_message = bytes(input(), encoding='utf-8')
        try:
            result = rsa.verify(new_message, signature, pubkey)
            print(result)
        except rsa.VerificationError:
            print("Ошибка верификации...")
    elif check == 'N':
        print("Проверка подписи: ")
        result = rsa.verify(message_for_encryption, signature, pubkey)
        print(result)
        print("Верификация успешна!")
    else:
        print("Выход...")
    # Проверка цифровой подписи
    # print(rsa.verify(message_for_encryption, signature, pubkey))


def main():
    encryption()


if __name__ == '__main__':
    main()
