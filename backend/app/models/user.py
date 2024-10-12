from app.db.base import Base
from sqlalchemy import Column, Integer, Index, String


class User(Base):
    __tablename__: "users"
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(100))
    lastname = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String)
    # username = Column(String, unique=True, index=True)
    # email = Column(String, unique=True, index=True)
