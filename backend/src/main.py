from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .infrastructure.api.routes import battles, predictions
from .infrastructure.database.connection import Base, engine
from .domain.exceptions import DomainError

app = FastAPI()

# データベース初期化
@app.on_event("startup")
async def init_db():
  Base.metadata.create_all(bind=engine)

# エラーハンドリングミドルウェア
@app.middleware("http")
async def error_handler(request: Request, call_next):
  try:
      return await call_next(request)
  except DomainError as e:
      return JSONResponse(
          status_code=400,
          content={"code": e.code, "message": e.message}
      )
  except Exception as e:
      return JSONResponse(
          status_code=500,
          content={
              "code": "INTERNAL_ERROR",
              "message": "Internal server error"
          }
      )
  
# ルーター登録
app.include_router(battles.router)
app.include_router(predictions.router)
  