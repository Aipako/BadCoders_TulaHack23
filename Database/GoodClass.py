from sqlalchemy import *
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Good(Base):
    __tablename__ = "Goods"

    UserId = Column(Integer, primary_key=True, autoincrement=False, nullable=False)
    Url = Column(String, nullable=False)
    Price = Column(Integer)
    MedianPrice = Column(Integer)
