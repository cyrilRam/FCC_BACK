from fastapi import APIRouter, HTTPException, UploadFile
from fastapi.responses import JSONResponse

from models.imports.Results import Result
from utils import excelMethodes

router = APIRouter()


@router.post("/ImportsDataFromFile/{obj_Type:str}")
async def create_Formation(file: UploadFile, obj_Type: str):
    try:
        if obj_Type == "results":
            df, imports = await excelMethodes.fromExcelToList(file, Result)
            Result.add(imports)
            return JSONResponse("Ajout données réalisé")
    except Exception as e:
        # Gérer l'exception ici (par exemple, enregistrer un journal)
        raise HTTPException(
            status_code=500, detail=f"Erreur BDD : {e}")
