from typing import Optional

import pandas as pd
from pydantic import BaseModel

import models.CRUD as CRUD


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
        values = [(formation.nom.lower(), formation.promotion.lower()) for formation in listStatic]
        CRUD.cudMethod(query, values)

    @staticmethod
    def get():
        query = "SELECT id_formation, nom, promotion FROM formation"
        result = CRUD.getDataStaticTable(query)
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
        CRUD.cudMethod(query, values)

    @staticmethod
    def update(listStatic):
        query = "UPDATE formation SET nom = %s, promotion = %s WHERE id_formation = %s"
        values = [(formation.nom.lower(), formation.promotion.lower(), formation.id) for formation in listStatic]
        CRUD.cudMethod(query, values)

    def __eq__(self, other):
        """
        Override the equality operator to compare based on nom and promotion fields.
        """
        return (
                isinstance(other, Formation)
                and self.nom == other.nom
                and self.promotion == other.promotion
        )
