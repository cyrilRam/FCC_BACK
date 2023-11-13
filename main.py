from typing import List
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi import FastAPI
from APIs import staticTable

# #
# TODO:-afficher liste des formation et possibiliter modifier noms et promo
# TODO:-ajouter nouvelle ligne formation et ajouter a la base
# TODO:-telecharger toutes les formations dans un excel

app = FastAPI()

app.include_router(staticTable.router, prefix="/api", tags=["staticTable"])

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
