import sqlite3


def fill_table_user(cursor_work):
    for i in range(1, 11):
        cursor_work.execute("""
        INSERT INTO User(username, email, age, balance) 
        VALUES (?, ?, ?, ?)
        """, (f"User{i}", f"example{i}@gmail.com)", i*10, 1000))


def update_balance(cursor_work):
    cursor_work.execute("UPDATE User SET balance = ? WHERE id % 2 <> 0", (500,))


def delete_3(cursor_work):
    cursor_work.execute("DELETE FROM User WHERE (id+2) % 3 = 0")


if __name__ == '__main__':
    db = sqlite3.connect("not_telegram.db")
    cursor = db.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS User(id INTEGER PRIMARY KEY,
                                       username TEXT NOT NULL,
                                       email TEXT NOT NULL,
                                       age INTEGER,
                                       balance INTEGER NO NULL) 
                   """)

    fill_table_user(cursor)
    update_balance(cursor)
    delete_3(cursor)

    cursor.execute("SELECT * FROM User WHERE age<>60")
    users = cursor.fetchall()
    for user in users:
        print(f"Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}")
    db.commit()
    db.close()

