from uuid import UUID
from sqlalchemy import Column, DateTime, Integer, Boolean, ForeignKey, Enum
from .base import BaseModel
from ....domain.entities.battle import FinishType

class BattleModel(BaseModel):
  __tablename__ = "battles"
  blader_id = Column(UUID(as_uuid=True), ForeignKey("bladers.id"), nullable=False)
  bey_id = Column(UUID(as_uuid=True), ForeignKey("beyblades.id"), nullable=False)
  opponent_id = Column(UUID(as_uuid=True), ForeignKey("bladers.id"), nullable=False)
  finish_type = Column(Enum(FinishType), nullable=False)
  points_earned = Column(Integer, nullable=False)
  points_lost = Column(Integer, nullable=False)
  is_winner = Column(Boolean, nullable=False)
  date = Column(DateTime, nullable=False)
