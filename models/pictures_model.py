from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped

from models.base_model import Base


class Pictures(Base):
    __tablename__ = 'pictures'
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    Path: Mapped[str] = Column(String(30), nullable=False)
