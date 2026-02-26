from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Table, Column, Integer, String, Boolean
from DB import engine
from BaseModels import Base


class Pictures(Base):
    __tablename__ = 'pictures'
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    Path: Mapped[str] = Column(String(30), nullable=False)


Base.metadata.create_all(engine)