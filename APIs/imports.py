from fastapi import APIRouter, HTTPException, UploadFile
from fastapi.responses import JSONResponse

from models.imports.Results import Result
from utils.imports import excelMethodes, importAFile

router = APIRouter()


@router.get("/getDataImports/{period:str}")
async def getImports(period: str):
    try:
        df, imports = Result.get(period)
        json_data = df.to_json(orient="records")
        return JSONResponse(content=json_data)

    except Exception as e:
        print(f"Une exception s'est produite dans read_formation : {e}")
        raise HTTPException(
            status_code=500, detail="Erreur interne du serveur")


@router.post("/ImportsDataFromFile/{obj_Type:str}")
async def uploadResults(file: UploadFile, obj_Type: str):
    try:
        if obj_Type == "results":
            df, imports = await excelMethodes.fromExcelToList(file, Result)
            importAFile.importDataFromImportFile(imports)
            return JSONResponse("Ajout données réalisé")
    except Exception as e:
        # Gérer l'exception ici (par exemple, enregistrer un journal)
        raise HTTPException(
            status_code=500, detail=f"Erreur BDD : {e}")
