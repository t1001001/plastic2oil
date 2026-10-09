from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from src.models.oil import Oil
from src.models.plastic import Plastic
from src.services.conversion_service import convert

router = APIRouter()

@router.post("/conversion", response_model=Oil)
async def convert_plastic(plastic: Plastic, request: Request):
    oil = convert(plastic=plastic)
    if request.headers.get("HX-Request") == "true":
        return HTMLResponse(
            content=(
                f"<p>Plastic: {oil.amount_of_plastic:g}</p>"
                f"<p>Pyrolysis oil: {oil.amount_of_pyrolysis_oil:g}</p>"
                f"<p>Estimated value: {oil.money:g}</p>"
            )
        )
    return oil