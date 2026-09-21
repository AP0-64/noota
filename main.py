"""Importation"""
from itertools import count

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="API Test")


class User(BaseModel):
    """Structure"""

    titre: str
    faite: bool = False


users = {}
compteur_id = count(1)


@app.get("/")
def accueil():
    """Route test"""

    return {"message": "L'API est activé"}


@app.get("/users")
def lister_users():
    """Méthode GET"""

    return users


@app.get("/users/{user_id}")
def lire_user(user_id: int):
    """Méthode GET/{id}"""

    if user_id not in users:
        raise HTTPException(status_code=404, detail="Utilisateur introuvable")

    return users[user_id]


@app.post("/users")
def creer_user(user: User):
    """Méthode POST"""

    nouvel_id = next(compteur_id)
    users[nouvel_id] = user

    return {"id": nouvel_id, "user": user}


@app.put("/users/{user_id}")
def modifier_user(user_id: int, user: User):
    """Méthode PUT"""

    if user_id not in users:
        raise HTTPException(status_code=404, detail="Utilisateur introuvable")
    users[user_id] = user

    return {"id": user_id, "user": user}


@app.delete("/users/{user_id}")
def supprimer_user(user_id: int):
    """Méthode DELETE"""

    if user_id not in users:
        raise HTTPException(status_code=404, detail="Utilisateur introuvable")
    del users[user_id]

    return {"message": "Utilisateur supprimée"}
