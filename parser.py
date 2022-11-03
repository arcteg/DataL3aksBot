dbs = ["(ГИБДД Санкт-Петербург (2018-2019)", "Спрашивай.ру (2015)", "dns-shop.ru (2022)"]


def check_email(email):
    count = 0
    res = ""
    f = open("db/sprashivai.ru_emailpass.txt", "r", encoding="utf8", errors="ignore")
    for line in f.readlines():
        line = list(line.split(":"))
        if email == line[0]:
            count += 1
            res += dbs[1] + "\n"
    f.close()

    f = open("db/dns-shop-users.txt", "r", encoding="utf8", errors="ignore")
    for line in f.readlines():
        line = list(line.split(" "))
        if email == line[3]:
            count += 1
            res += dbs[2]
    f.close()

    if count > 0:
        return f"*❗Найдено совпадений — {count}:*" + "\n" + res
    else:
        return "*✅Вашего email нет в базах данных!*"


def check_phone(num):
    count = 0
    res = ""
    if num[0] == "+":
        num[0] = ""
    f = open("db/spb_18-19-part1.txt", "r", encoding="cp1251", errors="ignore")
    for line in f.readlines():

        line = list(line.split("|"))
        if num == line[2]:
            count += 1
            res += dbs[0] + "\n"
    f.close()

    f = open("db/spb_18-19-part2.txt", "r", encoding="cp1251", errors="ignore")
    for line in f.readlines():
        line = list(line.split("|"))
        if num == line[41]:
            count += 1
            res += dbs[0] + "\n"
    f.close()

    if count > 0:
        return f"*❗Найдено совпадений — {count}:*" + "\n" + res
    else:
        return "*✅Вашего телефонного номера нет в базах данных!*"


def check_auto(number):
    count = 0
    res = ""
    number = number.lower()
    f = open("db/spb_18-19-part1.txt", "r", encoding="cp1251", errors="ignore")
    for line in f.readlines():
        line = list(line.split("|"))
        if number == line[41]:
            f.close()
            count += 1
            res += dbs[0] + "\n"

    f.close()

    f = open("db/spb_18-19-part2.txt", "r", encoding="cp1251", errors="ignore")
    for line in f.readlines():
        line = list(line.split("|"))
        if number == line[2]:
            count += 1
            if "ГИБДД Санкт-Петербург (2018-2019)" not in res:
                res += dbs[0] + "\n"

    f.close()

    if count > 0:
        return f"*❗Найдено совпадений — {count}:*" + "\n" + res
    else:
        return "*✅Вашего автомобильного номера нет в базах данных!*"
