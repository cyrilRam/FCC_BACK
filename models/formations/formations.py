from pydantic import BaseModel
from typing import Optional


class Formation(BaseModel):
    nom: str
    promotion: str
