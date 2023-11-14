from typing import List, Union

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from models.static_tables.Formation import Formation
from models.static_tables.Student import Student
from utils import UpdateAStaticTable

router = APIRouter()


@router.get("/getStaticTable/{obj_Type:str}")
async def read_table(obj_Type: str):
    try:
        if obj_Type == "formation":
            dataDf, listObject = Formation.get()
        elif obj_Type == "student":
            dataDf, listObject = Student.get()
        json_data = dataDf.to_json(orient="records")
        return JSONResponse(content=json_data)
    except Exception as e:
        print(f"Une exception s'est produite dans read_formation : {e}")
        raise HTTPException(
            status_code=500, detail="Erreur interne du serveur")


@router.post("/updateTable/")
async def update_Formation(newData: Union[List[Formation], List[Student]]):
    try:
        UpdateAStaticTable.updateTable(newData)
        return JSONResponse("Mise a jour des données")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erreur BDD : {e}")
