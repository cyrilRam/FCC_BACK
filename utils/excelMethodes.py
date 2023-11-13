import io
from typing import Type

import pandas as pd
from fastapi import HTTPException

from models.formations.formations import Formation
from models.students.Student import Student

dicoColumn = {
    Formation: ['nom', 'promotion'],
    Student: ['nom', 'prenom', 'age']
}


async def fromExcelToList(file, object_type: Type):
    # Lire le contenu du fichier comme des bytes
    file_content = await file.read()

    # Utiliser io.BytesIO pour créer un objet en mémoire à partir des bytes
    excel_data = io.BytesIO(file_content)
    df = pd.read_excel(excel_data)

    # Vérifier que les noms de colonnes correspondent à l'objet type
    expected_columns = dicoColumn.get(object_type)
    if not df.columns.tolist() == expected_columns:
        raise HTTPException(
            status_code=400, detail="Le nom des colonnes du fichier Excel ne correspond pas à ce qui est attendu")

    objects = []
    for _, row in df.iterrows():
        if object_type in dicoColumn:
            columns = dicoColumn[object_type]

            obj_data = {col: row[col] for col in columns}
            obj_data['id'] = None
            # Exclure le champ 'id' si présent

            obj = object_type(**obj_data)
        else:
            raise ValueError("Type d'objet non reconnu")
        objects.append(obj)

    return objects
