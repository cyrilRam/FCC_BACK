import pandas as pd
from pydantic import BaseModel

from models.imports import importsDAO


class Result(BaseModel):
    periodstr: str
    nom: str
    prenom: str
    note: int

    @staticmethod
    def add(listImports):
        query = "INSERT INTO resultats (periodstr, nom,prenom,note) VALUES (%s, %s,%s,%s)"
        values = [(result.periodstr, result.nom, result.prenom, result.note) for result in listImports]
        importsDAO.cudMethod(query, values)

    @staticmethod
    def get():
        query = "SELECT periodstr, nom, prenom,note FROM resultats"
        result = importsDAO.getDataStaticTable(query)
        staticList = [Result(periodstr=row[0], nom=row[1], prenom=row[2], note=row[3]) for row in result]
        columns = ["periodstr", "nom", "prenom", "note"]
        staticDf = pd.DataFrame(result, columns=columns)
        return staticDf, staticList

    @staticmethod
    def delete(listStatic):
        query = ("DELETE FROM resultats WHERE periodstr = %s")
        values = [(result.periodstr,) for result in listStatic]
        importsDAO.cudMethod(query, values)
