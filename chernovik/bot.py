# импортируем библиотеку телебот,
# предварительно скачав её через терминал pip install telebot
import telebot
from telebot import types
# Создаем объект нашего бота (мозг бота)
bot = telebot.TeleBot("6731412102:AAHWWPjIJVmRhlfenFRDLOufLasvNBGcoHY")
# создаём кнопку "переводчик"
def knopka():
    # создаем пространство для кнопки
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # создаем кнопки
    knopka_perevodchik = types.KeyboardButton("Переводчик")
    knopka_otmena = types.KeyboardButton("Отмена")
    # вставляем кнопку в пространство
    kb.add(knopka_perevodchik, knopka_otmena)
    # возвращаем пространство с кнопками
    return kb
# декоратор для команды /start
@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "Добро прожаловать!", reply_markup=knopka())
# декоратор для текста
@bot.message_handler(content_types=["text"])
def texting(message):
    user_id = message.from_user.id
    text = message.text
    if text.lower() == "переводчик":
        bot.send_message(user_id, "Введите слово для перевода")
        bot.register_next_step_handler(message, perevod_slova)
    else:
        bot.send_message(user_id, "Я вас не понимаю")
# декоратор для реагирования на фотографии отправленные пользователем
def perevod_slova(message):
    user_id = message.from_user.id
    slovo = message.text
    bot.send_message(user_id, f"Рандомный перевод слова {slovo}")
    bot.register_next_step_handler(message, perevod_slova2, slovo)
def perevod_slova2(message, slovo):
    user_id = message.from_user.id
    bot.send_message(user_id, slovo)

@bot.message_handler(content_types=["photo"])
def send_photo(message):
    #получаем айди пользователя
    user_id = message.from_user.id
    # сохраняем url фотографии
    photo = "https://www.myphone.kg/files/media/22/22799.webp"
    #отправляем фото пользователю
    bot.send_photo(user_id, photo, caption="Это телефон")
#запускаем бесконечный цикл работы бота
bot.infinity_polling()
