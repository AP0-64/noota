# API Test

API CRUD réalisée avec FastAPI pour gérer des utilisateurs.
Les données sont stockées en mémoire grâce à un dictionnaire : elles sont perdues à chaque redémarrage.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Lancement

```bash
fastapi dev main.py
```

L'API est disponible sur <http://127.0.0.1:8000> et la documentation interactive sur <http://127.0.0.1:8000/docs>.

## Routes

| Méthode | Route              | Description                    |
|---------|--------------------|--------------------------------|
| GET     | `/`                | Vérifie que l'API est active   |
| GET     | `/users`           | Liste les utilisateurs         |
| GET     | `/users/{user_id}` | Récupère un utilisateur        |
| POST    | `/users`           | Crée un utilisateur            |
| PUT     | `/users/{user_id}` | Modifie un utilisateur         |
| DELETE  | `/users/{user_id}` | Supprime un utilisateur        |

Exemple de corps pour `POST` / `PUT` :

```json
{
  "titre": str,
  "faite": bool
}
```
