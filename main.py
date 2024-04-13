from telebot import types,telebot
from parsing import pogoda_in_taraz,pogoda_in_semey,pogoda_in_almaty,pogoda_in_aktau,pogoda_in_astana,pogoda_in_atyrau
from parsing import kurs_dollar,kurs_euro,kurs_rub,kurs_chy
import random
from parsing import news,last_news
import requests
bot = telebot.TeleBot(token='6179654095:AAGVixhDs2y77DpktKJNLZrAPyCtyh1fM30')

@bot.message_handler (commands= ['start1'])
def start(message):
    user_id = message.chat.id
    welcome_message = 'Приветствую, меня зовут Юджиро Хан а мой отец @amolav88! Чем могу помочь?\n'
    available_commands = '/start1 - Начать\n/helpp - Помощь\n/pogoda - Погода\n/game - Игры\n/spisok_Bokeihanova - Список класса\n/kurs - капитальный курс тенге'
    bot.send_message(user_id, welcome_message + available_commands)

@bot.message_handler(commands=['pogoda'])
def help(message):
    user_id = message.chat.id
    help_text = "Выберите действие:"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton ("погода в Алматы")
    button2 = types.KeyboardButton("погода в Семее")
    button3 = types.KeyboardButton ("погода в Атырау")
    button4 = types.KeyboardButton("погода в Астанe")
    button5 = types.KeyboardButton("погода в Актауе")
    button6 = types.KeyboardButton("погода в Таразе")
    button7 = types.KeyboardButton("/start1 - кнопка назад")
    markup.row(button1,button2)
    markup.row(button3,button4)
    markup.row(button5,button6)
    markup.row(button7)
    bot.send_message(user_id, help_text, reply_markup = markup)


@bot.message_handler(commands=['helpp'])
def help(message):
    user_id = message.chat.id
    help_text = "Выберите действие:"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton ("последние новости")
    button3 = types.KeyboardButton ("привет")
    markup.row(button1)
    markup.row(button3)
    bot.send_message(user_id, help_text, reply_markup = markup)

@bot.message_handler(commands=['game'])
def help(message):
    user_id = message.chat.id
    help_text = "Какая игра:"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton ("Рандомная цифра")
    button2 = types.KeyboardButton("Квест на тему Хэлуин")
    markup.row(button1)
    markup.row(button2)
    bot.send_message(user_id, help_text, reply_markup = markup)


@bot.message_handler(commands=['send_photo'])  # Обработчик команды /send_photo
def send_photo(message):
    # URL изображения
    photo_url = 'https://sun9-13.userapi.com/wJF6Rue1jFvQkY1Xkxlx-_-guyWl71lcj6CiXw/hrXnuppaUWs.jpg'
    # Загружаем изображение из интернета
    response = requests.get(photo_url, stream=True)
    response.raise_for_status()

    # Отправляем изображение в чат
    bot.send_photo(message.chat.id, response.raw)

@bot.message_handler (func = lambda message: True)
def text_message_handler (message):
    user_id = message.chat.id
    text = message.text
    if str(text).lower() == "привет":
        bot.send_message(user_id,"Привет!")
    if str(text) == "Рандомная цифра":
        bot.send_message(user_id,random.randint(1, 18))
        bot.send_message(user_id, "/start1 - кнопка назад")
    if str(text).lower() == "как дела?":
        bot.send_message(user_id,"нормально")
        bot.send_message(user_id, "/start1 - кнопка назад")
    if str(text) == "погода в Семее":
        bot.send_message(user_id, pogoda_in_semey())
    if str(text) == "погода в Алматы":
        bot.send_message(user_id, pogoda_in_almaty())
    if str(text) == "погода в Атырау":
        bot.send_message(user_id, pogoda_in_atyrau())
    if str(text) == "погода в Астанe":
        bot.send_message(user_id, pogoda_in_astana())
    if str(text) == "погода в Таразе":
        bot.send_message(user_id, pogoda_in_taraz())
    if str(text) == '/spisok_Bokeihanova':
        bot.send_message(user_id,"1)Нурали\n2)Темирлан\n3)Дана\n4)Дильназ\n5)Жанель\n6)Санжар\n7)Маргулан\n8)Жандос\n9)Акерке\n10)Ерали\n11)Жанасыл\n12)Али\n13)Ерасыл\n14)Байарыстан\n15)Амир\n16)Алибек")
    if str(text) == '/spisok_Bokeihanova@Y1urik_bot':
        bot.send_message(user_id,"1)Нурали\n2)Темирлан\n3)Дана\n4)Дильназ\n5)Жанель\n6)Санжар\n7)Маргулан\n8)Жандос\n9)Акерке\n10)Ерали\n11)Жанасыл\n12)Али\n13)Ерасыл\n14)Байарыстан\n15)Амир\n16)Алибек")
    if str(text) == "погода в Актауе":
        bot.send_message(user_id, pogoda_in_aktau())
    if str(text).lower() == "последние новости":
        bot.send_message(user_id, news())
        bot.send_message(user_id, "/start1 - кнопка назад")
    if str(text).lower() == "новости":
        bot.send_message(user_id, last_news())
        bot.send_message(user_id, "/start1 - кнопка назад")
    if str(text) == "/kurs":
        bot.send_message(user_id, kurs_euro())
        bot.send_message(user_id, kurs_dollar())
        bot.send_message(user_id, kurs_rub())
        bot.send_message(user_id, kurs_chy())
        bot.send_message(user_id, "/start1 - кнопка назад")
    if str(text) == "/kurs@Y1urik_bot":
        bot.send_message(user_id, kurs_euro())
        bot.send_message(user_id, kurs_dollar())
        bot.send_message(user_id, kurs_rub())k
        bot.send_message(user_id, kurs_chy())
        bot.send_message(user_id,"/start1 - кнопка назад" )

bot.polling (none_stop=True)