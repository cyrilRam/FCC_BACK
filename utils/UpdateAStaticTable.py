from models.static_tables.Formation import Formation
from models.static_tables.Student import Student


def updateTable(newData):
    """
    TODO: verifier que les 3 liste nous donnent bien des listes de formation
    :param newData:
    :return:
    """

    objects_to_delete, objects_to_updtade = findObjectToDeleteAndUpdate(newData)
    objects_to_add = [obj for obj in newData if obj.id is None]

    if type(newData[0]) == Formation:
        Formation.delete(objects_to_delete) if objects_to_delete else None
        Formation.add(objects_to_add) if objects_to_add else None
        Formation.update(objects_to_updtade) if objects_to_updtade else None
    elif type(newData[0]) == Student:
        Student.delete(objects_to_delete) if objects_to_delete else None
        Student.add(objects_to_add) if objects_to_add else None
        Student.update(objects_to_updtade) if objects_to_updtade else None


def findObjectToDeleteAndUpdate(newData):
    if type(newData[0]) == Formation:
        df, old_objects = Formation.get()
    elif type(newData[0]) == Student:
        df, old_objects = Student.get()

    objects_to_delete = []
    for old_obj in old_objects:
        isIn = False
        for new_obj in newData:
            if old_obj.id == new_obj.id:
                isIn = True
        if not isIn:
            objects_to_delete.append(old_obj)

    objects_to_updtade = []
    for new_obj in newData:
        for old_ob in old_objects:
            # si meme id mais que diffrenets alors on a des modifs
            if new_obj.id == old_ob.id and new_obj != old_ob:
                objects_to_updtade.append(new_obj)

    return objects_to_delete, objects_to_updtade
