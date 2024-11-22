from fastapi import APIRouter, Depends
from ....application.usecases.record_battle import RecordBattleUseCase, RecordBattleRequest
from ..dependencies import get_battle_usecase

router = APIRouter(prefix="/api/battles")

@router.post("")
async def record_battle(
  request: RecordBattleRequest,
  usecase: RecordBattleUseCase = Depends(get_battle_usecase)
):
  return await usecase.execute(request)

@router.get("")
async def get_battles(
  blader_name: str = None,
  start_date: datetime = None,
  end_date: datetime = None,
):
  # 実装