from pydantic import BaseModel


class Formation(BaseModel):
    id: int
    nom: str
    promotion: str
