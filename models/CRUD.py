from config.db import mydb


def cudMethod(query, values):
    cursor = mydb.cursor()
    cursor.executemany(query, values)
    mydb.commit()
    cursor.close()


def getDataStaticTable(query, params=None):
    cursor = mydb.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)

    result = cursor.fetchall()
    cursor.close()
    return result
