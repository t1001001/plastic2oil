from pydantic import BaseModel

class Oil(BaseModel):
    amount_of_plastic: float
    money: float