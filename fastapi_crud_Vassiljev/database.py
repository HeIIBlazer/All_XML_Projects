from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Это код нужен для подключения к базе данный MySQL.

user = 'root'
password = ''
host = 'localhost'
port = 3306
database = 'library_db'

SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# autocommit - Это значит, что при успешном выполнении запроса изменения немедленно сохраняются в базу данных, а откат становится невозможным.
# autoflush - заставляет вывод записываться в файл.
# engine - создает подключение к базе данных

Base = declarative_base()