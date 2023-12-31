import io

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse, StreamingResponse

from models.calcul.Moyennes import Moyenne
from models.imports.Results import Result
from models.static_tables.Student import Student
from utils.calcul.calculMethod import calculMoyenne, getDataForExcelMoyenne
from utils.calcul.pdf import merge_pdfs

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
        lst = Result.getDate()
        return lst
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erreur recup period : {e}")


@router.get("/lastCalculForPeriod/{period:str}")
async def getDateUpdate(period: str):
    try:
        return Moyenne.lastDateCalculPeriod(period)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erreur recup period : {e}")


@router.get("/uploadExcelMoyennes/{period:str}")
async def uploadMoyennes(period: str):
    try:
        df = getDataForExcelMoyenne(period)
        excel_content = io.BytesIO()
        df.to_excel(excel_content, index=False)
        excel_content.seek(0)
        return StreamingResponse(content=excel_content,
                                 media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                                 headers={"Content-Disposition": "attachment;filename=resultats.xlsx"})

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erreur extraction excel : {e}")


@router.get("/uploadPDFMoyennes/{period:str}")
async def uploadMoyennes(period: str):
    df_results, reults = Result.get(period)
    df_students, students = Student.get()
    merged_pdf_content = merge_pdfs(students, df_results, df_students)
    return StreamingResponse(merged_pdf_content, media_type="application/pdf")
