from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = "mysql+mysqlconnector://" + os.getenv('MYSQL_USER') + ":" + os.getenv('MYSQL_PASSWORD') + "@" + os.getenv('DB_HOST') + ":" + os.getenv('DB_PORT') + "/" + os.getenv('DB_NAME')
engine = create_engine(DATABASE_URL, echo=True)
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
    
