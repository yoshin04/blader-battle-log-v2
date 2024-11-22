from fastapi import Depends
from ..database.connection import SessionLocal
from ..database.repositories import *

async def get_db():
  db = SessionLocal()
  try:
      yield db
  finally:
      db.close()

def get_battle_usecase(db = Depends(get_db)):
  repo = SQLBattleRepository(db)
  return RecordBattleUseCase(repo)
