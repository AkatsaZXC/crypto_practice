import rsa
import random

# Генерация рандомной длины ключа
random_key_size_list = [128, 256, 512, 1024, 2048, 4096]
random_key_size = random.choice(random_key_size_list)
# Генерация пары ключей
(pubkey, privkey) = rsa.newkeys(random_key_size)

def auth():
    info_to_check = pubkey
    print(pubkey)


def main():
    auth()


if __name__ == '__main__':
    main()
