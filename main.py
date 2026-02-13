from data_manager import charger_clients, charger_vehicules
from ui import afficher_menu, demander_choix_menu, afficher_clients, afficher_vehicules



def main():
    clients = charger_clients()
    vehicules = charger_vehicules()


    while True:
        afficher_menu()
        choix = demander_choix_menu()

        if choix == "1":
            afficher_clients(clients)
        elif choix == "2":      
            afficher_vehicules(vehicules)
        elif choix == "7":
            print("Au revoir.")
            break
        else:
            print("Option non encore implémentée.")


if __name__ == "__main__":
    main()
