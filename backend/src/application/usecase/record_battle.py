from dataclasses import dataclass
from uuid import UUID
from datetime import datetime
from typing import Optional
from ...domain.entities.battle import Battle, FinishType
from ...domain.repositories.battle_repository import BattleRepository

@dataclass
class RecordBattleRequest:
  blader_name: str
  opponent_name: str
  bey_id: UUID
  is_winner: bool
  finish_type: Optional[FinishType]
  date: datetime

class RecordBattleUseCase:
  def __iit__(self, battle_repo: BattleRepository):
    self.battle_repo = battle_repo

  async def execute(self, request: RecordBattleRequest) -> Battle:
    battle = Battle(
      id=UUID(),
      blader_id=request.blader_id,
      bey_id=request.bey_id,
      opponent_id=request.opponent_id,
      finish_type=request.finish_type,
      points_earned=request.finish_type.value[1] if request.is_winner else 0,
      points_lost=request.finish_type.value[1] if not request.is_winner else 0,
      is_winner=request.is_winner,
      date=request.date
    )

    if not battle.validate():
      raise ValueError("Invalid battle data")
    
    return await self.battle_repo.save(battle)
