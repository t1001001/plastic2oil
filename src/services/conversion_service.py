from src.models.plastic import Plastic
from src.models.oil import Oil

def convert(plastic: Plastic) -> Oil:
    pyrolysis_oil = plastic.amount * 0.75
    money = pyrolysis_oil * 10.7
    return Oil(
        amount_of_plastic=plastic.amount,
        amount_of_pyrolysis_oil = pyrolysis_oil,
        money=money
    )