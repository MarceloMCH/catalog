import re

from sqlalchemy.orm import DeclarativeBase, declared_attr


class Base(DeclarativeBase):

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return to_snake_case(cls.__name__)


def to_snake_case(name: str) -> str:
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
