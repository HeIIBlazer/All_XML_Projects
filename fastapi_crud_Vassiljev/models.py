from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base

class Category(Base): #Этот класс считывает информацию из таблицы Category 
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)

    books = relationship('Book', secondary='bookcategories', back_populates='categories')

class Book(Base): #Этот класс считывает информацию из таблицы Book 
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True)
    isbn = Column(String(20), index=True)
    pageCount = Column(Integer)
    shortDescription = Column(String(255))
    longDescription = Column(String(3000))
    publishedDate = Column(DateTime)
    
    categories = relationship('Category', secondary='bookcategories', back_populates='books')
    authors = relationship('Author', secondary='bookauthors', back_populates='books')

class Author(Base): #Этот класс считывает информацию из таблицы Author
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)

    books = relationship('Book', secondary='bookauthors', back_populates='authors')

class BookAuthors(Base): #Этот класс считывает информацию из таблицы BookCategory
    __tablename__ = "bookauthors"

    id = Column(Integer, primary_key=True, index=True)
    BookId = Column(Integer, ForeignKey('books.id'))
    AuthorId = Column(Integer, ForeignKey('authors.id'))
    
class BookCategory(Base): #Этот класс считывает информацию из таблицы BookCategory
    __tablename__ = "bookcategories"

    id = Column(Integer, primary_key=True, index=True)
    BookId = Column(Integer, ForeignKey('books.id'))
    CategoryId = Column(Integer, ForeignKey('categories.id'))

