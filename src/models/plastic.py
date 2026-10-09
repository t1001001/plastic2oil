from pydantic import BaseModel

class Plastic(BaseModel):
    hdpe: float | None = None
    ldpe: float | None = None
    pp: float | None = None
    ps_eps: float | None = None