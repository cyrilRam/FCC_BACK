from models.static_tables.Formation import Formation


def updateTable(newData):
    """
    TODO: verifier que les 3 liste nous donnent bien des listes de formation
    :param newData:
    :return:
    """
    if type(newData[0]) == Formation:
        df, old_objects = Formation.get()
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

        Formation.delete(objects_to_delete) if objects_to_delete else None
        Formation.add(objects_to_add) if objects_to_add else None
        Formation.update(objects_to_updtade) if objects_to_updtade else None

    return
