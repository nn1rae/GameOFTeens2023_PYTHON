import telebot
from telebot import types
import time


bot = telebot.TeleBot("TOKEN")

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
        bot.send_photo(message.from_user.id,photo=open("img/1.jpg", 'rb') ,caption="Вам потрібен самостійний чи спільний тариф?",parse_mode = "Markdown", reply_markup=gen_callback_data([["Самостійний","0"], ["Спільний","1"]]))
    elif message.text == "Створити свій":
        text = "[Створити свій тариф](https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/handmade/)"
        bot.send_message(message.from_user.id, text, parse_mode='Markdown')



    
@bot.callback_query_handler(lambda query: query.data)
def call_back(data):
    historyOfAnswers = data.data
    if historyOfAnswers == "0":
        bot.delete_message(data.message.chat.id,data.message.message_id)
        bot.send_photo(data.from_user.id,photo=open("img/1.jpg", 'rb') ,caption="Вас цікавить «Тарифна підписка» чи безліміт на соціальні мережі?",parse_mode = "Markdown", reply_markup=gen_callback_data([["Jaja Naturlisch", historyOfAnswers + "1"], ["Nien", historyOfAnswers + "1"]]))
    else:
       pass
    
    
bot.polling(none_stop=True)