from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from sqlalchemy import DateTime
from datetime import datetime

DATABASE_URL = 'sqlite:///./app.db'

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class NotFoundError(Exception):
    pass


# Database Models
class DBItem(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, nullable = False)
    description = Column(String)
    automations = relationship("DBAutomation", back_populates="item")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class DBAutomation(Base):
    __tablename__ = "automations"
    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"), nullable=False)
    code = Column(String, nullable=False)
    item = relationship("DBItem", back_populates="automations")
    
#Drop all the tables 
Base.metadata.drop_all(bind=engine) 
#create all table
Base.metadata.create_all(bind=engine)


# this check the opening and closing activity of the db session
def get_db():
    """Dependency that provides database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
