class TarifsManager:

    TARIFS = {
        4: {100: (35.0, 0.25),
            200: (50.0, 0.20),
            300: (65.0, 0.15),
            "+300": (80.0, 0.10),
        },
        5: { 100: (45.0, 0.30),
            200: (60.0, 0.25),
            300: (75.0, 0.20),
            "+300": (95.0, 0.15),
        },
        6: {
            100: (60.0, 0.40),
            200: (80.0, 0.35),
            300: (100.0, 0.30),
            "+300": (120.0, 0.25),
        },
    }

    @classmethod
    def obtenir_tarif(cls, cylindree: int, forfait_km):
        if cylindree not in cls.TARIFS:
            return None
        return cls.TARIFS.get(cylindree, {}).get(forfait_km)

    @classmethod
    def afficher_grille(cls):
        print("======================================================================")
        print("GRILLE TARIFAIRE")
        print("======================================================================")
        print("Cylindrée  Forfait  Coût/jour  Prix km supp.")
        print("----------------------------------------------------------------------")

        for cylindree, forfaits in cls.TARIFS.items():
            print(f"{cylindree} cylindres :")
            for forfait, valeurs in forfaits.items():
                print(f"  {forfait} -> {valeurs}")
