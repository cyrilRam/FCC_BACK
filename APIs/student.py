from fastapi import APIRouter, HTTPException, UploadFile
from fastapi.responses import JSONResponse
import models.students.StudentsDAO as DAO
from models.students.Student import Student
from typing import List
from utils import excelMethodes
from typing import TypeVar, List, Type



router = APIRouter()


@router.get("/students/")
async def read_formation():
    try:
       studentsDF=DAO.getStudents()
       json_data=studentsDF.to_json(orient="records")
       return JSONResponse(content=json_data)
    except Exception as e:
        print(f"Une exception s'est produite dans read_formation : {e}")
        raise HTTPException(
            status_code=500, detail="Erreur interne du serveur")


@router.post("/students/", response_model=List[Student])
async def create_Formation(file: UploadFile):
    try:
        students = await excelMethodes.fromExcelToList(file, Student)
        DAO.addStudent(students)
        return JSONResponse("Ajout données réalisé")
    except Exception as e:
        # Gérer l'exception ici (par exemple, enregistrer un journal)
        raise HTTPException(
            status_code=500, detail=f"Erreur BDD : {e}")