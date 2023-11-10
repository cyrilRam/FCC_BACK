from fastapi import APIRouter, Depends, HTTPException, UploadFile
from fastapi.responses import JSONResponse
import models.formations.formationsDAO as DAO
from models.formations.formations import Formation
from typing import List
from utils import excelMethodes


router = APIRouter()


@router.get("/formations/")
async def read_formation():
    try:
       return DAO.getFormations()
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
