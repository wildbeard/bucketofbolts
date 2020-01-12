from .BaseModel import BaseModel
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import Column, Integer, String, DateTime
from dataclasses import dataclass

@dataclass
class Hardware(BaseModel):

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

    # Used for the hardware_type hybrid prop
    # Should be defined on any Model that extends
    # Hardware
    HARDWARE_TYPE = 0

    id = Column(Integer, primary_key=True)
    hardware_type_id = Column(Integer)
    hardware_size_id = Column(Integer)
    user_id = Column(Integer)
    name = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)

    def __init__(self, hardware_type_id, hardware_size_id, user_id, name):
        self.hardware_type_id = hardware_type_id
        self.hardware_size_id = hardware_size_id
        self.user_id = user_id
        self.name = name

    # A scope of sorts to use as a query filter
    @hybrid_property
    def hardware_type(self):
        return self.hardware_type_id == self.HARDWARE_TYPE

