from crypto_pr9 import auth_rsa


def menu_bar():
    print("""
    ________________________________

        [1] Аутентификация на основе RSA
        """)
    cipher_number = input("Выберите номер: \n")

    if cipher_number == '1':
        try:
            if __name__ == '__main__':
                auth_rsa.main()
        except KeyboardInterrupt:
            print("Выход...")
            exit()


def main():
    menu_bar()
