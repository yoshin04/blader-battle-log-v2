from abc import abstractmethod
from .base import Repository
from ..entities.battle import Battle
from datetime import datetime
from typing import List

class BattleRepository(Repository[Battle]):
  @abstractmethod
  async def find_by_blader(self, blader_id: UUID) -> List[Battle]:
    pass

  @abstractmethod
  async def find_by_date_range(self, start: datetime, end: datetime) -> List[Battle]: 
    pass
