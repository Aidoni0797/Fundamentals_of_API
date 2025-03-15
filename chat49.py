# прикольный код надо просто узнать как работать с кодом с умом

from telebot import types
import telebot

# Подставьте ваш токен вместо 'YOUR_TOKEN_HERE'
TOKEN = '...'

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)

# Отправка фотографии
@bot.message_handler(commands=['photo'])
def send_photo(message):
    photo = open('path/to/photo.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)

# Отправка видео
@bot.message_handler(commands=['video'])
def send_video(message):
    video = open('path/to/video.mp4', 'rb')
    bot.send_video(message.chat.id, video)

# Отправка аудио
@bot.message_handler(commands=['audio'])
def send_audio(message):
    audio = open('path/to/audio.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)

# Отправка документа
@bot.message_handler(commands=['document'])
def send_document(message):
    document = open('path/to/document.pdf', 'rb')
    bot.send_document(message.chat.id, document)

# Отправка сообщения с клавиатурой
@bot.message_handler(commands=['keyboard'])
def send_keyboard(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Кнопка 1')
    button2 = types.KeyboardButton('Кнопка 2')

    markup.add(button1, button2)
    bot.send_message(message.chat.id, 'Выбери кнопку:', reply_markup=markup)

# Обработка команды с использованием Inline-кнопок
@bot.message_handler(commands=['options'])
def options_command(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Вариант 1', callback_data='option1')
    button2 = types.InlineKeyboardButton('Вариант 2', callback_data='option2')

    markup.add(button1, button2)
    bot.send_message(message.chat.id, 'Выбери вариант:', reply_markup=markup)

# Обработка нажатий на Inline-кнопки
@bot.callback_query_handler(func=lambda call: True)
def handle_button_click(call):
    if call.data == 'option1':
        bot.answer_callback_query(call.id, 'Вы выбрали Вариант 1')
    elif call.data == 'option2':
        bot.answer_callback_query(call.id, 'Вы выбрали Вариант 2')

# Запуск бота
bot.polling(none_stop=True)