from models.imports.Results import Result


def importDataFromImportFile(newData):
    """
    -checker si les daes de new data sont deja présentes dans la table
        -si non on fait le add classique
        -si oui on supprime ls data de cette periode
    :param newData:
    :return:
    """
    df, actualData = Result.get()
    if checkIfDataForThisPeriodExisting(newData, actualData):
        deleteData = [result for result in actualData if result.periodstr == newData[0].periodstr]
        Result.delete(deleteData)
        Result.add(newData)
    else:
        Result.add(newData)

    objToDelete = []


def checkIfDataForThisPeriodExisting(newData, actualData):
    existing_periods = [result.periodstr for result in actualData]
    return newData[0].periodstr in existing_periods
