"""Importation"""
from itertools import count

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Création app
app = FastAPI(title="API Test")


class Tache(BaseModel):
    """Structure"""

    titre: str
    faite: bool = False


taches = {}
compteur_id = count(1)


@app.get("/")
def accueil():
    """Route test"""

    return {"message": "L'API est activé"}


@app.get("/taches")
def lister_taches():
    """Méthode GET"""

    return taches


@app.get("/taches/{tache_id}")
def lire_tache(tache_id: int):
    """Méthode GET/{id}"""

    if tache_id not in taches:
        raise HTTPException(status_code=404, detail="Tâche introuvable")
    return taches[tache_id]


@app.post("/taches")
def creer_tache(tache: Tache):
    """Méthode POST"""

    nouvel_id = next(compteur_id)
    taches[nouvel_id] = tache
    return {"id": nouvel_id, "tache": tache}


@app.put("/taches/{tache_id}")
def modifier_tache(tache_id: int, tache: Tache):
    """Méthode PUT"""

    if tache_id not in taches:
        raise HTTPException(status_code=404, detail="Tâche introuvable")
    taches[tache_id] = tache
    return {"id": tache_id, "tache": tache}


@app.delete("/taches/{tache_id}")
def supprimer_tache(tache_id: int):
    """Méthode DELETE"""

    if tache_id not in taches:
        raise HTTPException(status_code=404, detail="Tâche introuvable")
    del taches[tache_id]
    return {"message": "Tâche supprimée"}
