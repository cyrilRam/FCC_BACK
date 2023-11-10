
from config.db import mydb
import pandas as pd
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

    # Convertir les résultats en DataFrame de pandas
    columns = ["id", "nom", "promotion"]
    formations_df = pd.DataFrame(result, columns=columns)

    return formations_df
