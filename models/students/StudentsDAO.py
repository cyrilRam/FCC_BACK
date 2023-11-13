from config.db import mydb
import pandas as pd

def addStudent(students):
    cursor = mydb.cursor()
    query = "INSERT INTO student (nom, prenom,age) VALUES (%s, %s,%s)"
    values = [(student.nom, student.prenom,student.age) for student in students]
    cursor.executemany(query, values)
    mydb.commit()
    cursor.close()

def getStudents():
    cursor = mydb.cursor()
    query = "SELECT id_student, nom, prenom,age FROM student"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()

    # Convertir les résultats en DataFrame de pandas
    columns = ["id", "nom", "prenom","age"]
    student_df = pd.DataFrame(result, columns=columns)

    return student_df