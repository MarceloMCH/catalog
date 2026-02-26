from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from sqlalchemy import String, Boolean, Integer
from DB import engine
from BaseModels import Base


class Store(Base):
    __tablename__ = 'stores'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    UID: Mapped[str] = mapped_column(String(50), nullable=False)
    status: Mapped[bool] = mapped_column(Boolean, nullable=False)

    products: Mapped[List["Products"]] = relationship("Products", back_populates="stores")


Base.metadata.create_all(engine)