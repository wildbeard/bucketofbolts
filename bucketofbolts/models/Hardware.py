from .BaseModel import BaseModel
from .mixins.SoftDeletes import SoftDeleteMixin
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import Column, Integer, String, DateTime
from dataclasses import dataclass

@dataclass
class Hardware(SoftDeleteMixin, BaseModel):

    # For json serialization
    id: int
    hardware_type_id: int
    hardware_size_id: int
    user_id: int
    name: int
    created_at: str
    updated_at: str
    deleted_at: str

    __tablename__ = 'hardware'

    id = Column(Integer, primary_key=True)
    hardware_type_id = Column(Integer)
    hardware_size_id = Column(Integer)
    user_id = Column(Integer)
    name = Column(String)

    def __init__(self, hardware_type_id, hardware_size_id, user_id, name):

        self.__HARDWARE_TYPE = None

        self.hardware_type_id = hardware_type_id
        self.hardware_size_id = hardware_size_id
        self.user_id = user_id
        self.name = name

    # A scope of sorts to use as a query filter
    @hybrid_property
    def hardware_type(self):
        return self.hardware_type_id == self.__HARDWARE_TYPE

