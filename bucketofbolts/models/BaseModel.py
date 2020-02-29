from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel(Base):

    __abstract__ = True
    
    def __init__(self):
        self.protected_columns = []

    def to_dict(self):
        d = {}
        for col in self.__table__.columns:
            if col.name in self.protected_columns:
                continue
            d[col.name] = getattr(self, col.name)
        return d