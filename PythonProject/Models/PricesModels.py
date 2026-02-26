from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
from typing import List
from DB import engine
from sqlalchemy import Float, Integer
from BaseModels import Base




class Price(Base):
    __tablename__ = 'price'

    id: Mapped[int] = mapped_column(Integer,primary_key=True, autoincrement=True)
    Value: Mapped[float] = mapped_column(Float,nullable=False)


Base.metadata.create_all(engine)