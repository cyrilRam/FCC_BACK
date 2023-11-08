
from pydantic import BaseModel


class Formation(BaseModel):
    nom: str
    promotion: str
