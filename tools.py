import string  # Удерживать CTRL + Left Click

# TODO: Использование string
POSSIBLE_CHARS: str = string.ascii_letters + string.digits + "_"


def check_password(text: str) -> str | bool:
    """
    Проверка пароля
    :param text: пароль пользователя
    :return: Сообщение - Пароль принят! если пароль прошел проверку
    True - Если пароль прошел проверку
    False - Если пароль не прошел проверку
    """
    errors: list[str] = []

    # [Проверка пароля] Пароль должен состоять только из латинских букв, цифр и
    # символа нижнего подчёркивания (_)
    for char in text:
        if char not in POSSIBLE_CHARS:
            errors.append("Пароль должен состоять только из латинских букв, "
                          "цифр и символа нижнего подчёркивания (_).")
            break
    # [Проверка пароля] Пароль должен начинаться с заглавной буквы
    if not text[0].isupper():
        errors.append("Пароль должен начинаться с заглавной буквы.")
    # [Проверка пароля] Пароль должен заканчиваться только латинской буквой или цифрой.
    elif text[-1] not in string.ascii_letters + string.digits:
        errors.append("Пароль должен заканчиваться только латинской буквой или цифрой.")
    # [Проверка пароля] Минимальная длина пароля — 12 символов, максимальная — 32 символа.
    elif len(text) < 12 or len(text) > 32:
        errors.append("Минимальная длина пароля — 12 символов, максимальная — 32 символа.")

    # Вывод ошибок на экран
    if errors:
        print("Пароль несоответствует требованиям!")
        for error in errors:
            print(error)
        return False
    else:
        print("Пароль принят!")
        return True


# Запись пароля в файл
def write_password(user_password):
    """
    Запись валидного пароля в файл
    :param user_password: Пользовательский пароль
    """
    valid_passwords = open("valid_passwords.txt", "a")
    valid_passwords.write(user_password + "\n")
    valid_passwords.close()