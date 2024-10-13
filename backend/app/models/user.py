from app.db.base import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    # username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    # full_name = Column(String, nullable=True)
    firstname = Column(String(100))
    lastname = Column(String(100), nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # If you want to relate this user to other entities, such as QR codes
    # qr_codes = relationship("QRCode", back_populates="owner")
    # profile = relationship("Profile", back_populates="user")

    def __repr__(self):
        return f"User(firstname={self.firstname}, lastname={self.lastname}, id={self.id}, hashed_password={self.hashed_password})"



class Profile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        Integer, ForeignKey("users.id"), unique=True, nullable=False
    )  # Foreign key linking to the User model
    bio = Column(Text, nullable=True)
    profile_image = Column(String, nullable=True)  # URL to the user's profile image
    website = Column(String, nullable=True)
    location = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship back to the User model
    # user = relationship("User", back_populates="profile")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"
