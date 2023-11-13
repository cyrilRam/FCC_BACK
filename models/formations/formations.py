from typing import Optional

from pydantic import BaseModel


class Formation(BaseModel):
    id: Optional[int]
    nom: str
    promotion: str
