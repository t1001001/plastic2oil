from pydantic import BaseModel

class Plastic(BaseModel):
    hdpe: float = 0.0
    ldpe: float = 0.0
    pp: float = 0.0
    ps_eps: float = 0.0