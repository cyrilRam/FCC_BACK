from pydantic import BaseModel


class Student(BaseModel):
    nom: str
    prenom: str
    age: int
