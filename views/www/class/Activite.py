class Activite:
    
    """Classe définissant une activité caractérisée par :
    - son nom
    - son numéro
    - le numéro de l'équipement"""
    
    def __init__(self, nom, numero, numeroEquipement):
        self.nom = nom
        self.numero = numero
        self.numeroEquipement = numeroEquipement

    def __str__(self):
        return self.nom + " - " + self.numero + " - " + self.numeroEquipement
    
    def __eq__(self, other):
        return self.nom == other.nom and self.numero == other.numero and self.numeroEquipement == other.numeroEquipement

    def __hash__(self):
        return hash(('nom', self.nom, 'numero', self.numero, 'numeroEquipement', self.numeroEquipement))

