from fastapi import HTTPException
from models.formations import Formation
from typing import TypeVar, List, Type
import pandas as pd
import io


async def fromExcelToList(file, object_type: Type):
    # Lire le contenu du fichier comme des bytes
    file_content = await file.read()

    # Utiliser io.BytesIO pour créer un objet en mémoire à partir des bytes
    excel_data = io.BytesIO(file_content)
    df = pd.read_excel(excel_data)

    # Vérifier que les noms de colonnes correspondent à l'objet type
    if object_type == Formation:
        expected_columns = ['nom', 'promotion']
        if not df.columns.tolist() == expected_columns:
            raise HTTPException(
                status_code=400, detail="Le nom des colonnes du fichier Excel ne correspond pas à ce qui est attendu")

    objects = []
    for _, row in df.iterrows():
        if object_type == Formation:
            obj = Formation(nom=row['nom'], promotion=row['promotion'])
        else:
            raise ValueError("Type d'objet non recconu")
        objects.append(obj)

    return objects
