dbs = ["<db names>"]


def check_email(email):
    count = 0
    res = ""
    f = open("<email db name>", "r", encoding="utf8", errors="ignore")
    for line in f.readlines():
        line = list(line.split(":"))
        if email == line[0]:
            count += 1
            res += dbs[1] + "\n"
    f.close()

    f = open("<email db2 name>", "r", encoding="utf8", errors="ignore")
    for line in f.readlines():
        line = list(line.split(" "))
        if email == line[3]:
            count += 1
            res += dbs[2]
    f.close()

    if count > 0:
        return f"*❗Найдено совпадений — {count}:*" + "\n" + res
    else:
        return "*✅Вашего email нет в БД!*"


def check_phone(num):
    count = 0
    res = ""
    if num[0] == "+":
        num[0] = ""
    f = open("<phone db name>", "r", encoding="cp1251", errors="ignore")
    for line in f.readlines():

        line = list(line.split("|"))
        if num == line[2]:
            count += 1
            res += dbs[0] + "\n"
    f.close()

    f = open("<phone db2 name>", "r", encoding="cp1251", errors="ignore")
    for line in f.readlines():
        line = list(line.split("|"))
        if num == line[41]:
            count += 1
            res += dbs[0] + "\n"
    f.close()

    if count > 0:
        return f"*❗Найдено совпадений — {count}:*" + "\n" + res
    else:
        return "*✅Вашего телефонного номера нет в БД!*"


def check_auto(number):
    count = 0
    res = ""
    number = number.lower()
    f = open("<auto db name>", "r", encoding="cp1251", errors="ignore")
    for line in f.readlines():
        line = list(line.split("|"))
        if number == line[41]:
            f.close()
            count += 1
            res += dbs[0] + "\n"

    f.close()

    f = open("<auto db2 name>", "r", encoding="cp1251", errors="ignore")
    for line in f.readlines():
        line = list(line.split("|"))
        if number == line[2]:
            count += 1
            res += dbs[0] + "\n"

    f.close()

    if count > 0:
        return f"*❗Найдено совпадений — {count}:*" + "\n" + res
    else:
        return "*✅Вашего автомобильного номера нет в БД!*"
