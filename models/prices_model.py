from sqlalchemy import Float, Integer
from sqlalchemy.orm import Mapped, mapped_column

from db import engine
from models.base_model import Base


class Price(Base):
    __tablename__ = 'price'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    Value: Mapped[float] = mapped_column(Float, nullable=False)


Base.metadata.create_all(engine)
