from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()
engine = create_engine("postgresql://admin:admin1234@localhost:5436/integrations?client_encoding=utf8", echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
session = SessionLocal()


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


Base.metadata.create_all(bind=engine)
pan = User('yefersoncasti@gmail.com', 'Admin1234', 'yeferson', 'castiblanco', 987654321)
session.add(pan)
session.commit()
