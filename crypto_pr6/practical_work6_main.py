import os
from crypto_pr6 import xor_cipher


def menu_bar():
    print("""
________________________________

    [1] Гаммирование или XOR-шифрование
    """)

    cipher_number = input("Выберите номер шифра:\n")

    if cipher_number == '1':
        try:
            xor_cipher.main()
        except KeyboardInterrupt:
            print("Выход...")
            exit()


def main():
    menu_bar()
