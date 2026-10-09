from fastapi import APIRouter
from src.models.oil import Oil
from src.models.plastic import Plastic
from src.services.conversion_service import convert

router = APIRouter()

@router.post("/conversion", response_model=Oil)
async def convert_plastic(plastic: Plastic):
    return convert(plastic=plastic)