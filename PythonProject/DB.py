from sqlalchemy import create_engine, text

user="postgres"
password="98071011"
host="localhost"
database="catalog"
port="5432"

engine = create_engine(
    f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
)

with engine.connect() as connection:
    result = connection.execute(text("SELECT 1"))
    print("Conectado com sucesso!")