import pandas as pd

from config.db import mydb
from models.formations.formations import Formation


def addFormations(formations):
    cursor = mydb.cursor()
    query = "INSERT INTO formation (nom, promotion) VALUES (%s, %s)"
    values = [(formation.nom, formation.promotion) for formation in formations]
    cursor.executemany(query, values)
    mydb.commit()
    cursor.close()


def uploadFormations(new_formations):
    cursor = mydb.cursor()
    update_query = "UPDATE formation SET nom = %s, promotion = %s WHERE id_formation = %s"
    update_values = [(formation.nom, formation.promotion, formation.id) for formation in new_formations]
    cursor.executemany(update_query, update_values)
    mydb.commit()
    cursor.close()


def deleteFormations(delete_formations):
    cursor = mydb.cursor()
    update_query = ("DELETE FROM formation WHERE id_formation = %s")
    delete_values = [(formation.id,) for formation in delete_formations]
    #update_values = [formation.id for formation in delete_formations]
    cursor.executemany(update_query, delete_values)
    mydb.commit()
    cursor.close()


def getFormations():
    cursor = mydb.cursor()
    query = "SELECT id_formation, nom, promotion FROM formation"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()

    # convertir liste de forma

    formations_list = [Formation(id=row[0], nom=row[1], promotion=row[2]) for row in result]

    # Convertir les résultats en DataFrame de pandas
    columns = ["id", "nom", "promotion"]
    formations_df = pd.DataFrame(result, columns=columns)

    return formations_df, formations_list
