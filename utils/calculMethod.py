from datetime import datetime

from models.calcul.Moyennes import Moyenne
from models.imports.Results import Result
from models.static_tables.Student import Student


def calculMoyenne(periodstr):
    """
    on recupere la periode
    verification que bien données results pour cette periode
    si y a deja des données sur cette period on les supprime dans la table Moyennes
    on recupere les données pour cette periode dans la table results
    on calcule les moeynnes :
        -parcourt des students:
            -si present dans results moyenne des resultats
    :return:
    """
    dfResult, listResults = Result.get(periodstr)
    lstMoyennes = []
    date = datetime.now().date()

    if Moyenne.isDataExisting(periodstr):
        Moyenne.delete(periodstr)

    if listResults:
        dfNameStudent, listStudents = Student.get()
        df_moyenne_eleve = dfResult.groupby(['nom', 'prenom']).agg({'note': 'mean'}).reset_index()
        for index, row in df_moyenne_eleve.iterrows():
            student = wichStudentFromName(listStudents, [row['nom'], row['prenom']])
            lstMoyennes.append(Moyenne(student=student, periodstr=periodstr, moyenne=row['note'], date_calcul=date))

        Moyenne.add(lstMoyennes)

    else:
        raise Exception("Data non idsponible pour la periode " + periodstr + ". Veuillez alimneter les donnée")


def wichStudentFromName(listStudent, name):
    for student in listStudent:
        if student.nom == name[0] and student.prenom == name[1]:
            return student

    return None
