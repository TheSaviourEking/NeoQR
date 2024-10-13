from app.db.base import Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime


class QRCode(Base):
    __tablename__ = "qrcodes"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    data = Column(
        Text, nullable=False
    )  # The actual data that the QR code encodes (e.g., URL, text)
    image_url = Column(String, nullable=False)  # URL of the generated QR code image
    customization = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship back to the User model
    owner = relationship("User", back_populates="qr_codes")
