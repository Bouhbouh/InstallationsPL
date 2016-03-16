class Installation:
    
    """Classe définissant une installation caractérisée par :
    - son nom
    - son numéro
    - le nom de la commune
    - le code postal
    - du nom du lieu dit
    - du numéro de la voie
    - du nom de la voie
    - de sa longitude
    - de sa latitude"""
    
    def __init__(self, nom, numero, commune, codePostal, lieuDit, numeroVoie, nomVoie, longitude, latitude):
        self.nom = nom
        self.numero = numero
        self.commune = commune
        self.codePostal = codePostal
        self.lieuDit = lieuDit
        self.numeroVoie = numeroVoie
        self.nomVoie = nomVoie
        self.longitude = longitude
        self.latitude = latitude

    def __str__(self):
        return self.nom + " - " + self.numero + " - " + self.commune + " - " + self.codePostal + " - " + self.lieuDit + " - " + self.nomVoie + " - " + self.nomVoie + " - " + self.longitude + " - " + self.latitude

    def __eq__(self, other):
        return self.nom == other.nom and self.numero == other.numero and self.commune == other.commune and self.codePostal == other.codePostal and self.lieuDit == other.lieuDit and self.numeroVoie == other.numeroVoie and self.nomVoie == other.nomVoie and self.longitude == other.longitude and self.latitude == other.latitude

    def __hash__(self):
        return hash(('nom', self.nom, 'numero', self.numero, 'commune', self.commune, 'codePostal', self.codePostal, 'lieuDit', self.lieuDit, 'numeroVoie', self.numeroVoie, 'nomVoie', self.nomVoie, 'longitude', self.longitude, 'latitude', self.latitude))

