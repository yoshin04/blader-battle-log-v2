from fastapi import APIRouter, Depends

router = APIRouter(prefix="/api/battles")

@router.post("/predict")
async def predict_beyblade(
  request: PredictionRequest,
  usecase: PredictBeybladeUseCase = Depends(get_prediction_usecase)
):
  return await usecase.execute(request)

