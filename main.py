import os
from crypto_pr1 import practical_work1_main
from crypto_pr6 import crypto_pr_main


def menu_bar():
    print("""
    [1]Практическая работа №1
    [2]Практическая работа №2""")

    practical_work_number = input("Выберите номер:\n")

    if practical_work_number == '1':
        try:
            print("Выбрана *Практическая работа №1*")
            practical_work1_main.main()
        except KeyboardInterrupt:
            print("Выход...")
            exit()
    if practical_work_number == '6':
        try:
            print("Выбрана *Практическая работа №2*")
            crypto_pr_main.main()
        except KeyboardInterrupt:
            print("Выход...")
            exit()


def main():
    print(f"""________________________________

    Привет, {os.getlogin()}!
    """)
    print("""________________________________
    
    [*] Создано Филипповым Л.А
    [*] Группа: БББО-08-18
________________________________""")

    menu_bar()


if __name__ == '__main__':
    main()
