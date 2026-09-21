from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Création app
app = FastAPI(title="API Test")


# Format
class Tache(BaseModel):
    titre: str
    faite: bool = False


# DB (un simple dictionnaire en mémoire)
taches = {}
prochain_id = 1


@app.get("/")
def accueil():
    return {"message": "Bienvenue sur l'API Todo !"}


@app.get("/taches")
def lister_taches():
    return taches


@app.get("/taches/{tache_id}")
def lire_tache(tache_id: int):
    if tache_id not in taches:
        raise HTTPException(status_code=404, detail="Tâche introuvable")
    return taches[tache_id]


@app.post("/taches")
def creer_tache(tache: Tache):
    global prochain_id
    taches[prochain_id] = tache
    prochain_id += 1
    return {"id": prochain_id - 1, "tache": tache}


@app.put("/taches/{tache_id}")
def modifier_tache(tache_id: int, tache: Tache):
    if tache_id not in taches:
        raise HTTPException(status_code=404, detail="Tâche introuvable")
    taches[tache_id] = tache
    return {"id": tache_id, "tache": tache}


@app.delete("/taches/{tache_id}")
def supprimer_tache(tache_id: int):
    if tache_id not in taches:
        raise HTTPException(status_code=404, detail="Tâche introuvable")
    del taches[tache_id]
    return {"message": "Tâche supprimée"}
