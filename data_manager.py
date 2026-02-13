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

from models import Reservation


def charger_reservations(fichier: str = "reservations.json") -> list:
    with open(fichier, "r", encoding="utf-8") as f:
        donnees = json.load(f)

    reservations = [
        Reservation(
            id_reservation=d["id_reservation"],
            id_client=d["id_client"],
            id_vehicule=d["id_vehicule"],
            date_depart=d["date_depart"],
            date_retour=d["date_retour"],
            forfait_km=d["forfait_km"],
            cout_journalier=d["cout_journalier"],
            prix_km_supp=d["prix_km_supp"],
        )
        for d in donnees
    ]

    return reservations


def generer_id_reservation(reservations: list) -> str:
    if not reservations:
        return "R0001"

    derniers_ids = [int(r.id_reservation[1:]) for r in reservations]
    nouveau_id = max(derniers_ids) + 1
    return f"R{nouveau_id:04d}"


def sauvegarder_reservation(reservation: Reservation, fichier: str = "reservations.json"):
    reservations = charger_reservations(fichier)

    reservations.append(reservation)

    donnees = [
        {
            "id_reservation": r.id_reservation,
            "id_client": r.id_client,
            "id_vehicule": r.id_vehicule,
            "date_depart": r.date_depart,
            "date_retour": r.date_retour,
            "forfait_km": r.forfait_km,
            "cout_journalier": r.cout_journalier,
            "prix_km_supp": r.prix_km_supp,
            "cout_estime": r.cout_estime,
        }
        for r in reservations
    ]

    with open(fichier, "w", encoding="utf-8") as f:
        json.dump(donnees, f, indent=2)


def filtrer_reservations_par_client(reservations: list, id_client: str) -> list:
    return [r for r in reservations if r.id_client == id_client]
