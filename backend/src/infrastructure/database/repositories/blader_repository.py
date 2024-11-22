from typing import Optional, LiteralString
from uuid import UUID
from sqlalchemy.orm import Session
from ....domain.repositories.blader_repository import BladerRepository
from ....domain.entities.blader import Blader
from ..models.blader import BladerModel

class SQLBladerRepository(BladerRepository):
  def __init__(self, session: Session):
    self.session = session

  async def find_by_id(self, id: UUID) -> Optional[Blader]:
    model = self.session.query(BladerModel).filter(BladerModel.id == id).first()
    return self._to_entity(model) if model else None
  
  async def find_by_name(self, name: str) -> Optional[Blader]:
    model = self.session.query(BladerModel).filter(BladerModel.name == name).first()
    return self._to_entity(model) if model else None

  def _to_entity(self, model: BladerModel) -> Blader:
    return Blader(
      id=model.id,
      name=model.name,
      rank=model.rank,
      team_id=model.team_id,
      rank_history=model.rank_history,
      win_rate=model.win_rate
    )
