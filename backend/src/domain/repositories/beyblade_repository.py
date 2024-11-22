from abc import abstractmethod
from .base import Repository
from ..entities.beyblade import Beyblade, BeyType
from typing import List

class BeybladeRepository(Repository[Beyblade]):
  @abstractmethod
  async def find_by_type(self, bey_type: BeyType) -> List[Beyblade]:
    pass

  @abstractmethod
  async def find_environment_beys(self) -> List[Beyblade]:
    pass
