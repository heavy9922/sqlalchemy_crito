from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.users import Base

app = FastAPI()
engine = create_engine("postgresql://admin:admin1234@localhost:5436/integrations?client_encoding=utf8", echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = SessionLocal()

Base.metadata.create_all(bind=engine)

