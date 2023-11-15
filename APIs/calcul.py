from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

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
