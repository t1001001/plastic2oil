from pydantic import BaseModel

class Plastic(BaseModel):
    hdpe: float
    ldpe: float
    pp: float
    ps_eps: float