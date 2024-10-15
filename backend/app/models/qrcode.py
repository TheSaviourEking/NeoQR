from app.db.base import Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime


# class QRCode(Base):
#     __tablename__ = "qrcodes"

#     id = Column(Integer, primary_key=True, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
#     data = Column(
#         Text, nullable=False
#     )  # The actual data that the QR code encodes (e.g., URL, text)
#     image_url = Column(String, nullable=False)  # URL of the generated QR code image
#     customization = Column(Text, nullable=True)
#     created_at = Column(DateTime, default=datetime.utcnow)
#     updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship back to the User model
    # owner = relationship("User", back_populates="qr_codes")


class QRCode(Base):
    """ The QR code model """
    __tablename__ = "qr_codes"

    id = Column(Integer, primary_key=True, index=True)

    data = Column(String, nullable=False)

    # Customization options
    background_color = Column(String, default="#FFFFFF")
    foreground_color = Column(String, default="#000000") 
    custom_image_url = Column(String, nullable=True)  # Link to an image if user uploads
    pattern = Column(String, default="square")  # E.g., square, circle, etc.

    # QR code performance/tracking fields
    scan_count = Column(Integer, default=0)  # Number of times the QR code was scanned
    last_scanned_at = Column(DateTime, nullable=True)  # Timestamp of the last scan

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Foreign key to relate the QR code to the user who created it
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="qr_codes")

    def increment_scan_count(self):
        """Method to update the scan count and last scanned timestamp."""
        self.scan_count += 1
        self.last_scanned_at = datetime.utcnow()
