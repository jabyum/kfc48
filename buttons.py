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
def products_menu(actual_products):
    kb = types.InlineKeyboardMarkup(row_width=3)
    # создаем постоянные кнопки
    back = types.InlineKeyboardButton(text="Назад", callback_data="mm")

    # создаем динамичиские кнопки
    all_products = [types.InlineKeyboardButton(text=product[1], callback_data=product[0])
                    for product in actual_products]
    kb.add(*all_products)
    kb.row(back)
    return kb
def exact_product(current_amount=1, plus_or_minus=""):
    kb = types.InlineKeyboardMarkup(row_width=3)
    #создаем постоянные кнопки
    back = types.InlineKeyboardButton(text="Назад", callback_data="back")
    #создаем плюс
    plus = types.InlineKeyboardButton(text="➕", callback_data="plus")
    #создаем минус
    minus = types.InlineKeyboardButton(text="➖", callback_data="minus")
    #актуальное количество
    count = types.InlineKeyboardButton(text=f"{current_amount}", callback_data="none")
    # подтвердить
    add_to_cart = types.InlineKeyboardButton(text="Добавить в корзину", callback_data="to_cart")
    # прописываем логику
    if plus_or_minus == "plus":
        new_amount = current_amount + 1
        count = types.InlineKeyboardButton(text=f"{new_amount}", callback_data=str(new_amount))
    elif plus_or_minus == "minus":
        if current_amount > 1:
            new_amount = current_amount - 1
            count = types.InlineKeyboardButton(text=f"{new_amount}", callback_data=str(new_amount))
    kb.add(minus, count, plus)
    kb.row(add_to_cart)
    kb.row(back)
    return kb

def get_cart_kb():
    kb = types.InlineKeyboardMarkup(row_width=1)
    clear = types.InlineKeyboardButton("Очистить корзину", callback_data="clear_cart")
    order = types.InlineKeyboardButton("Оформить заказ", callback_data="order")
    back = types.InlineKeyboardButton("Назад", callback_data="mm")
    kb.add(clear, order, back)
    return kb
def get_location():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    location = types.KeyboardButton("Отправить локацию", request_location=True)
    kb.add(location)
    return kb