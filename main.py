import os
from crypto_pr1 import practical_work1_main
from crypto_pr6 import practical_work6_main
from crypto_pr7 import practical_work7_main


def menu_bar():
    print("""
    [1]Практическая работа №1
    [6]Практическая работа №6
    [7]Практическая работа №7""")

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
            print("Выбрана *Практическая работа №6*")
            practical_work6_main.main()
        except KeyboardInterrupt:
            print("Выход...")
            exit()
    if practical_work_number == '7':
        try:
            print("Выбрана *Практическая работа №7*")
            practical_work7_main.main()
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
