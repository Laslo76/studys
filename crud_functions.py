import sqlite3


def initiate_db():
    with sqlite3.connect("shop.db") as db:
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Products (id INTEGER PRIMARY KEY, title TEXT NOT NULL, description TEXT, img TEXT, price INTEGER NOT NULL)")
        db.commit()


def generate_products():

    with sqlite3.connect("shop.db") as db:
        products = []
        for i in range(1, 5):
            products.append((f"Продукт {i}", f"Описание {i}", f"product{i}.jpg", i * 100))

        cursor = db.cursor()
        cursor.executemany("INSERT INTO Products(title, description, img, price) VALUES (?, ?, ?, ?) ", products)
        db.commit()


def get_all_products():
    with sqlite3.connect("shop.db") as db:
        cursor = db.cursor()
        cursor.execute("""
        SELECT * FROM Products
        """)
    return cursor.fetchall()


if __name__ == '__main__':
    initiate_db()
    generate_products()