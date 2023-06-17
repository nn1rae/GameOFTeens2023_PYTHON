import telebot
from telebot import types
import time


bot = telebot.TeleBot("TOKEN")  # BotFather Token

# List of available tariffs
tariffs = [
    {
        "atr": ["a", "b", "d", "f", "h", "j"],
        "name": "Вільний Лайф",
        "url": "https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/vilniy-life-2021/",
        "img": "img/001.png",
    },
    {
        "atr": ["a", "b", "d", "f", "h", "j"],
        "name": "Смарт Лайф",
        "url": "https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-life-2021/",
        "img": "img/002.png",
    },
    {
        "atr": ["a", "b", "c", "e", "h", "j"],
        "name": "Просто Лайф",
        "url": "https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/prosto-life-2021/",
        "img": "img/003.png",
    },
    {
        "atr": ["b", "d", "f", "h", "j"],
        "name": "Платінум Лайф",
        "url": "https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/platinum-life-2021/",
        "img": "img/004.png",
    },
    {
        "atr": ["a", "b", "c", "f", "h", "j"],
        "name": "Шкільний Лайф",
        "url": "https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/shkilniy/",
        "img": "img/005.png",
    },
    {
        "atr": ["a", "b", "c", "e", "g", "j"],
        "name": "Ґаджет Безпека",
        "url": "https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-bezpeka/",
        "img": "img/061.png",
    },
    {
        "atr": ["a", "b", "d", "f", "g", "i"],
        "name": "Ґаджет Смарт",
        "url": "https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-smart21/",
        "img": "img/062.png",
    },
    {
        "atr": ["b", "d", "e", "g", "j"],
        "name": "Ґаджет Планшет",
        "url": "https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-tab21/",
        "img": "img/063.png",
    },
    {
        "atr": ["b", "d", "e", "g", "j"],
        "name": "Ґаджет Роутер",
        "url": "https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-rout21/",
        "img": "img/064.png",
    },
    {
        "atr": ["a", "b", "d", "e", "g", "i"],
        "name": "Смарт Сім'я S",
        "url": "https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-family-s/",
        "img": "img/071.png",
    },
    {
        "atr": ["b", "d", "f", "g", "i"],
        "name": "Смарт Сім'я M",
        "url": "https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart_simja-m/",
        "img": "img/072.png",
    },
    {
        "atr": ["b", "d", "f", "g", "i"],
        "name": "Смарт Сім'я L",
        "url": "https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-family-l/",
        "img": "img/073.png",
    },
]


# Function to find all matching tariffs based on user preferences
def find_tariffs(tarifWish):
    global tariffs
    possibleTariffs = []
    for tariff in tariffs:
        if all(attr in tariff["atr"] for attr in tarifWish):
            possibleTariffs.append(tariff)
    return possibleTariffs


# Function to generate inline keyboard callback data
def gen_callback_data(data):
    keyboard = types.InlineKeyboardMarkup()
    for i in data:
        button = types.InlineKeyboardButton(i[0], callback_data=i[1])
        keyboard.add(button)
    return keyboard


# Handler for the /authors command
@bot.message_handler(commands=["authors"])
def info(messege):
    mes = """
    *Інформація по боту*
    Бот створений мовою Python 3.10.10;
    Бот був зроблений за крихту хліба;
    *____________________________*
    Версія *ALPHA 1.1*
    *____________________________*
    """
    bot.send_message(messege.chat.id, mes, parse_mode="Markdown")
    bot.send_photo(
        messege.from_user.id,
        photo=open("img/nn1rae.jpg", "rb"),
        caption="*nn1rae*\nГоловний інженер-програміст\n\n546F6D617465206D6974204B61666665653F",
        parse_mode="Markdown",
    )
    time.sleep(0.8)
    bot.send_photo(
        messege.from_user.id,
        photo=open("img/dokshyy.jpg", "rb"),
        caption="*dokshyy*\nРедактор-дизайнер\n\n"
        'Поки ви заробляєте дивани, вони сидять на мільйонах..."',
        parse_mode="Markdown",
    )
    time.sleep(0.8)
    bot.send_photo(
        messege.from_user.id,
        photo=open("img/dennys.jpg", "rb"),
        caption='*dennys*\nАналітик тарифних планів\n\n"Якщо життя повернеться до тебе дупою - засади йому"',
        parse_mode="Markdown",
    )
    time.sleep(0.8)
    bot.send_photo(
        messege.from_user.id,
        photo=open("img/nigggar.jpg", "rb"),
        caption='*niggar*\nТалісман\n\n"Не порівнюйте себе з іншими. Якщо ви робите це, ви ображаєте себе."',
        parse_mode="Markdown",
    )


# Handler for the /start command
@bot.message_handler(commands=["start"])
def info(message):
    markup = types.ReplyKeyboardMarkup()
    item1 = types.KeyboardButton("Підібрати оптимальний тариф")
    item2 = types.KeyboardButton("Створити свій ")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Привіт, Вас вітає lifecell!")
    time.sleep(0.8)
    bot.send_message(
        message.chat.id,
        "Вам підібрати оптимальний тариф чи Ви хочете створити свій унікальний тариф?",
        reply_markup=markup,
    )


# Handler for choosing the tariff
@bot.message_handler(content_types=["text"])
def text_input(message):
    if message.text == "Підібрати оптимальний тариф":
        bot.send_photo(
            message.from_user.id,
            photo=open("img/1.png", "rb"),
            caption="Чи є у Вас обмеження в бюджеті?",
            parse_mode="Markdown",
            reply_markup=gen_callback_data([["Так", "0a"], ["Ні", "0b"]]),
        )
    elif message.text == "Створити свій":
        text = "[Створити свій тариф](https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/handmade/)"
        bot.send_message(message.from_user.id, text, parse_mode="Markdown")


# Handler for callback queries
@bot.callback_query_handler(lambda query: query.data)
def call_back(data):
    historyOfAnswers = data.data[1:]
    msgRow = int(data.data[:1])
    match msgRow:
        case 0:
            bot.delete_message(data.message.chat.id, data.message.message_id)
            bot.send_photo(
                data.from_user.id,
                photo=open("img/1.png", "rb"),
                caption="Чи часто Ви користуєтеся інтернетом?",
                parse_mode="Markdown",
                reply_markup=gen_callback_data(
                    [
                        ["Так", str(msgRow + 1) + historyOfAnswers + "d"],
                        ["Ні", str(msgRow + 1) + historyOfAnswers + "c"],
                    ]
                ),
            )
        case 1:
            bot.delete_message(data.message.chat.id, data.message.message_id)
            if not find_tariffs(historyOfAnswers):
                bot.send_message(
                    data.from_user.id,
                    "На основі нашого опитування, самий підходящий(і) для Вас тариф(и):",
                )
                for tariff in find_tariffs(historyOfAnswers[:-1]):
                    bot.send_photo(
                        data.from_user.id,
                        photo=open(tariff["img"], "rb"),
                        caption="[{name}]({url})".format(
                            name=tariff["name"], url=tariff["url"]
                        ),
                        parse_mode="Markdown",
                    )
            elif len(find_tariffs(historyOfAnswers)) == 1:
                tariff = find_tariffs(historyOfAnswers)[0]
                bot.send_message(
                    data.from_user.id,
                    "На основі нашого опитування, самий підходящий для Вас тариф:",
                )
                bot.send_photo(
                    data.from_user.id,
                    photo=open(tariff["img"], "rb"),
                    caption="[{name}]({url})".format(
                        name=tariff["name"], url=tariff["url"]
                    ),
                    parse_mode="Markdown",
                )
            else:
                bot.send_photo(
                    data.from_user.id,
                    photo=open("img/1.png", "rb"),
                    caption="Наскільки часто Ви спілкуєтесь по телефону?",
                    parse_mode="Markdown",
                    reply_markup=gen_callback_data(
                        [
                            ["Доволі часто", str(msgRow + 1) + historyOfAnswers + "f"],
                            ["Не часто", str(msgRow + 1) + historyOfAnswers + "e"],
                        ]
                    ),
                )
        case 2:
            bot.delete_message(data.message.chat.id, data.message.message_id)
            if not find_tariffs(
                historyOfAnswers
            ):  # if no matching tariffs it will go back and send all avaleble
                bot.send_message(
                    data.from_user.id,
                    "На основі нашого опитування, самий підходящий(і) для Вас тариф(и):",
                )
                for tariff in find_tariffs(historyOfAnswers[:-1]):
                    bot.send_photo(
                        data.from_user.id,
                        photo=open(tariff["img"], "rb"),
                        caption="[{name}]({url})".format(
                            name=tariff["name"], url=tariff["url"]
                        ),
                        parse_mode="Markdown",
                    )
            elif (
                len(find_tariffs(historyOfAnswers)) == 1
            ):  # if only one tarif is avaleble there is no need to ask more questions and it will sdend the only tariff
                tariff = find_tariffs(historyOfAnswers)[0]
                bot.send_message(
                    data.from_user.id,
                    "На основі нашого опитування, самий підходящий для Вас тариф:",
                )
                bot.send_photo(
                    data.from_user.id,
                    photo=open(tariff["img"], "rb"),
                    caption="[{name}]({url})".format(
                        name=tariff["name"], url=tariff["url"]
                    ),
                    parse_mode="Markdown",
                )
            else:  # it continues to search for perfect match
                bot.send_photo(
                    data.from_user.id,
                    photo=open("img/1.png", "rb"),
                    caption="Чи цікавить Вас спільний тариф?",
                    parse_mode="Markdown",
                    reply_markup=gen_callback_data(
                        [
                            ["Так", str(msgRow + 1) + historyOfAnswers + "g"],
                            ["Ні", str(msgRow + 1) + historyOfAnswers + "h"],
                        ]
                    ),
                )
        case 3:
            bot.delete_message(data.message.chat.id, data.message.message_id)
            if not find_tariffs(historyOfAnswers):
                bot.send_message(
                    data.from_user.id,
                    "На основі нашого опитування, самий підходящий(і) для Вас тариф(и):",
                )
                for tariff in find_tariffs(historyOfAnswers[:-1]):
                    bot.send_photo(
                        data.from_user.id,
                        photo=open(tariff["img"], "rb"),
                        caption="[{name}]({url})".format(
                            name=tariff["name"], url=tariff["url"]
                        ),
                        parse_mode="Markdown",
                    )
            elif len(find_tariffs(historyOfAnswers)) == 1:
                tariff = find_tariffs(historyOfAnswers)[0]
                bot.send_message(
                    data.from_user.id,
                    "На основі нашого опитування, самий підходящий для Вас тариф:",
                )
                bot.send_photo(
                    data.from_user.id,
                    photo=open(tariff["img"], "rb"),
                    caption="[{name}]({url})".format(
                        name=tariff["name"], url=tariff["url"]
                    ),
                    parse_mode="Markdown",
                )
            else:
                bot.send_photo(
                    data.from_user.id,
                    photo=open("img/1.png", "rb"),
                    caption='Чи користуєтесь Ви послугою "СМС"?',
                    parse_mode="Markdown",
                    reply_markup=gen_callback_data(
                        [
                            ["Так", str(msgRow + 1) + historyOfAnswers + "i"],
                            ["Ні", str(msgRow + 1) + historyOfAnswers + "j"],
                        ]
                    ),
                )
        case 4:
            bot.delete_message(data.message.chat.id, data.message.message_id)
            if not find_tariffs(historyOfAnswers):
                bot.send_message(
                    data.from_user.id,
                    "На основі нашого опитування, самий підходящий(і) для Вас тариф(и):",
                )
                for tariff in find_tariffs(historyOfAnswers[:-1]):
                    bot.send_photo(
                        data.from_user.id,
                        photo=open(tariff["img"], "rb"),
                        caption="[{name}]({url})".format(
                            name=tariff["name"], url=tariff["url"]
                        ),
                        parse_mode="Markdown",
                    )
            elif len(find_tariffs(historyOfAnswers)) == 1:
                tariff = find_tariffs(historyOfAnswers)[0]
                bot.send_message(
                    data.from_user.id,
                    "На основі нашого опитування, самий підходящий для Вас тариф:",
                )
                bot.send_photo(
                    data.from_user.id,
                    photo=open(tariff["img"], "rb"),
                    caption="[{name}]({url})".format(
                        name=tariff["name"], url=tariff["url"]
                    ),
                    parse_mode="Markdown",
                )
            else:
                bot.send_message(
                    data.from_user.id,
                    "На основі нашого опитування, самий підходящі для Вас тарифи:",
                )
                for tariff in find_tariffs(historyOfAnswers):
                    bot.send_photo(
                        data.from_user.id,
                        photo=open(tariff["img"], "rb"),
                        caption="[{name}]({url})".format(
                            name=tariff["name"], url=tariff["url"]
                        ),
                        parse_mode="Markdown",
                    )
        case _:
            pass


bot.polling(none_stop=True)
