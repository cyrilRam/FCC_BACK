from fastapi import APIRouter, HTTPException, UploadFile
from fastapi.responses import JSONResponse

from models.imports.Results import Result
from utils import excelMethodes
from utils import importAFile

router = APIRouter()


@router.get("/getDataImports/")
async def getImports():
    try:
        df, imports = Result.get()
        json_data = df.to_json(orient="records")
        return JSONResponse(content=json_data)

    except Exception as e:
        print(f"Une exception s'est produite dans read_formation : {e}")
        raise HTTPException(
            status_code=500, detail="Erreur interne du serveur")


@router.post("/ImportsDataFromFile/{obj_Type:str}")
async def create_Formation(file: UploadFile, obj_Type: str):
    try:
        if obj_Type == "results":
            df, imports = await excelMethodes.fromExcelToList(file, Result)
            importAFile.importDataFromImportFile(imports)
            return JSONResponse("Ajout données réalisé")
    except Exception as e:
        # Gérer l'exception ici (par exemple, enregistrer un journal)
        raise HTTPException(
            status_code=500, detail=f"Erreur BDD : {e}")
