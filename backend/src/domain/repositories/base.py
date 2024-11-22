from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, List
from uuid import UUID

T = TypeVar('T')

class Repository(ABC, Generic[T]):
  @abstractmethod
  async def find_by_id(self, id: UUID) -> Optional[T]:
    pass

  @abstractmethod
  async def find_all(self) -> List[T]:
    pass

  @abstractmethod
  async def save(self, entity: T) -> T:
    pass

  @abstractmethod
  async def delete(self, id: UUID) -> bool:
    pass
