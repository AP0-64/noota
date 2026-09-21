from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# On crée l'application
app = FastAPI(title="API Todo toute simple")


# Le format d'une tâche envoyée par le client
class Tache(BaseModel):
    titre: str
    faite: bool = False


# Notre "base de données" : un simple dictionnaire en mémoire
# (tout est perdu quand on arrête le serveur)
taches = {}
prochain_id = 1


@app.get("/")
def accueil():
    return {"message": "Bienvenue sur l'API Todo !"}


# Lister toutes les tâches
@app.get("/taches")
def lister_taches():
    return taches


# Récupérer une seule tâche grâce à son id
@app.get("/taches/{tache_id}")
def lire_tache(tache_id: int):
    if tache_id not in taches:
        raise HTTPException(status_code=404, detail="Tâche introuvable")
    return taches[tache_id]


# Créer une nouvelle tâche
@app.post("/taches")
def creer_tache(tache: Tache):
    global prochain_id
    taches[prochain_id] = tache
    prochain_id += 1
    return {"id": prochain_id - 1, "tache": tache}


# Modifier une tâche existante
@app.put("/taches/{tache_id}")
def modifier_tache(tache_id: int, tache: Tache):
    if tache_id not in taches:
        raise HTTPException(status_code=404, detail="Tâche introuvable")
    taches[tache_id] = tache
    return {"id": tache_id, "tache": tache}


# Supprimer une tâche
@app.delete("/taches/{tache_id}")
def supprimer_tache(tache_id: int):
    if tache_id not in taches:
        raise HTTPException(status_code=404, detail="Tâche introuvable")
    del taches[tache_id]
    return {"message": "Tâche supprimée"}
