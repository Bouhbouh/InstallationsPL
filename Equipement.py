import csv
from Installation import Installation

class Equipement:
    """
        Classe définissant un équipement caractérisé par :
        - son numéro d'installation
        - son nom
        - son id
        - le nom de l'équipement
    """
    def __init__(self, colonne):
        """
            Constructeur de la classe équipement
        """
        tab_assoc = {
            "num": "InsNumeroInstall",
            "nom": "InsNom",
            "id_equipement": "EquipementId",
            "nom_equip": "EquNom"
        }

        for attribut in tab_assoc:
            for nom_colonne in colonne:
                if nom_colonne == tab_assoc[attribut]:
                    exec("self." + attribut + "= colonne[nom_colonne]")


    def __str__(self):
        """
            Méthode qui permet d'afficher un équipement
        """
        return "[" + self.num + ", " + self.nom + ", " + self.id_equipement + ", " + self.nom_equip + "]"