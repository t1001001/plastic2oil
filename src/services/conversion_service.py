from src.models.plastic import Plastic
from src.models.oil import Oil

def convert(plastic: Plastic) -> Oil:
    amount_of_plastic = plastic.hdpe + plastic.ldpe + plastic.pp + plastic.ps_eps
    amount_of_pyrolysis_oil = plastic.hdpe * 0.75 + plastic.ldpe * 0.75 * plastic.pp * 0.75 + plastic.ps_eps * 0.75
    money = amount_of_pyrolysis_oil * 10.7
    return Oil(
        amount_of_plastic=amount_of_plastic,
        amount_of_pyrolysis_oil = amount_of_pyrolysis_oil,
        money=money
    )