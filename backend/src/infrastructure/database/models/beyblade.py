from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey, Enum
from sqlqlchemy.dialects.postgresql import UUID
from .base import BaseModel
from ....domain.entities.beyblade import BeyType

class BladeModel(BaseModel):
  __tablename__ = "blades"
  name = Column(String, nullable=False)
  attack = Column(Integer, nullable=False)
  defense = Column(Integer, nullable=False)
  stamina = Column(Integer, nullable=False)
  weight = Column(Float, nullable=False)

class RatchetModel(BaseModel):
  __tablename__ = "ratchets"
  name = Column(String, nullable=False)
  attack = Column(Integer, nullable=False)
  defense = Column(Integer, nullable=False)
  stamina = Column(Integer, nullable=False)
  weight = Column(Float, nullable=False)

class BitModel(BaseModel):
  __tablename__ = "bits"
  name = Column(String, nullable=False)
  attack = Column(Integer, nullable=False)
  defense = Column(Integer, nullable=False)
  stamina = Column(Integer, nullable=False)
  dash = Column(Integer, nullable=False)
  burst_resistance = Column(Integer, nullable=False)
  weight = Column(Float, nullable=False)

class BeybladeModel(BaseModel):
  __tablename__ = "beyblades"
  blade_id = Column(UUID(as_uuid=True), ForeignKey("blades.id"), nullable=False)
  ratchet_id = Column(UUID(as_uuid=True), ForeignKey("ratchets.id"), nullable=False)
  bit_id = Column(UUID(as_uuid=True), ForeignKey("bits.id"), nullable=False)
  type = Column(Enum(BeyType), nullable=False)
  is_environment = Column(Boolean, default=False)
  environment_score = Column(Integer, nullable=True)
  memo = Column(String, nullable=True)

