import tools


def main():
    print("Программа проверки пароля\n"
          "Введите пароль и получите ответ\n")


    user_password = input("Введите пароль: ")

    # Записываем пароль в файл если пароль прошел проверку
    if tools.check_password(user_password):
        tools.write_password(user_password)


if __name__ == "__main__":
    main()
