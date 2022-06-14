from datetime import date, datetime
from token import NEWLINE
from typing import List, Optional
from pydantic import BaseModel

class Category(BaseModel): #Этот класс Установливает как будет выглядет Json файл c добавлением новой категории.
    id: Optional[int]
    name: str
    class Config:
        orm_mode = True

# NEW
class Book(BaseModel): #Этот класс Установливает как будет выглядет Json файл c добавлением новой книги.
    id: Optional[int]
    title: str
    isbn: str
    pageCount: Optional[int]
    shortDescription: Optional[str]
    longDescription: Optional[str]
    publishedDate: Optional[datetime]
    class Config:
        orm_mode = True

class Author(BaseModel): #Этот класс Установливает как будет выглядет Json файл c добавлением нового автора.
    id: Optional[int]
    name: str
    class Config:
        orm_mode = True


    


