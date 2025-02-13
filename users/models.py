from datetime import datetime

from sqlalchemy import Column, Integer, String, Enum, Date
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    gender = Column(Enum('male', 'female', 'other', name='gender'), nullable=False)
    password = Column(String, nullable=False)
    registration_date = Column(Date, nullable=False, default=datetime.today())
    email = Column(String, nullable=False, unique=True)

