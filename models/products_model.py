from sqlalchemy import Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base_model import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    status: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    store_id: Mapped[int] = mapped_column(ForeignKey("stores.id"), nullable=False)

    store: Mapped["Store"] = relationship("Store", back_populates="products")
