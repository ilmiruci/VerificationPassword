import string

POSSIBLE_CHARS: str = string.ascii_letters + string.digits + "_"


def is_possible_chars(password: str, errors: list[str]) -> bool:
    """
    Пароль должен состоять только из латинских букв, цифр и
    символа нижнего подчёркивания (_).

    :param password: Пароль.
    :param errors: Список ошибок.
    """
    for char in password:
        if char not in POSSIBLE_CHARS:
            errors.append("Пароль должен состоять только из латинских букв, "
                          "цифр и символа нижнего подчёркивания (_).")
            return False
    return True


def is_first_char_upper(password: str, errors: list[str]) -> bool:
    """
    Пароль должен начинаться с заглавной буквы.

    :param password:
    :param errors:
    """
    if password[0] not in string.ascii_uppercase:
        errors.append("Пароль должен начинаться с заглавной буквы.")
        return False
    return True


def is_last_char_alpha_num(password: str, errors: list[str]) -> bool:
    if password[-1] not in string.ascii_letters + string.digits:
        errors.append("Пароль должен заканчиваться только латинской буквой или цифрой.")
        return False
    return True


def check_length(password: str, errors: list[str]) -> bool:
    min_length, max_length = 12, 32

    if not (min_length <= len(password) <= max_length):
        errors.append(
            f"Минимальная длина пароля — {min_length} "
            f"Максимальная длина пароля — {max_length}"
        )
        return False
    return True


def write_password(password: str) -> None:
    """
    Запись валидного пароля в файл.
    :param password: Пользовательский пароль
    """
    with open("valid_passwords.txt", mode="a", encoding="UTF-8") as file:
        file.write(password + "\n")
