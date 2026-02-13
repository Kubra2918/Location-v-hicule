import json
from models import Client, Vehicule


def charger_clients(fichier: str = "clients.json") -> list:
    with open(fichier, "r", encoding="utf-8") as f:
        donnees = json.load(f)

    clients = [Client.from_dict(d) for d in donnees]
    return clients


def charger_vehicules(fichier: str = "vehicules.json") -> list:
    with open(fichier, "r", encoding="utf-8") as f:
        donnees = json.load(f)

    vehicules = [Vehicule.from_dict(d) for d in donnees]
    return vehicules
