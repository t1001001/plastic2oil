from src.models.plastic import Plastic
from src.models.oil import Oil

def convert(plastic: Plastic) -> Oil:
    return Oil(
        amount_of_plastic=plastic.amount_kg,
        money=plastic.amount_kg * 2
    )