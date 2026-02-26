from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from DB import engine
from BaseModels import Base

class Category(Base):
    __tablename__ = 'category'
    id: Mapped[int] = mapped_column(Integer,primary_key=True, autoincrement=True)
    name:Mapped[str] = mapped_column(String(30), nullable=False)

Base.metadata.create_all(engine)
