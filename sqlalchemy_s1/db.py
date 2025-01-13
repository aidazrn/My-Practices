import sqlite3

def create_table():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        book_name TEXT,
        publish_data TEXT,
        writer TEXT,
        price FLOAT)"""
    )
    connection.commit()
    connection.close()

def insert_book(book_name, publish_data, writer, price):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO books (book_name, publish_data, writer, price) VALUE (?,?,?,?)",(book_name, publish_data, writer, price))
    connection.commit()
    connection.close()


def books_data(id):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books WHERE id = ?", (id,))
    books = cursor.fetchall()
    connection.close()
    return books