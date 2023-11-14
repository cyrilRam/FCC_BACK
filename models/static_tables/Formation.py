from typing import Optional

import pandas as pd
from pydantic import BaseModel

import models.static_tables.staticDAO as staticDAO


class Formation(BaseModel):
    id: Optional[int]
    nom: str
    promotion: str

    # def __init__(self, id: Optional[int] = None, nom: str = "", promotion: str = "", **data: Any):
    #     super().__init__(**data)
    #     self.id = id
    #     self.nom = nom
    #     self.promotion = promotion

    @staticmethod
    def add(listStatic):
        query = "INSERT INTO formation (nom, promotion) VALUES (%s, %s)"
        values = [(formation.nom, formation.promotion) for formation in listStatic]
        staticDAO.cudMethod(query, values)

    @staticmethod
    def get():
        query = "SELECT id_formation, nom, promotion FROM formation"
        result = staticDAO.getDataStaticTable(query)
        # convertir liste de forma
        staticList = [Formation(id=row[0], nom=row[1], promotion=row[2]) for row in result]
        # Convertir les résultats en DataFrame de pandas
        columns = ["id", "nom", "promotion"]
        staticDf = pd.DataFrame(result, columns=columns)
        return staticDf, staticList

    @staticmethod
    def delete(listStatic):
        query = ("DELETE FROM formation WHERE id_formation = %s")
        values = [(formation.id,) for formation in listStatic]
        staticDAO.cudMethod(query, values)

    @staticmethod
    def update(listStatic):
        query = "UPDATE formation SET nom = %s, promotion = %s WHERE id_formation = %s"
        values = [(formation.nom, formation.promotion, formation.id) for formation in listStatic]
        staticDAO.cudMethod(query, values)