from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

from backend.database.database import Base


class Document(Base):

    __tablename__ = "documents"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    filename = Column(
        String,
        nullable=False
    )

    document_type = Column(
        String,
        nullable=False
    )

    extracted_text = Column(
        Text
    )

    extracted_information = Column(
        Text
    )

    uploaded_at = Column(
        DateTime,
        default=datetime.utcnow
    )