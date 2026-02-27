from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql+psycopg2://postgres:98071011@localhost:5432/catalog",
    connect_args={"options": "-c client_encoding=UTF-8"},
)

with engine.connect() as connection:
    print(connection.execute(text("SELECT 1")).scalar())