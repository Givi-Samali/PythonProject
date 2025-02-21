import os
import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()


def create():
    os.system("clear")
    cur.execute("CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)")
    conn.commit()


def lists():
    os.system("clear")
    lst = cur.execute("SELECT * FROM users").fetchall()
    for i in lst: print(*i)


def add():
    os.system("clear")
    name = input("Name - ")
    cur.execute("INSERT INTO users (name) VALUES (?)", (name,))
    conn.commit()
    print("Ok")


def update():
    os.system("clear")
    idd = input("Ввод id - ")
    new_name = input("Ввод нового значения - ")
    cur.execute(f"UPDATE users SET name = '{new_name}' WHERE id = {idd}")
    conn.commit()
    print("Ok")


def dell():
    os.system("clear")
    idd = input("id для удаления - ")
    cur.execute(f"DELETE FROM users WHERE id = {idd}")
    conn.commit()


com = ""


def main(com):
    os.system("clear")
    while not "exit" in com:
        com = input(">>")
        if "help" in com:
            print("create\nlists\nadd\nupdate\ndel")
        elif com == "create":
            create()
        elif com == "lists":
            lists()
        elif com == "add":
            add()
        elif com == "update":
            update()
        elif com == "del":
            dell()


main(com)
