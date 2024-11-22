from typing import List, Optional
from datetime import datetime
from sqlalchemy.orm import Session
from ....domain.repositories.battle_repository import BattleRepository
from ....domain.entities.battle import Battle
from ..models.battle import BattleModel

class SQLBattleRepository(BattleRepository):
  def __init__(self, session: Session):
    self.session = session

  async def find_by_id(self, id: UUID) -> Optional[Battle]:
    model = self.session.query(BattleModel).filter(BattleModel.id == id).first()
    return self._to_entity(model) if model else None
  
  async def find_by_blader(self, blader_id: UUID) -> List[Battle]:
    models = (self.session.query(BattleModel).filter(BattleModel.blader_id == blader_id).all())
    return [self._to_entity(model) for model in models]
  
  async def find_by_date_range(self, start: datetime, end: datetime) -> List[Battle]:
    models = (self.session.query(BattleModel).filter(BattleModel.date >= start).filter(BattleModel.date <= end).all())
    return [self._to_entity(model) for model in models]
