from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Boolean, ForeignKey
from DB import engine
from BaseModels import Base


class Products(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    status: Mapped[bool] = mapped_column(Boolean, nullable=False)

    store_id: Mapped[int] = mapped_column(ForeignKey("stores.id"))

    store: Mapped["store"] = relationship("stores", back_populates="products")


Base.metadata.create_all(engine)