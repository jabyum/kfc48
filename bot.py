# импорт библиотек
import telebot
import database
import buttons
from telebot import types
# создаём объект бота
bot = telebot.TeleBot("6731412102:AAHWWPjIJVmRhlfenFRDLOufLasvNBGcoHY")
# создаем временную базу
users = {}
# database.add_product("Чизбургер3", 20000.0, 0, "Лучший чизбургер2", "https://bkmenu.ru/files/2021/06/chizburger-menu-bk.png")

# обработчик команды /start
@bot.message_handler(commands=["start"])
def start(message):
    # сохраняем id пользователя
    user_id = message.from_user.id
    # проверяем наличие пользователя в базе данных
    checker = database.check_user(user_id)
    # если пользователь есть в бд открываем ему меню
    if checker == True:
        bot.send_message(user_id, "Главное меню", reply_markup=buttons.main_menu())
    # если пользователя нет в бд, начинаем регистрацию
    elif checker == False:
        # отправляем ответ на команду старт
        bot.send_message(user_id, "Добро пожаловать в бота KFC-test.\n"
                                  "Начнём регистрацию. Введите своё имя")
        # переход на этап регистрации
        bot.register_next_step_handler(message, registration)
def registration(message):
    user_id = message.from_user.id
    name = message.text
    # просим отправить номер и прикрепляем кнопку
    bot.send_message(user_id, "Отправьте свой номер телефона", reply_markup=buttons.get_phone_number())
    # переход на следующий этап получения номер и сохраняем имя
    bot.register_next_step_handler(message, get_number, name)
def get_number(message, name):
    user_id = message.from_user.id
    # проверяем в каком формате отправлен номер
    #если через кнопку
    if message.contact:
        phone_number = message.contact.phone_number
        bot.send_message(user_id, "Вы успешно зарегистрировались", reply_markup=types.ReplyKeyboardRemove())
        database.add_user(user_id=user_id, user_name=name, user_phone_number=phone_number)
        print(database.get_users())
    # если номер записан вручную возвращаем его в эту же функцию
    else:
        bot.send_message(user_id, "Отправьте свой номер через кнопку")
        bot.register_next_step_handler(message, get_number, name)


@bot.callback_query_handler(lambda call: call.data in ["products", "cart", "feedback"])
def for_calls(call):
    user_id = call.message.chat.id
    if call.data == "products":
        actual_product = database.get_pr_id_name()
        bot.send_message(user_id, "Доступные бургеры", reply_markup=buttons.products_menu(actual_product))
    elif call.data == "cart":
        pass
    elif call.data == "feedback":
        bot.send_message(user_id, "Напишите ваш отзыв")
        bot.register_next_step_handler(call.message, feedback_fc)

def feedback_fc(message):
    user_id = message.from_user.id
    bot.send_message(-1001954411455, f"{message.text}\n"
                                     f"Юзер пользователя: {user_id}")
@bot.callback_query_handler(lambda call: int(call.data) in database.get_all_id())
def calls_for_products(call):
    user_id = call.message.chat.id
    product = database.get_exact_product(1)
    users[user_id] = {"pr_id": call.data, "pr_count": 1}

    bot.send_photo(user_id, photo=product[3], caption=f"{product[0]}\n"
                          f"Цена:{product[1]}\n"
                          f"Описание: {product[2]}\n"
                          f"Выберите количество:", reply_markup=buttons.exact_product())

bot.infinity_polling()

