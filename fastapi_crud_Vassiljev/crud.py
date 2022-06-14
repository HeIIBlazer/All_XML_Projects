from database import SessionLocal, engine
from sqlalchemy.orm import Session
import models
import schemas

def get_category_by_id(db: Session, category_id: int): #Это функция, которая выберает категорию по ее ID.
    return db.query(models.Category).get(category_id)

def get_categories(db:Session): #Это функция, которая выберает все категории.
    return db.query(models.Category).all()

def get_book_by_id(db: Session, book_id: int): #Это функция, которая выберает книгу по ее ID.
    return db.query(models.Book).get(book_id)

def get_author_by_id(db: Session, author_id: int): #Это функция, которая выберает книгу по ее ID.
    return db.query(models.Author).get(author_id)

def get_book_by_title(db: Session, title: str): #Эт функция, которая выберает книгу по ее названию.
    return db.query(models.Book).filter(models.Book.title == title).first()

def get_books(db: Session, skip: int = 0, limit: int = 10): #Это функция, которая выберает все книги.
    return db.query(models.Book).offset(skip).limit(limit).all()

def create_category(db: Session, category: schemas.Category): #Это функция, которая Создает новую категорию.
    print(category.name)
    new_category = models.Category(name = category.name)
    db.add(new_category)
    db.commit()
    return new_category

# NEW FUNCTIONS Books

def create_book(db: Session, book: schemas.Book): #Это функция, которая создает новую книгу.
    print(book.title)
    new_book = models.Book(title = book.title, isbn = book.isbn, pageCount = book.pageCount, shortDescription = book.shortDescription, longDescription = book.longDescription,publishedDate = book.publishedDate)
    db.add(new_book)
    db.commit()
    return new_book

# NEW FUNCTIONS Authors

def get_authors_by_id(db: Session, author_id: int): #Это функция, которая выберает автора по ее ID.
    return db.query(models.Author).get(author_id)

def get_authors(db:Session): #Это функция, которая выберает всех авторов.
    return db.query(models.Author).all()

def create_author(db: Session, author: schemas.Author): #Это функция, которая создает нового автора.
    print(author.name)
    new_author = models.Author(name = author.name)
    db.add(new_author)
    db.commit()
    return new_author

def delete_author(db: Session, id): #Это функция, удаляет выброного автора.
    try:
        db.delete(get_author_by_id(db,id))
        db.commit()
        return "Succesfully deleted"
    except:
        return "NOT DELETED"

def delete_category(db: Session, id): #Это функция, удаляет выброного категорию.
    try:
        db.delete(get_category_by_id(db,id))
        db.commit()
        return "Succesfully deleted"
    except:
        return "NOT DELETED"

def delete_book(db: Session, id): #Это функция, удаляет выброную книгу.
    try:
        db.delete(get_book_by_id(db,id))
        db.commit()
        return "Succesfully deleted"
    except:
        return "NOT DELETED"






