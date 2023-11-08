
from config.db import mydb
def addFormations(formations):
    cursor = mydb.cursor()
    query = "INSERT INTO formation (nom, promotion) VALUES (%s, %s)"
    values = [(formation.nom, formation.promotion) for formation in formations]
    cursor.executemany(query, values)
    mydb.commit()
    cursor.close()

def getFormations():
    cursor = mydb.cursor()
    query = "SELECT id_formation, nom, promotion FROM formation"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result
