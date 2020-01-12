from .BaseModel import BaseModel
from sqlalchemy import Column, Integer, String
from dataclasses import dataclass

@dataclass
class User(BaseModel):

    # Omitting a column here hides
    # it from the json serialization
    id: int
    username: str

    __tablename__ = 'users'

    protected_columns = [ 'password' ]

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    