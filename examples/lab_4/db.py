"""
Реализуете механизмы работы с базой пользователей в этом модуле.
Примеры функции описаны ниже.
Вы спокойно можете изменять их, добавлять новые.
Главное - чтобы модуль работал так, как необходимо вашей программе.
"""


def create_new_user_db() -> bool:
    """
    Создание новой базы. Служебная функция.
    Возвращает:
        true - если операция была выполнена успешно;
        false - если не смог создать новую базу.

        Можно так же реализовать возвращение не true/false,
        а кода результата/ошибки.

        Или реализовать их через исключения.
    """
    pass


def insert(user: str, password: bytes, user_dir: str, enc_key: bytes) -> bool:
    """
    Добавить нового пользователя

    user: логин пользователя
    password: хэш от пароля
    user_dir: директория пользователя
    enc_key: зашифрованный ключ
    Возвращает:
        true - если операция была выполнена успешно;
        false - если не смог добавить пользователя.

        Можно так же реализовать возвращение не true/false,
        а кода результата/ошибки.

        Или реализовать их через исключения.
    """
    pass


def select(user: str):
    """
    Получить информацию о существующем пользователе

    user: логин пользователя
    Возвращает:
        информацию о пользователе, если пользователь с таким именем существует;
        None - если не смог найти пользователя.

        Можно реализовать генерацию исключений для проверок.
    """
    pass


def update(user: str, enc_key: bytes) -> bool:
    """
    Обновить информацию о существующем пользователе

    user: логин пользователя
    enc_key - новый зашифрованный ключ
    Возвращает:
        true - если операция была выполнена успешно;
        false - если не смог изменить информацию пользователя.

        Можно так же реализовать возвращение не true/false,
        а кода результата/ошибки.

        Или реализовать их через исключения.
    """
    pass


def delete(user: str) -> bool:
    """
    Удалить информацию о существующем пользователе

    user: логин пользователя
    Возвращает:
        true - если операция была выполнена успешно;
        false - если не смог удалить информацию пользователя.

        Можно так же реализовать возвращение не true/false,
        а кода результата/ошибки.

        Или реализовать их через исключения.
    """
    pass
