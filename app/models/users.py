from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, index=True)
    password = Column(String(500))
    name = Column(String(15))
    lastname = Column(String(15))
    document = Column(Integer)

    def __init__(self, email: str, password: str, name: str, lastname: str, document: float):
        self.email = email
        self.password = password
        self.name = name
        self.lastname = lastname
        self.document = document
