from sqlalchemy import Column, DateTime

class SoftDeleteMixin(object):

    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)