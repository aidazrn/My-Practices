from fastapi import FastAPI
from db import *

app = FastAPI()
create_table()


@app.post('/add-books/')
def create_book(book_name: str, publish_date: str, writer, price: float):
    insert_book(book_name, publish_date, writer, price)
    return {"message": "book added successfully"}

@app.get('/books/')
def get_book(id: int):
    book_data = books_data(id)
    if not book_data:
        return {"message":"no book found with the specfied ID"}
    return book_data