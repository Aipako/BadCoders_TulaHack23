from sqlalchemy import *
from sqlalchemy.orm import create_session
from sqlalchemy.schema import Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
import Good
import UserData


class DataBaseController:
    #Атрибуты класса

    #Конструктор класса

    def __init__(self):
        self.__sqlEngine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
        self.__sqlEngine.connect()
        self.__metadata = MetaData(bind=self.__sqlEngine)
        self.__connect_tables()
        self.__session = create_session(bind=self.__sqlEngine)

    #Ищем существующую базу данных

    def get_existing_db(self):
        pass

    #Подключаем таблицы

    def __connect_tables(self):
        self.__usersTable = Table('Users', self.__metadata, autoload=True)
        self.__goodsTable = Table('Goods', self.__metadata, autoload=True)

    def add_good_to_db(self, userId, good):
        good



