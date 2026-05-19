from app.core.db import Base
from sqlalchemy import Column,String,Integer

class Users(Base):
    
    __table_name__ ="users"
    
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String)
    password = Column(String)
    