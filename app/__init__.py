from fastapi import FastAPI
from sqlalchemy import create_engine, func, LargeBinary
from sqlalchemy.orm import sessionmaker
from app.models.users import Base, User
from sqlalchemy.dialects.postgresql import BYTEA
app = FastAPI()
engine = create_engine("postgresql://admin:admin1234@localhost:5436/integrations?client_encoding=utf8", echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = SessionLocal()

Base.metadata.create_all(bind=engine)
new_user = User('yeferson@example.com', 'Admin1234', 'yeferson', 'castiblanco', 1023456890)
session.add(new_user)
session.commit()
key = 'Admin1234'
document = 1023456890
decrypted_email = session.query(func.pgp_sym_decrypt(User.email.cast(BYTEA), 'Admin1234')).all()
print(decrypted_email, 'XD')