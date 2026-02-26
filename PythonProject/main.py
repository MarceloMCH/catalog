from DB import engine


# importe TODOS os models
from Models.BaseModels import Base
from Models.StoresModels import Store
from Models.ProductsModels  import Products

Base.metadata.create_all(engine)

print("Tabelas criadas com sucesso!")