import os
from practical_work1 import slogan_cipher


def menu_bar():
    print("""
________________________________
    
    [1] Лозунговый шифр
    """)

    cipher_number = input("Выберите номер шифра:\n")

    if cipher_number == '1':
        try:
            slogan_cipher.main()
        except KeyboardInterrupt:
            print("Выход...")
            exit()


def main():
    menu_bar()
