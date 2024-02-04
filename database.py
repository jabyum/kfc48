# импортируем библиотеки
import sqlite3
from datetime import datetime
# создаем подключение/файл
connection = sqlite3.connect("kfc.db")
# среда или переводчик
sql = connection.cursor()
# создаем таблицу users
sql.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER, name TEXT, phone_number TEXT, reg_date DATETIME);")
sql.execute("CREATE TABLE IF NOT EXISTS products (pr_id INTEGER PRIMARY KEY AUTOINCREMENT, pr_name TEXT, "
            "pr_price REAL, pr_quantity INTEGER, pr_des TEXT, pr_photo TEXT, reg_date DATETIME);")
sql.execute("CREATE TABLE IF NOT EXISTS cart (user_id INTEGER, pr_id INTEGER, pr_name TEXT, pr_count INTEGER, "
            "total_price REAL);")
def add_user(user_id, user_name, user_phone_number):
    # создаем подключение/файл
    connection = sqlite3.connect("kfc.db")
    # среда или переводчик
    sql = connection.cursor()
    # сохраняем данные из бота
    sql.execute("INSERT INTO users (user_id, name, phone_number, reg_date) VALUES (?, ?, ?, ?);",
                (user_id, user_name, user_phone_number, datetime.now()))
    connection.commit()
def get_users():
    connection = sqlite3.connect("kfc.db")
    sql = connection.cursor()
    # получение всех пользователей
    users = sql.execute("SELECT * FROM users;").fetchall()
    # передаем результат
    return users
def check_user(user_id):
    connection = sqlite3.connect("kfc.db")
    sql = connection.cursor()
    # проверяем есть ли пользователь в базе данных
    checker = sql.execute("SELECT user_id FROM users WHERE user_id = ?;", (user_id, )).fetchone()
    # если пользователь есть, то возвращаем True
    if checker:
        return True
    # если пользователя нет - False
    else:
        return False
# Работа со складом (продуктами)
# добавление продуктов на склад
def add_product(pr_name, pr_price, pr_quantity, pr_des, pr_photo):
    connection = sqlite3.connect("kfc.db")
    sql = connection.cursor()
    sql.execute("INSERT INTO products (pr_name, pr_price, pr_quantity, pr_des, pr_photo, reg_date) "
                "VALUES (?, ?, ?, ?, ?, ?);",
                (pr_name, pr_price, pr_quantity, pr_des, pr_photo, datetime.now()))
    connection.commit()
# получение информации о всех продуктах
def get_all_products():
    connection = sqlite3.connect("kfc.db")
    sql = connection.cursor()
    all_products = sql.execute("SELECT * FROM products").fetchall()
    return all_products
# информация для кнопок главного меню
def get_pr_id_name():
    connection = sqlite3.connect("kfc.db")
    sql = connection.cursor()
    get_name_id = sql.execute("SELECT pr_id, pr_name, pr_quantity FROM products").fetchall()
    actual_count = [(i[0], i[1]) for i in get_name_id if i[2]>0]
    return actual_count
# получение инфомрации о продукте по id
def get_exact_product(pr_id):
    connection = sqlite3.connect("kfc.db")
    sql = connection.cursor()
    get_exact_prod = sql.execute("SELECT pr_name, pr_price, pr_des, pr_photo FROM products WHERE pr_id=?;",
                                 (pr_id, )).fetchone()
    return get_exact_prod
# очистка склада
def delete_products():
    connection = sqlite3.connect("kfc.db")
    sql = connection.cursor()
    sql.execute("DELETE FROM products")
    connection.commit()
    return get_all_products()
# удаление конкретного продукта
def delete_exact_product(pr_id):
    connection = sqlite3.connect("kfc.db")
    sql = connection.cursor()
    sql.execute("DELETE FROM products WHERE pr_id=?;", (pr_id, ))
    connection.commit()
# изменения количества продукта
def change_quantity(pr_id, new_qauntity):
    connection = sqlite3.connect("kfc.db")
    sql = connection.cursor()
    sql.execute("UPDATE products SET pr_quantity=? WHERE pr_id=?;", (new_qauntity, pr_id))
    connection.commit()
# корзина
# добавить продукт в корзину
def add_to_cart(user_id, pr_id, pr_name, pr_count):
    connection = sqlite3.connect("kfc.db")
    sql = connection.cursor()
    total_price = pr_count * get_exact_product(pr_id)[1]
    sql.execute("INSERT INTO cart (user_id, pr_id, pr_name, pr_count, total_price);",
                (user_id, pr_id, pr_name, pr_count, total_price))
    connection.commit()
# удаление определенного продукта из корзины
def delete_exact_pr_from_cart(user_id, pr_id):
    connection = sqlite3.connect("kfc.db")
    sql = connection.cursor()
    sql.execute("DELETE * FROM cart WHERE user_id=? AND pr_id=?;", (user_id, pr_id))
    connection.commit()
# очистка всей корзины
def delete_user_cart(user_id):
    connection = sqlite3.connect("kfc.db")
    sql = connection.cursor()
    sql.execute("DELETE * FROM cart WHERE user_id=?;", (user_id, ))
    connection.commit()
# получение корзины пользователя
def get_user_cart(user_id):
    connection = sqlite3.connect("kfc.db")
    sql = connection.cursor()
    user_cart = sql.execute("SELECT pr_name, pr_count, total_price FROM cart "
                            "WHERE user_id=?;", (user_id, )).fetchall()
    return user_cart
