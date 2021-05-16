from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from pathlib import Path
import os

path_to_ds_file = f"/home/{os.getlogin()}/ds_file.txt"


def encryption():
    if os.path.exists(path_to_ds_file):
        pass
    else:
        file = 'ds_file.txt'
        path = f"/home/{os.getlogin()}/"
        with open(os.path.join(path, file), 'w') as fp:
            pass
    # Генерация ключа RSA
    key = RSA.generate(2048)
    # Получение хэша файла
    hash = SHA256.new()
    with open(path_to_ds_file, "rb") as f:
        for i in iter(lambda: f.read(4096), b""):
            hash.update(i)
    # Подписка хэша
    signature = pkcs1_15.new(key).sign(hash)

    # Получение открытого ключа из закрытого
    pub_key = key.public_key()

    # # Пересылаете пользователю файл, публичный ключ и подпись
    # # На стороне пользователя заново вычисляете хэш файла (опущено) и сверяете подпись
    # pkcs1_15.new(pubkey).verify(h, signature)
    #
    # # Отличающийся хэш не должен проходить проверку
    # pkcs1_15.new(pubkey).verify(SHA256.new(b'test'), signature)  # raise ValueError("Invalid signature")

def main():
    encryption()


if __name__ == '__main__':
    main()
