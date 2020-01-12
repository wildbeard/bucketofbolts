from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel(Base):

    __abstract__ = True

    # Protected columns would be hidden from
    # the to_dict method
    protected_columns = []

    def to_dict(self):
        d = {}
        for col in self.__table__.columns:
            if col.name in self.protected_columns:
                continue
            d[col.name] = getattr(self, col.name)
        return d