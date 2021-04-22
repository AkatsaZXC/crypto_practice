import os
from crypto_pr6 import covert_multilateral_computing


def menu_bar():
    print("""
________________________________

    [1] Тайные многосторонние вычисления
    """)

    cipher_number = input("Выберите номер шифра:\n")

    if cipher_number == '1':
        try:
            covert_multilateral_computing.main()
        except KeyboardInterrupt:
            print("Выход...")
            exit()
def main():
    menu_bar()
