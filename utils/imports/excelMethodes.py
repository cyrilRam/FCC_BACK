import io
from typing import Type

import pandas as pd

from models.imports.Results import Result
from models.static_tables.Formation import Formation
from models.static_tables.Student import Student

dicoColumn = {
    Formation: ['nom', 'promotion'],
    Student: ['nom', 'prenom', 'age'],
    Result: ['periodstr', 'nom', 'prenom', 'note']
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
        raise NotGoodNameColumns("Les nom des colonnes ne correspond pas a ce qui est attendu")

    objects = []
    for _, row in df.iterrows():
        if object_type in dicoColumn:
            columns = dicoColumn[object_type]
            obj_data = {col: row[col] for col in columns}
            obj = object_type(**obj_data)
        else:
            raise ValueError("Type d'objet non reconnu")
        objects.append(obj)

    return df, objects


class NotGoodNameColumns(Exception):
    pass
