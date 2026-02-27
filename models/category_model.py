from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from models.base_model import Base


class Category(Base):
    __tablename__ = 'category'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
