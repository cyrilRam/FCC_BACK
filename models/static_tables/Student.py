from typing import Optional

import pandas as pd
from pydantic import BaseModel

import models.CRUD as CRUD


class Student(BaseModel):
    id: Optional[int]
    nom: str
    prenom: str
    age: int

    @staticmethod
    def add(listStatic):
        query = "INSERT INTO student (nom, prenom,age) VALUES (%s, %s,%s)"
        values = [(student.nom.lower(), student.prenom.lower(), student.age) for student in listStatic]
        CRUD.cudMethod(query, values)

    @staticmethod
    def get():
        query = "SELECT id_student, nom, prenom,age FROM student"
        result = CRUD.getDataStaticTable(query)
        staticList = [Student(id=row[0], nom=row[1], prenom=row[2], age=row[3]) for row in result]
        columns = ["id", "nom", "prenom", "age"]
        staticDf = pd.DataFrame(result, columns=columns)

        return staticDf, staticList

    @staticmethod
    def delete(listStatic):
        query = ("DELETE FROM student WHERE id_student = %s")
        values = [(student.id,) for student in listStatic]
        CRUD.cudMethod(query, values)

    @staticmethod
    def update(listStatic):
        query = "UPDATE student SET nom = %s, prenom = %s,age=%s WHERE id_student = %s"
        values = [(student.nom.lower(), student.prenom.lower(), student.age, student.id) for student in
                  listStatic]
        CRUD.cudMethod(query, values)

    def __eq__(self, other):
        """
        Override the equality operator to compare based on nom,age et prenom fields.
        """
        return (
                isinstance(other, Student)
                and self.nom == other.nom
                and self.prenom == other.prenom
                and self.age == other.age
        )
