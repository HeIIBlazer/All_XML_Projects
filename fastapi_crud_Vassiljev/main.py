from fastapi import FastAPI
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

app = FastAPI()

@app.get("/") # Позволяет выводит на страницу сайта с текстом {"message":"Hello World"}.
async def root():
    return {"message": "Hello World"}


def get_db(): #Это функция, которая подключает к базе данных в MySQL.
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/categories/") # Позволяет выводит на страницу сайта Данные из таблицы Category.
def read_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)

@app.post("/categories/", response_model=schemas.Category) # Позволяет выводит на страницу добавление в таблицу Category.
def add_category(category: schemas.Category, db: Session = Depends(get_db)):
    return crud.create_category(db, category)

@app.delete("/categories/delete/{category_id}") # Позволяет удалять категорию.
def delete_category(category_id: int, db: Session = Depends(get_db)):
    return crud.delete_author(db,category_id)

# NEW BOOKS

@app.get("/books/") # Позволяет выводит на страницу сайта данные из таблицы Books.
def read_books(db: Session = Depends(get_db)):
    return crud.get_books(db)

@app.post("/books/", response_model=schemas.Book) # Позволяет выводит на страницу добавление в таблицу Books.
def add_Book(book: schemas.Book, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

@app.delete("/books/delete/{book_id}") # Позволяет удалять книгу.
def delete_book(book_id: int, db: Session = Depends(get_db)):
    return crud.delete_book(db,book_id)

# NEW AUTHORS

@app.get("/authors/") # Позволяет выводит на страницу сайта Данные из таблицы Authors.
def read_authors(db: Session = Depends(get_db)):
    return crud.get_authors(db)

@app.post("/authors/", response_model=schemas.Author) # Позволяет выводит на страницу добавление в таблицу Authors.
def add_Author(author: schemas.Author, db: Session = Depends(get_db)):
    return crud.create_book(db, author)

@app.delete("/authors/delete/{author_id}") # Позволяет удалять автора.
def delete_author(author_id: int, db: Session = Depends(get_db)):
    return crud.delete_author(db,author_id)