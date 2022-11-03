import telebot
import re
import parser

bot = telebot.TeleBot("TOKEN")
regex_email = re.compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
regex_phone = re.compile(r"(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$")
regex_auto = re.compile(r"^(([АВЕКМНОРСТУХ]\d{3}(?<!000)[АВЕКМНОРСТУХ]{1,2})(\d{2,3})|(\d{4}(?<!0000)[АВЕКМНОРСТУХ]{2})(\d{2})|(\d{3}(?<!000)(C?D|[ТНМВКЕ])\d{3}(?<!000))(\d{2}(?<!00))|([ТСК][АВЕКМНОРСТУХ]{2}\d{3}(?<!000))(\d{2})|([АВЕКМНОРСТУХ]{2}\d{3}(?<!000)[АВЕКМНОРСТУХ])(\d{2})|([АВЕКМНОРСТУХ]\d{4}(?<!0000))(\d{2})|(\d{3}(?<!000)[АВЕКМНОРСТУХ])(\d{2})|(\d{4}(?<!0000)[АВЕКМНОРСТУХ])(\d{2})|([АВЕКМНОРСТУХ]{2}\d{4}(?<!0000))(\d{2})|([АВЕКМНОРСТУХ]{2}\d{3}(?<!000))(\d{2,3})|(^Т[АВЕКМНОРСТУХ]{2}\d{3}(?<!000)\d{2,3}))")


@bot.message_handler(commands=['start'])
def get_start_messages(message):
    bot.send_message(message.chat.id, "*Бот принимает следующие форматы запросов:*\n"
                                      "✉ Email: `petrov_1991@mail.ru`\n📱 Телефон: `73842673895`\n 🚗 Номер авто: "
                                      "`В432ДМ777`", parse_mode="Markdown")


@bot.message_handler(commands=['stats'])
def get_stats_messages(message):
    bot.send_message(message.chat.id, f"*Статистика бота:*\n📊 Подключено баз: `{len(parser.dbs)}`\n📄 Количество "
                                      f"строк: `54 116 449`\n"
                                      "🗓 Последнее обновление: `30.09.2022`", parse_mode='Markdown')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, "👀 Сканирую базы данных...")
    bot.send_chat_action(message.chat.id, 'typing')
    if re.fullmatch(regex_email, message.text):
        bot.send_message(message.chat.id, text=parser.check_email(message.text), parse_mode='Markdown')
    elif re.fullmatch(regex_phone, message.text):
        bot.send_message(message.chat.id, text=parser.check_phone(message.text), parse_mode='Markdown')
    elif re.fullmatch(regex_auto, message.text):
        bot.send_message(message.chat.id, text=parser.check_auto(message.text), parse_mode='Markdown')
    else:
        bot.send_message(message.chat.id, "*⚠Ошибка! Проверьте введённые данные и повторите запрос!*", parse_mode=
        'Markdown')


bot.infinity_polling()
