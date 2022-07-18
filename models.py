from datetime import datetime
from tokenize import Number
from click import DateTime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Numeric,DateTime
from sqlalchemy.orm import relationship

from database import Base


class Price(Base):
    __tablename__ = "price"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    url = Column(String)
    datetime = Column(DateTime)
    price = Column(String(64))
    price_int = Column(Numeric(10, 2))

    def __repr__(self):
        return f"{self.name} | {self.price}"


