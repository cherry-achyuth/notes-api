from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase,sessionmaker
import os

load_dotenv()

database_url = os.getenv('DATABASE_URL')

if not database_url:
    raise RuntimeError("database url is not configured")

engine = create_engine(database_url,pool_pre_ping = True)

SessionLocal = sessionmaker(bind = engine,autoflush=False,expire_on_commit = False)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()