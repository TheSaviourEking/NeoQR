from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.db.base import Base


class User(Base):
    """The User model"""

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

    qr_codes = relationship("QRCode", back_populates="user")

    # profile = relationship(
    #     "Profile",
    #     back_populates="user",
    #     uselist=False,
    #     cascade="all, delete-orphan",
    #     lazy="joined",
    # )

    profile = relationship(
        "Profile",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan",
    )

    # def __repr__(self):
    #     return f"<User id={self.id} email={self.email} firstname={self.firstname} lastname={self.lastname}>"


class Profile(Base):
    """The User Profile Model"""

    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    bio = Column(Text, nullable=True)
    profile_image = Column(String, nullable=True)  # URL to the user's profile image
    website = Column(String, nullable=True)
    location = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship back to the User model
    # user = relationship("User", back_populates="profile", lazy="joined")
    user = relationship("User", back_populates="profile")

    # def __repr__(self):
    #     return f"<Profile id={self.id} user_id={self.user_id} bio={self.bio} profile_image={self.profile_image} website={self.website} location={self.location}>"
