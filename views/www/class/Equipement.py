class Equipement:
    
    """Classe définissant un equipement caractérisée par :
    - son nom
    - son numéro
    - son type
    - le numéro de l'installation"""
    
    def __init__(self, nom, numero, type, numeroInstallation):
        self.nom = nom
        self.numero = numero
        self.type = type
        self.numeroInstallation = numeroInstallation

    def __str__(self):
        return self.nom + " - " + self.numero + " - " + self.type + " - " + self.numeroInstallation

    def __eq__(self, other):
        return self.nom == other.nom and self.numero == other.numero and self.type == other.type and self.numeroInstallation == other.numeroInstallation

    def __hash__(self):
        return hash(('nom', self.nom, 'numero', self.numero, 'type', self.type, 'numeroInstallation', self.numeroInstallation))

