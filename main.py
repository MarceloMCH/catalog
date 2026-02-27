from db import engine
from models.base_model import Base

import models.category_model  # noqa:
import models.products_model  # noqa:
import models.stores_model    # noqa:

Base.metadata.create_all(engine)
print("Tabelas criadas com sucesso!")