from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from models.imports.Results import Result
from utils.calculMethod import calculMoyenne

router = APIRouter()


@router.get("/makeCalcul/{period:str}")
async def madeCalcul(period: str):
    try:
        calculMoyenne(period)
        return JSONResponse("Calcul réalisés")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erreur Calcul : {e}")


@router.get("/getPeriodWithData")
async def getPeriod():
    try:
        return Result.getDate()
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erreur recup period : {e}")
