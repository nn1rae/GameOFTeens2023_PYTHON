import telebot
from telebot import types
import time


bot = telebot.TeleBot("TOKEN")

tarifs = [{"atr": ["a","d","f","h","j"], "name": "Вільний Лайф", "url" : "https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/vilniy-life-2021/"}, 
    {"atr": ["a","d","f","h","j"], "name": "Смарт Лайф", "url" : "https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-life-2021/"},
    {"atr": ["a","c","e","h","j"], "name": "Просто Лайф", "url" : "https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/prosto-life-2021/"},
    {"atr": ["b","d","f","h","j"], "name": "Платінум Лай", "url" : "https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/platinum-life-2021/"},
    {"atr": ["a","c","f","h","j"], "name": "Шкільний Лайф", "url" : "https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/shkilniy/"},
    {"atr": ["a","c","e","h","j"], "name": "Ґаджет Безпека", "url" : "https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-bezpeka/"},
    {"atr": ["a","d","f","h","i"], "name": "Ґаджет Смарт", "url" : "https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-smart21/"},
    {"atr": ["b","d","e","h","j"], "name": "Ґаджет Планшет", "url" : "https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-tab21/"},
    {"atr": ["b","d","e","h","j"], "name": "Ґаджет Роутер", "url" : "https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-rout21/"},
    {"atr": ["a","d","e","g","i"], "name": "Смарт Сім'я S", "url" : "https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-family-s/"},
    {"atr": ["b","d","f", "g","i"], "name": "Смарт Сім'я M", "url" : "https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart_simja-m/"},
    {"atr": ["b","d","f","g","i"], "name": "Смарт Сім'я L", "url" : "https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-family-l/"}]
    
def find_tarif(tarifWish):
    global tarifs
    max_matches = 0
    best_tarif = []
    tarifWishList = [char for char in tarifWish]
    if "g" in tarifWish:
        group_tarifs_only = [tarif for tarif in tarifs if "g" in tarif["atr"]]
        for tarif in group_tarifs_only:
            matches = len(set(tarifWishList) & set(tarif["atr"]))
            if matches > max_matches:
                max_matches = matches
                best_tarif = tarif
    else:
        for tarif in tarifs:
            matches = len(set(tarifWishList) & set(tarif["atr"]))
            if matches > max_matches:
                max_matches = matches
                best_tarif = tarif

    return best_tarif


def gen_callback_data(data):
    keyboard = types.InlineKeyboardMarkup()
    for i in data:
        button = types.InlineKeyboardButton(i[0], callback_data=i[1])
        keyboard.add(button)
    return keyboard
    
@bot.message_handler(commands=["start"])
def info(message):
    markup = types.ReplyKeyboardMarkup()
    item1 = types.KeyboardButton("Підібрати оптимальний тариф")
    item2 = types.KeyboardButton("Створити свій ")
    markup.add(item1,item2)
    bot.send_message(message.chat.id, "Привіт, Вас вітає lifecell!")
    time.sleep(0.8)
    bot.send_message(message.chat.id, "Вам підібрати оптимальний тариф чи Ви хочете створити свій унікальний тариф?", reply_markup=markup)

    
    
    
@bot.message_handler(content_types=["text"])
def text_input(message):
    if message.text == "Підібрати оптимальний тариф":
        bot.send_photo(message.from_user.id,photo=open("img/1.png", 'rb') ,caption="Чи є у Вас обмеження в бюджеті?",parse_mode = "Markdown", reply_markup=gen_callback_data([["Так","0a"], ["Ні","0b"]]))
    elif message.text == "Створити свій":
        text = "[Створити свій тариф](https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/handmade/)"
        bot.send_message(message.from_user.id, text, parse_mode='Markdown')



    
@bot.callback_query_handler(lambda query: query.data)
def call_back(data):
    historyOfAnswers = data.data[1:]
    msgRow = int(data.data[:1])
    match msgRow:
        case 0:
            bot.delete_message(data.message.chat.id,data.message.message_id)
            bot.send_photo(data.from_user.id,photo=open("img/1.png", 'rb') ,caption="Чи часто Ви користуєтеся інтернетом?",parse_mode = "Markdown", reply_markup=gen_callback_data([["Так", str(msgRow + 1) + historyOfAnswers + "d"], ["Ні", str(msgRow + 1) + historyOfAnswers + "c"]]))
        case 1:
            bot.delete_message(data.message.chat.id,data.message.message_id)
            bot.send_photo(data.from_user.id,photo=open("img/1.png", 'rb') ,caption="Наскільки часто Ви спілкуєтесь по телефону?",parse_mode = "Markdown", reply_markup=gen_callback_data([["Доволі часто", str(msgRow + 1) + historyOfAnswers + "f"], ["Не часто", str(msgRow + 1) + historyOfAnswers + "e"]]))
        case 2:
            bot.delete_message(data.message.chat.id,data.message.message_id)
            bot.send_photo(data.from_user.id,photo=open("img/1.png", 'rb') ,caption="Чи цікавить Вас спільний тариф?",parse_mode = "Markdown", reply_markup=gen_callback_data([["Так", str(msgRow + 1) + historyOfAnswers + "g"], ["Ні", str(msgRow + 1) + historyOfAnswers + "h"]]))
        case 3:
            bot.delete_message(data.message.chat.id,data.message.message_id)
            bot.send_photo(data.from_user.id,photo=open("img/1.png", 'rb') ,caption='Чи користуєтесь Ви послугою "СМС"?',parse_mode = "Markdown", reply_markup=gen_callback_data([["Так", str(msgRow + 1) + historyOfAnswers + "i"], ["Ні", str(msgRow + 1) + historyOfAnswers + "j"]]))
        case 4:
            bot.delete_message(data.message.chat.id,data.message.message_id)
            tarif = find_tarif(historyOfAnswers)
            bot.send_message(data.from_user.id,"На основі мого опитування, самий підходящий для Вас тариф: [{name}]({url})".format(name=tarif["name"],url=tarif["url"]),parse_mode = "Markdown")
        case _:
            pass
            
    
    
bot.polling(none_stop=True)
