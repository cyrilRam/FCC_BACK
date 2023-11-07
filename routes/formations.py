from fastapi import APIRouter, Depends, HTTPException, UploadFile
from fastapi.responses import JSONResponse
from config.db import mydb
from models.formations import Formation
from typing import List
import pandas as pd
import io
from utils import excelMethodes

router = APIRouter()


@router.get("/formations/")
async def read_formation():
    try:
        cursor = mydb.cursor()
        query = "SELECT id_formation, nom, promotion FROM formations"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return {"formations": result}
    except Exception as e:
        print(f"Une exception s'est produite dans read_formation : {e}")
        raise HTTPException(
            status_code=500, detail="Erreur interne du serveur")


@router.post("/formations/", response_model=List[Formation])
async def create_Formation(file: UploadFile):
    try:
        formations = await excelMethodes.fromExcelToList(file, Formation)
        cursor = mydb.cursor()
        query = "INSERT INTO formations (nom, promotion) VALUES (%s, %s)"
        values = [(formation.nom, formation.promotion)
                  for formation in formations]
        cursor.executemany(query, values)
        mydb.commit()
        cursor.close()
        return JSONResponse("Ajout données réalisé")
    except HTTPException as e:
        # Gérer l'exception ici (par exemple, enregistrer un journal)
        print(f"Une exception s'est produite dans create_Formation : {e}")
        raise e
    except Exception as e:
        # Gérer l'exception ici (par exemple, enregistrer un journal)
        raise HTTPException(
            status_code=500, detail=f"Erreur BDD : {e}")
