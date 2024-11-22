from abc import abstractmethod
from .base import Repository
from ..entities.blader import Blader
from typing import List, Optional

class BladerRepository(Repository[Blader]):
    @abstractmethod
    async def find_by_name(self, name: str) -> Optional[Blader]:
        pass
    
    @abstractmethod
    async def find_by_team(self, team_id: UUID) -> List[Blader]:
        pass
      
