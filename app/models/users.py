from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, func

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(500), unique=True, index=True)
    password = Column(String(500))
    name = Column(String(500))
    lastname = Column(String(500))
    document = Column(Integer)
    #
    def __init__(self, email: str, password: str, name: str, lastname: str, document: float):
        key = 'Admin1234'
        self.email = func.pgp_sym_encrypt(email, key)
        self.password = func.pgp_sym_encrypt(password, key)
        self.name = name
        self.lastname = lastname
        self.document = document
