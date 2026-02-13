class TarifsManager:

    TARIFS = {
        4: {},
        5: {},
        6: {}
    }

    @classmethod
    def obtenir_tarif(cls, cylindree: int, forfait_km):
        return cls.TARIFS.get(cylindree, {}).get(forfait_km)

    @classmethod
    def afficher_grille(cls):
        for cylindree, forfaits in cls.TARIFS.items():
            print(f"{cylindree} cylindres :")
            for forfait, valeurs in forfaits.items():
                print(f"  {forfait} -> {valeurs}")
