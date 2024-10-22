import sqlite3


db_name = "shop_user.db"

def initiate_db():
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Products (id INTEGER PRIMARY KEY, title TEXT NOT NULL, description TEXT, img TEXT, price INTEGER NOT NULL)")

        cursor.execute("CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY, username TEXT NOT NULL, email TEXT NOT NULL, age INTEGER NOT NULL, balance INTEGER NOT NULL)")

        db.commit()


def generate_products():

    with sqlite3.connect(db_name) as db:
        products = []
        for i in range(1, 5):
            products.append((f"Продукт {i}", f"Описание {i}", f"product{i}.jpg", i * 100))

        cursor = db.cursor()
        cursor.executemany("INSERT INTO Products(title, description, img, price) VALUES (?, ?, ?, ?) ", products)
        db.commit()


def get_all_products():
    result = None
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Products")
        result = cursor.fetchall()
    return result


def is_include(username):
    result = False
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        query = f"SELECT * FROM Users WHERE username = '{username}'"
        cursor.execute(query)
        print()
        result = len(cursor.fetchall()) > 0
    return result


def add_user(username, email, age, balance=1000):
    if not is_include(username):
        with sqlite3.connect(db_name) as db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO Users(username, email, age, balance)  VALUES (?, ?, ?, ?)",
                           (username, email, age, balance))
            db.commit()

if __name__ == '__main__':
    initiate_db()
    #generate_products()
    #add_user('test', 'test@mail.ru', 27)
    #print(is_include('jon'))
