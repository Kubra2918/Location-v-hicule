from datetime import datetime

class Reservation:
    def __init__(
        self,
        id_reservation: str,
        id_client: str,
        id_vehicule: str,
        date_depart: str,
        date_retour: str,
        forfait_km,
        cout_journalier: float,
        prix_km_supp: float,
    ):
        self.id_reservation = id_reservation
        self.id_client = id_client
        self.id_vehicule = id_vehicule
        self.date_depart = date_depart
        self.date_retour = date_retour
        self.forfait_km = forfait_km
        self.cout_journalier = cout_journalier
        self.prix_km_supp = prix_km_supp
        self.cout_estime = self._calculer_cout_estime()

    def _calculer_cout_estime(self) -> float:
        date_depart_obj = datetime.strptime(self.date_depart, "%Y-%m-%d")
        date_retour_obj = datetime.strptime(self.date_retour, "%Y-%m-%d")

        nb_jours = (date_retour_obj - date_depart_obj).days
        if nb_jours <= 0:
            nb_jours = 1

        return nb_jours * self.cout_journalier

    def __str__(self) -> str:
        return (
            f"{self.id_reservation} | Client: {self.id_client} | "
            f"Véhicule: {self.id_vehicule} | "
            f"{self.date_depart} ➔ {self.date_retour} | "
            f"Forfait: {self.forfait_km} km | "
            f"Coût estimé: {self.cout_estime:.2f}€"
        )
