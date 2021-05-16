import rsa


def encryption():
    # Генерация пары ключей
    (pubkey, privkey) = rsa.newkeys(2048)

    message_for_encryption = bytes(input("Введите сообщение для шифрования: "), encoding='utf-8')

    # Подписка сообщения цифровой подписью
    signature = rsa.sign(message_for_encryption, privkey, 'SHA-256')

    # Проверка цифровой подписи
    print(rsa.verify(message_for_encryption, signature, pubkey))


def main():
    encryption()


if __name__ == '__main__':
    main()
