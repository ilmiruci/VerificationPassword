import tools


def check_password() -> None:
    print("Программа проверки пароля\n"
          "Введите пароль и получите ответ\n")
    errors: list[str] = []

    text: str = input("Введите пароль: ")

    tools.is_possible_chars(text, errors)
    tools.is_first_char_upper(text, errors)
    tools.is_last_char_alpha_num(text, errors)
    tools.check_length(text, errors)

    if errors:
        print("Пароль несоответствует требованиям!")
        print(*errors, sep="\n")
    else:
        print("Пароль принят!")
        tools.write_password("Абвгед_234паыва")


if __name__ == "__main__":
    check_password()
