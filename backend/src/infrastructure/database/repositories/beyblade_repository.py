from uuid import UUID
from typing import List, Optional
from sqlalchemy.orm import Session, joinedload
from ....domain.repositories.beyblade_repository import BeybladeRepository
from ....domain.entities.beyblade import Beyblade, BeyType
from ..models.beyblade import BeybladeModel, BladeModel, RatchetModel, BitModel

class SQLBeybladeRepository(BeybladeRepository):
  def __init__(self, session: Session):
    self.session = session

  async def find_by_id(self, id: UUID) -> Optional[Beyblade]:
    model = (self.session.query(BeybladeModel)
              .options(joinedload(BeybladeModel.blade))
              .options(joinedload(BeybladeModel.ratchet))
              .options(joinedload(BeybladeModel.bit))
              .filter(BeybladeModel.id == id)
              .first())
    return self._to_entity(model) if model else None

  async def find_by_type(self, bey_type: BeyType) -> List[Beyblade]:
    models = (self.session.query(BeybladeModel).filter(BeybladeModel.type == bey_type).all())
    return [self._to_entity(model) for model in models]
  
  async def find_environment_beys(self) -> List[Beyblade]:
    models = (self.session.query(BeybladeModel).filter(BeybladeModel.is_environment == True).all())
    return [self._to_entity(model) for model in models]
  