from .BaseModel import BaseModel
from .mixins.SoftDeletes import SoftDeleteMixin
from sqlalchemy import Column, Integer, String
from dataclasses import dataclass

@dataclass
class User(SoftDeleteMixin, BaseModel):

    # Omitting a column here hides
    # it from the json serialization
    id: int
    username: str

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    def __init__(self, username, password):
        self.protected_columns = [ 'password' ]
        self.username = username
        self.password = password

    