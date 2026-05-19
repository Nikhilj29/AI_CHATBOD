from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
from app.core.config import setting

engine = create_engine(
    setting.DATABASE_URL,
    isolation_level="READ COMMITTED"
)

session_local = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()
Base.metadata.create_all(bind=engine)

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()