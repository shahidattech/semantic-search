from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Text, String, Sequence, Column, DateTime
import datetime


Base = declarative_base()

class Topic(Base):
    __tablename__ = "SKILLS"
    id = Column(Integer, primary_key=True, index=True)
    topic_name = Column(String(15), index=True, unique=True)
    files_in_topic = Column(Text)
    tenant_id =  Column(String(30), index= True)
    created_by = Column(String(30), index= True)
    updated_by = Column(String(30), index= True)
    creation_time = Column(DateTime, default=datetime.datetime.utcnow)
    updation_time = Column(DateTime, default=None)