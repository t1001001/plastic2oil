from pydantic import BaseModel

class Oil(BaseModel):
    amount_of_plastics: float
    money: float