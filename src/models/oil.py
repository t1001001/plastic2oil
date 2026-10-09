from pydantic import BaseModel

class Oil(BaseModel):
    amount_of_plastic: float
    amount_of_pyrolysis_oil: float
    money: float