from fastapi import APIRouter, HTTPException, UploadFile
from fastapi.responses import JSONResponse
import models.formations.formationsDAO as DAO
from models.formations.formations import Formation
from typing import List
from utils import excelMethodes
from typing import TypeVar, List, Type


router = APIRouter()


@router.get("/formations/")
async def read_formation():
    try:
       formationsDf=DAO.getFormations()
       json_data=formationsDf.to_json(orient="records")
       return JSONResponse(content=json_data)
    except Exception as e:
        print(f"Une exception s'est produite dans read_formation : {e}")
        raise HTTPException(
            status_code=500, detail="Erreur interne du serveur")


@router.post("/formations/", response_model=List[Formation])
async def create_Formation(file: UploadFile):
    try:
        formations = await excelMethodes.fromExcelToList(file, Formation)
        DAO.addFormations(formations)
        return JSONResponse("Ajout données réalisé")
    except Exception as e:
        # Gérer l'exception ici (par exemple, enregistrer un journal)
        raise HTTPException(
            status_code=500, detail=f"Erreur BDD : {e}")


@router.post("/formations/updateTable/",response_model=List[Formation])
async def update_Formation(newData:List[Formation]):
    """
    on va devoir gerer le cas on ou on a un id de fee et onn peut modifier ajouter de new fees
    il vaut mieux des tables avec un id a chaque fois et une unicite de la valeur ou alors c'st miux de mttr juste les noms
    et d'avoir ca en cle primaire.
    Sinon la table formation on met juste couple nom et promotion en cle primaire
    le pb avec ca si je modifie le nom et que j'ai une table qui utilise ce nom alors ma table est fausse alors que avec
    l'id je dois juste mettre a jour la valeur
    :param newData:
    :return:
    """
    # check chaque id si nom/promotion a changé on met à jour
    # si new id alors on ajoute dans la table
    # si lid n'est plus la on supprimme'
    try:

        print(newData)
        print(type(newData[0]))

        return JSONResponse("Mise a jour des données")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erreur BDD : {e}")

