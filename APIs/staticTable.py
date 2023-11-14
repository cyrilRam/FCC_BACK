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


# @router.post("/addDataStaticTable/{obj_Type:str}")
# async def create_Formation(file: UploadFile, obj_Type: str):
#     try:
#         if obj_Type == "formation":
#             formations = await excelMethodes.fromExcelToList(file, Formation)
#             Formation.add(formations)
#         elif obj_Type == "student":
#             students = await excelMethodes.fromExcelToList(file, Student)
#             Student.add(students)
#
#         return JSONResponse("Ajout données réalisé")
#     except Exception as e:
#         # Gérer l'exception ici (par exemple, enregistrer un journal)
#         raise HTTPException(
#             status_code=500, detail=f"Erreur BDD : {e}")


@router.post("/updateTable/")
async def update_Formation(newData: Union[List[Formation], List[Student]]):
    try:
        UpdateAStaticTable.updateTable(newData)
        return JSONResponse("Mise a jour des données")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erreur BDD : {e}")
