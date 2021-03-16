# Создать эмуляцию системы входа и регистрации для пользователей.
# При запуске программы, пользователя должно спросить проходил ли он
# регистрацию на нашем ресурсе, если да, тогда предложить ему ввести
# логин и пароль от его учетной записи.
# Если данные верны вывести сообщение об успешном входе в систему, если нет
# тогда сообщить об этом.
#############################################
# Если пользователь не регистрировался на ресурсе, тогда спросить не желает
# ли он пройти регистрацию.
# Если желает, взять от него необходимые данные и вывести об успешной
# регистрации, если не желает регистрироватся - пожелать удачи.
# Данные о зарегестрированных пользователях хранить в файле 'users.txt',
# по желанию можете создать файл для логирования событий регистрации и входа.
import datetime

zapros = input("Вітаємо на нашому ресурсі! Якщо ви зареєстровані напишить ("
               "Y) інакше (N): ").upper()

with open('users.txt', 'r+', encoding='utf-8') as usfile, \
     open('loguser.txt', 'a+', encoding='utf-8') as logfile:

    logpas = str(usfile.readlines())
    now_datetime = datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S")

    if zapros == 'Y':
        login_user = input("Введіть свій логін: ")
        pass_user = input("Введіть свій пароль: ")
        if f"{login_user}:{pass_user}" in logpas:
            print(f"Вітаємо {login_user} на нашому ресурсі.")
            logfile.write(f"{now_datetime} /{login_user}/-- вхід у ресурс\n")
        else:
            print("Невірно введений логін або пароль!")
            logfile.write(f"{now_datetime} /{login_user}/-- невірний "
                          f"логін або пароль\n")
    elif zapros == 'N':
        zapreg = input("Вітаємо! Бажаєте зареєструватися на нашому ресурсі ("
        "введіть (Y), якщо ні то (N): ").upper()
        if zapreg == 'Y':
            login_new = input("Введіть логін: ")
            pass_new = input("Введіть пароль: ")
            if f"{login_new}:{pass_new}" not in logpas:
                usfile.writelines(f"{login_new}:{pass_new}\n")
                print(f"Вітаємо {login_new} на нашому ресурсі.")
                logfile.write(f"{now_datetime} /{login_new}/-- нова "
                              f"реєстрація у ресурсі\n")
            else:
                print("Введений логін або пароль вже існує. Спробуйте ще!")
                logfile.write(f"{now_datetime} /-- спроба зареєструватися "
                              f"під існуючим логіном /{login_new}/\n")
        else:
            print("Дуже прикро! Всього Вам найкращого!")
            logfile.write(f"{now_datetime} /-- користувач відхилив "
                          f"реєстрацію у ресурсі\n")
