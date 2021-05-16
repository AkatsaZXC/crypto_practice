import os
from crypto_pr7 import digital_sign


def menu_bar():
    print("""
________________________________

    [1] ЭЦП на RSA
    """)

    cipher_number = input("Выберите номер шифра:\n")

    if cipher_number == '1':
        try:
            digital_sign.main()
        except KeyboardInterrupt:
            print("Выход...")
            exit()


def main():
    menu_bar()
