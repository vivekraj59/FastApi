from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# sqlalchemy does not know how to talk to DB, it has all the code to write the models. It will need a DB driver. We are using postgres DB.psycopg2 is the postgres DB driver


# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:admin@localhost:5432/fastapi'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
# SQLALCHEMY_DATABASE_URL = f'postgresql://{Settings.database_username}:{Settings.database_password}@{Settings.database_hostname}:{Settings.database_port}/{Settings.database_name}'


# engine is responsible for sql alchemy to connect to DB, it will establish the connection. To talk to DB we have to use session.
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# All the modes will be extending the base class
Base = declarative_base()


# Dependency, session object is responsible for talking to DB, it will give us a session. it close the session once done.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
