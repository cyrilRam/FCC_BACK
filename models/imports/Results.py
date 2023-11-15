import pandas as pd
from pydantic import BaseModel

import models.CRUD as CRUD


class Result(BaseModel):
    periodstr: str
    nom: str
    prenom: str
    note: int

    @staticmethod
    def add(listImports):
        query = "INSERT INTO resultats (periodstr, nom,prenom,note) VALUES (%s, %s,%s,%s)"
        values = [(result.periodstr.upper(), result.nom.lower(), result.prenom.lower(), result.note) for result in
                  listImports]
        CRUD.cudMethod(query, values)

    @staticmethod
    def get(periodstr=None):
        if periodstr:
            query = "SELECT periodstr, nom, prenom,note FROM resultats WHERE periodstr=%s"
            params = (periodstr,)
            result = CRUD.getDataStaticTable(query, params)
        else:
            query = "SELECT periodstr, nom, prenom,note FROM resultats"
            result = CRUD.getDataStaticTable(query)

        staticList = [Result(periodstr=row[0], nom=row[1], prenom=row[2], note=row[3]) for row in result]
        columns = ["periodstr", "nom", "prenom", "note"]
        staticDf = pd.DataFrame(result, columns=columns)
        return staticDf, staticList

    @staticmethod
    def delete(period):
        query = ("DELETE FROM resultats WHERE periodstr = %s")
        values = [(period,)]
        CRUD.cudMethod(query, values)

    def isDataExisting(period):
        query = "SELECT * FROM resultats WHERE periodstr=%s"
        params = (period,)
        result = CRUD.getDataStaticTable(query, params)
        return True if result else False
