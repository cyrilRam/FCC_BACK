from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from APIs import imports, calcul
from APIs import staticTable

# TODO : ajouter le calcul qui va pour une period donné ajouter une ligne par eleve et par moyenne avec possibilité de télécharger execl avec les données de la periode

app = FastAPI()

app.include_router(staticTable.router, prefix="/api", tags=["staticTable"])
app.include_router(imports.router, prefix="/api", tags=["Imports"])
app.include_router(calcul.router, prefix="/api", tags=["Calcul"])

origin = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
