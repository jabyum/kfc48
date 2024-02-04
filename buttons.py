# импорт библиотек
from telebot import types

def get_phone_number():
    # создаем пространство кнопки
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # создаем саму кнопку
    phone_number = types.KeyboardButton("Поделиться контактом", request_contact=True)
    # добавляем кнопку в пространство
    kb.add(phone_number)
    return kb

def main_menu():
    # создаем пространство и указываем количество кнопок в одной строчке
    kb = types.InlineKeyboardMarkup(row_width=1)
    # создаем сами кнопки
    products_menu = types.InlineKeyboardButton(text="Продукты", callback_data="products")
    cart_menu = types.InlineKeyboardButton(text="Корзина", callback_data="cart")
    feedback = types.InlineKeyboardButton(text="Оставить отзыв", callback_data="feedback")
    sup = types.InlineKeyboardButton(text="Тех.поддержка", callback_data="support")
    # добавляем кнопки в пространство
    kb.add(products_menu, cart_menu, feedback, sup)
    return kb



