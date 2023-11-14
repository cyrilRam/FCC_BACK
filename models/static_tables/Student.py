from typing import Optional

import pandas as pd
from pydantic import BaseModel

import models.static_tables.staticDAO as staticDAO


class Student(BaseModel):
    id: Optional[int]
    nom: str
    prenom: str
    age: int

    @staticmethod
    def add(listStatic):
        query = "INSERT INTO student (nom, prenom,age) VALUES (%s, %s,%s)"
        values = [(student.nom, student.prenom, student.age) for student in listStatic]
        staticDAO.cudMethod(query, values)

    @staticmethod
    def get():
        query = "SELECT id_student, nom, prenom,age FROM student"
        result = staticDAO.getDataStaticTable(query)
        # convertir liste de forma
        staticList = [Student(id=row[0], nom=row[1], prenom=row[2], age=row[3]) for row in result]
        # Convertir les résultats en DataFrame de pandas
        columns = ["id", "nom", "prenom", "age"]
        staticDf = pd.DataFrame(result, columns=columns)
        return staticDf, staticList

    @staticmethod
    def delete(listStatic):
        query = ("DELETE FROM student WHERE id_student = %s")
        values = [(student.id,) for student in listStatic]
        staticDAO.cudMethod(query, values)

    @staticmethod
    def update(listStatic):
        query = "UPDATE student SET nom = %s, prenom = %s,age=%s WHERE id_student = %s"
        values = [(student.nom, student.promotion, student.id) for student in listStatic]
        staticDAO.cudMethod(query, values)
