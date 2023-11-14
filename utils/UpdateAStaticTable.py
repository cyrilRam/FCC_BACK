import models.formations.formationsDAO as formationDAO
from models.formations.formations import Formation


def updateTable(newData):
    """
    TODO: verifier que les 3 liste nous donnent bien des listes de formation
    :param newData:
    :return:
    """
    if type(newData[0]) == Formation:
        df, old_objects = formationDAO.getFormations()
        objects_to_delete = []
        for old_obj in old_objects:
            isIn = False
            for new_obj in newData:
                if old_obj.id == new_obj.id:
                    isIn = True
            if not isIn:
                objects_to_delete.append(old_obj)

        objects_to_add = [obj for obj in newData if obj.id is None]

        objects_to_updtade = []

        for new_obj in newData:
            for old_ob in old_objects:
                if new_obj.id == old_ob.id:
                    if new_obj.nom != old_ob.nom or new_obj.promotion != old_ob.promotion:
                        objects_to_updtade.append(new_obj)



        formationDAO.deleteFormations(objects_to_delete) if objects_to_delete else None
        formationDAO.addFormations(objects_to_add) if objects_to_add else None
        formationDAO.uploadFormations(objects_to_updtade) if objects_to_updtade else None

    return
