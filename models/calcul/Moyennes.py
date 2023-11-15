from datetime import datetime

import pandas as pd
from pydantic import BaseModel

import models.CRUD as CRUD
from models.static_tables.Student import Student


class Moyenne(BaseModel):
    student: Student
    periodstr: str
    moyenne: float
    date_calcul: datetime

    @staticmethod
    def add(listImports):
        query = "INSERT INTO moyennes (id_student, periodstr,moyenne,date_calcul) VALUES (%s, %s,%s,%s)"
        values = [(result.student.id, result.periodstr, result.moyenne, result.date_calcul) for result in
                  listImports]
        CRUD.cudMethod(query, values)

    def isDataExisting(period):
        query = "SELECT * FROM moyennes WHERE periodstr=%s"
        params = (period,)
        result = CRUD.getDataStaticTable(query, params)
        return True if result else False

    @staticmethod
    def delete(period):
        query = ("DELETE FROM moyennes WHERE periodstr = %s")
        values = [(period,)]
        CRUD.cudMethod(query, values)

    @staticmethod
    def getData(period):
        query = "SELECT * FROM moyennes WHERE periodstr = %s"
        values = (period,)
        result = CRUD.getDataStaticTable(query, values)
        columns = ["id_student", "periodstr", "moyenne", "date"]
        staticDf = pd.DataFrame(result, columns=columns)
        return staticDf
