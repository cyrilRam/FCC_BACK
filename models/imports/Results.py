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

    # @staticmethod
    # def get():
    #     query = "SELECT id_formation, nom, promotion FROM formation"
    #     result = staticDAO.getDataStaticTable(query)
    #     # convertir liste de forma
    #     staticList = [Formation(id=row[0], nom=row[1], promotion=row[2]) for row in result]
    #     # Convertir les résultats en DataFrame de pandas
    #     columns = ["id", "nom", "promotion"]
    #     staticDf = pd.DataFrame(result, columns=columns)
    #     return staticDf, staticList
