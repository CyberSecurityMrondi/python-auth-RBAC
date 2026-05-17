import time

log = 0
failed_aut = 0
users = [
    ["Kot", "admin", "admin"],
    ["Шут", "StayOut2026", "admin"],
    ["Stellar2026", "user123", "moderator"],
    ["Guest", "Guest", "user"],
    ["hacker", "password123", "banned"],
]
reports = []

print(
    "Система авторизации приветствует вас! Для продолжения выберите один из перечисленных вариантов."
)

while True:
    try:
        var = int(input("\nВыберите вариант: 1 - вход; 2 - регистрация; 3 - выход: "))
    except ValueError:
        print("Ошибка! Пожалуйста, введите число (1, 2 или 3).")
        continue

    if var == 3:
        print("Выход инициализируется")
        time.sleep(0.2)
        print("Выход... 20%")
        time.sleep(0.2)
        print("Выход... 40%")
        time.sleep(0.2)
        print("Выход выполнен успешно! Ждем вас снова!")
        break

    if var == 2:
        already_exists = False
        new_login = input("Придумайте логин: ")
        if new_login.lower() == "admin" or new_login.lower() == "root":
            print(
                "Логины 'admin' и 'root' зарезервированы системой! Пожалуйста, смените логин. "
            )
            continue
        new_password = input("Придумайте пароль: ")
        if len(new_password) < 6:
            print("Пароль слишком короткий! Попробуйте еще раз.")
            continue
        if new_login.lower() in new_password.lower():
            print("Нельзя использоавать логин в своем пароле! Попробуйте еще раз!")
            continue

        for user in users:
            if user[0] == new_login:
                already_exists = True
        if not already_exists:
            users.append([new_login, new_password, "user"])
            print("Регистрация успешна!")
            var = 1
        else:
            print("Данный логин уже занят. Попробуйте другой")

    if var == 1:
        attempts = 3
        while attempts > 0:
            login = input("Ваш логин: ").strip()

            current_role = None
            for u in users:
                if u[0] == login:
                    current_role = u[2]
                    break

            password = input("Ваш пароль: ")

            success_login = False
            for x in users:
                if x[0] == login and x[1] == password:
                    current_role = x[2]
                    success_login = True
                    break

            if success_login:
                print("Доступ разрешен! Ваш логин:", login)
                print(f"Роль: {current_role}")
                log += 1

                if current_role == "admin":
                    admin_key_cat = "KrasnodarCatBlack"
                    admin_key_shut = "StayOut123400"
                    admin_key_check = input("Введите код доступа (2FA): ")

                    access = False
                    if login == "Kot" and admin_key_check == admin_key_cat:
                        access = True
                    elif login == "Шут" and admin_key_check == admin_key_shut:
                        access = True

                    if access:
                        print("Доступ активирован. Загрузка...")
                        time.sleep(1)
                        print("-----АДМИН_ПАНЕЛЬ-----")
                        print("Список пользователей:", users)

                        change = input("Изменить роль? (да/нет): ")
                        if change.lower() == "да":
                            target = input("Логин юзера: ")
                            new_r = input("Новая роль (moderator/user/banned): ")
                            if new_r == "banned":
                                cause = input("Введите причину: ")

                            if new_r == "admin":
                                print("Запрещено назначать админов!")
                            else:
                                for u in users:
                                    if u[0] == target:
                                        u[2] = new_r
                                        print("Готово!")
                                        break

                        print("-----ОКНО РЕПОРТОВ-----")
                        if not reports:
                            print("Репортов пока нет")
                        else:
                            for r in reports:
                                print(f"От: {r[0]} | Суть: {r[1]}")
                    else:
                        print("Код доступа неверный!")
                elif current_role == "banned":
                    print("Связываемся с базой данных. Пожалуйста подождите...")
                    time.sleep(2)
                    print(
                        "Ошибка! Ваш аккаунт заблокирован по причине",
                        cause,
                        "Обратитесь к администрации сервиса.",
                    )
                    rep = input("Хотите отправить репорт? (да/нет): ")
                    if rep.lower() == "да":
                        text = input("Опишите проблему: ")
                        reports.append([login, text])
                        print(
                            "Заявка на обжалование блокировки отправлена! Администрация рассмотрит её."
                        )
                    break

                elif current_role == "moderator":
                    moder_key = "GrayCat"
                    moder_key_check = input("Введите код доступа: ")
                    if moder_key_check == moder_key:
                        print("Доступ модератора подтвержден! Загрузка панели...")
                        time.sleep(1)
                        print("-----ПАНЕЛЬ МОДЕРАТОРА-----")
                        for u in users:
                            print(f"Пользователь: {u[0]}")
                    else:
                        print("Код доступа неверный!")
                    print("Пользователей в сети:", len(users))

                elif current_role == "user":
                    print("Добро пожаловать! Ваша роль на сервере: user.")
                    choice = input("Хотите отправить репорт? (да/нет): ")
                    if choice.lower() == "да":
                        text = input("Опишите проблему: ")
                        reports.append([login, text])
                        print("Репорт отправлен! Администрация рассмотрит его.")
                break

            else:
                attempts -= 1
                if attempts > 0:
                    print("Неверный логин или пароль! Осталось попыток:", attempts)
                else:
                    print("Доступ воспрещен! Аккаунт заблокирован!")
                    for u in users:
                        if u[0] == login:
                            u[2] = "banned"
                            break
                    break
