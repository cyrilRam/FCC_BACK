from models.imports.Results import Result
from models.static_tables.Student import Student


def importDataFromImportFile(newData):
    """
    -checker si les daes de new data sont deja présentes dans la table
        -si non on fait le add classique
        -si oui on supprime ls data de cette periode
    :param newData:
    :return:
    """
    possible, listNomsInconnus = checkIfStudentNotinDataBase(newData)
    period = newData[0].periodstr
    if possible:
        if Result.isDataExisting(period):
            Result.delete(period)
            Result.add(newData)
        else:
            Result.add(newData)
    else:
        raise Exception("Les (noms,prenoms) suivants ne sont pas dans la data base" + str(listNomsInconnus))


def checkIfStudentNotinDataBase(newData):
    """

    :param newData:
    :return: True si c'est vide la diff
    """
    dfStudent, listStudents = Student.get()
    listName = [(student.nom, student.prenom) for student in listStudents]
    nomPrenomInResult = [(d.nom.lower(), d.prenom.lower()) for d in newData]
    result = set(nomPrenomInResult) - set(listName)
    if not result:
        return True, set()
    else:
        return False, result
