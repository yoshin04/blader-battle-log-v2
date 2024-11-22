from uuid import UUID
from sqlalchemy import Column, String, Integer, Float, ForeignKey, JSON
from .base import BaseModel

class BladerModel(BaseModel):
  __tablename__ = "bladers"

  name = Column(String, nullable=False)
  rank = Column(Integer, nullable=False)
  team_id = Column(UUID(as_uuid=True), ForeignKey("teams.id"), nullable=True)
  rank_history = Column(JSON, nullable=True)
  win_rate = Column(Float, nullable=True)
