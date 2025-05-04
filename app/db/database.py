from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.settings import settings
from app.models.tablet import Tablet

engine = create_engine(settings.DATABASE_URL, connect_args= {"check_same_thread" : False})

SessionLocal = sessionmaker(autocommit = False, autoflush= False, bind= engine)

def get_db():
    
    db = SessionLocal()
    
    try:
        yield db
    finally:
        db.close()
        
        
get_db()
