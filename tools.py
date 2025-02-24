import string  # Удерживать CTRL + Left Click

# TODO: Использование string
POSSIBLE_CHARS: str = string.ascii_letters + string.digits + "_"

print(POSSIBLE_CHARS)


def check_password(text: str) -> None:
    errors: list[str] = []

    # Пароль должен начинаться с заглавной буквы
    if not text[0].isupper():
        errors.append("Пароль должен начинаться с заглавной буквы.")

    # Пароль должен заканчиваться только латинской буквой или цифрой.

    for char in text:
        if char not in POSSIBLE_CHARS:
            print("Пароль должен состоять только из латинских букв, "
                  "цифр и символа нижнего подчёркивания (_).")
            break

    for error in errors:
        print(error)
