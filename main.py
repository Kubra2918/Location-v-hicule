from data_manager import (
    charger_clients,
    charger_vehicules,
    charger_reservations,
    generer_id_reservation,
    sauvegarder_reservation,
)
from models import Reservation, TarifsManager
from ui import (afficher_menu, demander_choix_menu, afficher_clients, afficher_vehicules, afficher_reservations, afficher_reservations_client, nettoyer_terminal,)


def main():
    clients = charger_clients()
    vehicules = charger_vehicules()

    while True:
        afficher_menu()
        choix = demander_choix_menu()

        if choix in {"1", "2", "3", "4", "5", "6", "7"}:
            nettoyer_terminal()
        if choix == "1":
            afficher_clients(clients)

        elif choix == "2":
            afficher_vehicules(vehicules)

        elif choix == "3":
            reservations = charger_reservations()

            afficher_clients(clients)
            id_client = input("Entrez l'ID du client : ")

            afficher_vehicules(vehicules)
            id_vehicule = input("Entrez l'ID du véhicule : ")

            date_depart = input("Date de départ (AAAA-MM-JJ) : ")
            date_retour = input("Date de retour (AAAA-MM-JJ) : ")

            print("Forfaits disponibles : 100, 200, 300, +300")
            forfait_km = input("Entrez le forfait kilométrique : ")

            vehicule = next(v for v in vehicules if v.id_vehicule == id_vehicule)

            if forfait_km.isdigit():
                forfait_km = int(forfait_km)

            tarif = TarifsManager.obtenir_tarif(vehicule.cylindree, forfait_km)

            if not tarif:
                print("Tarif invalide.")
                continue

            cout_journalier, prix_km_supp = tarif

            nouvel_id = generer_id_reservation(reservations)

            reservation = Reservation(
                id_reservation=nouvel_id,
                id_client=id_client,
                id_vehicule=id_vehicule,
                date_depart=date_depart,
                date_retour=date_retour,
                forfait_km=forfait_km,
                cout_journalier=cout_journalier,
                prix_km_supp=prix_km_supp,
            )

            print("============================================================")
            print("RÉCAPITULATIF")
            print("============================================================")
            print(reservation)

            confirmation = input("Sauvegarder cette réservation ? (o/n) : ")

            if confirmation.lower() == "o":
                sauvegarder_reservation(reservation)
                print("Réservation enregistrée.")
            else:
                print("Réservation annulée.")

        elif choix == "5":
            reservations = charger_reservations()
            afficher_reservations(reservations)

        elif choix == "6":
            reservations = charger_reservations()
            id_client = input("Entrez l'ID du client : ")
            afficher_reservations_client(reservations, id_client)

        elif choix == "7":
            print("Au revoir.")
            break

        else:
            print("Option non encore implémentée.")


if __name__ == "__main__":
    main()
