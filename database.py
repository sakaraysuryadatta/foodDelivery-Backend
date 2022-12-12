from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHAMY_DATABASE_URL = 'sqlite:///./data.db'
#SQLALCHAMY_DATABASE_URL = 'postgres://samarthasthan5:cxM2DQIw4HJm@ep-black-wave-101254.ap-southeast-1.aws.neon.tech/neondb'

engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args={
                       "check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False,)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()