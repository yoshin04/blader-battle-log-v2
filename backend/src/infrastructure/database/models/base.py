import uuid
from sqlalcemy import Column, String
from sqlalchemy.dialecs.postgresql import UUID
from ..conection import Base

class BaseModel(Base):
  __abstract__ = True
  id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
