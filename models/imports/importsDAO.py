from config.db import mydb


def cudMethod(query, values):
    cursor = mydb.cursor()
    cursor.executemany(query, values)
    mydb.commit()
    cursor.close()


def getDataStaticTable(query):
    cursor = mydb.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result
