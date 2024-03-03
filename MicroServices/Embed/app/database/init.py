from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv(override=True)

print(os.getenv('MYSQL_USER'))
# DATABASE_URL = "mysql+mysqlconnector://" + os.getenv('MYSQL_USER') + ":" + os.getenv('MYSQL_PASSWORD') + "@" + os.getenv('DB_HOST') + ":" + os.getenv('DB_PORT') + "/" + os.getenv('DB_NAME')
print("DATABASE_URL", os.getenv('MYSQL_USER'), os.getenv('MYSQL_PASSWORD'), os.getenv('DB_HOST'))
engine = create_engine('DATABASE_URL', echo=True)
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
    
