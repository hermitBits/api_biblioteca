from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{getenv('MYSQL_USER')}:{getenv('MYSQL_ROOT_PASSWORD')}@{getenv('MYSQL_SERVICE')}:3306/{getenv('MYSQL_DATABASE')}"

print(SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()