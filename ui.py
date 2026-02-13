def afficher_menu():
    print("============================================================")
    print("SYSTÈME DE LOCATION DE VÉHICULES")
    print("============================================================")
    print("1. Afficher les clients")
    print("2. Afficher les véhicules")
    print("3. Créer une réservation")
    print("4. Afficher la grille tarifaire")
    print("5. Afficher toutes les réservations")
    print("6. Afficher les réservations d'un client")
    print("7. Quitter")
    print("============================================================")


def demander_choix_menu():
    return input("Votre choix : ")


def afficher_clients(clients):
    print("============================================================")
    print("LISTE DES CLIENTS")
    print("============================================================")
    for c in clients:
        print(str(c))
    print("============================================================")


def afficher_vehicules(vehicules):
    print("============================================================")
    print("LISTE DES VÉHICULES")
    print("============================================================")
    for v in vehicules:
        print(str(v))
    print("============================================================")

def afficher_reservations(reservations):
    print("============================================================")
    print("LISTE DES RÉSERVATIONS")
    print("============================================================")
    for r in reservations:
        print(str(r))
    print("============================================================")


def afficher_reservations_client(reservations, id_client):
    print("============================================================")
    print(f"RÉSERVATIONS DU CLIENT {id_client}")
    print("============================================================")

    trouve = False
    for r in reservations:
        if r.id_client == id_client:
            print(str(r))
            trouve = True

    if not trouve:
        print("Aucune réservation trouvée.")

    print("============================================================")
