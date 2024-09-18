def send_email(message, recipient, sender="university.help@gmail.com"):
    list_valid = ["com", "ru", "net"]
    if recipient.find("@") == -1 or sender.find("@") == -1:
        res = f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.'
    elif recipient == sender:
        res = f"Нельзя отправить письмо самому себе!"
    elif not recipient.split(".")[-1] in list_valid:
        res = f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.'
    elif not sender.split(".")[-1] in list_valid:
        res = f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.'
    else:
        res = f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}."
        if sender != "university.help@gmail.com":
            res = "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! " + res
    print(res)

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')