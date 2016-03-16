import csv

class Installation:
	"""
		Classe définissant une installation caractérisée par :
	    - son nom
	    - son numéro
	    - sa commune
	    - son code INSEE
	    - son code postal
	    - son numéro de voie
	    - son nom de voie
	    - sa location
    """
	def __init__(self, colonne):
		"""
			Constructeur de la class Installation
		"""
		tab_assoc = {
			"nom": "Nom usuel de l'installation",
			"num": "Numéro de l'installation",
			"commune": "Nom de la commune",
			"code_insee": "Code INSEE",
			"code_postal": "Code postal",
			"num_voie": "Numero de la voie",
			"nom_voie": "Nom de la voie",
			"location": "location"
		}

		for attribut in tab_assoc:
			for nom_colonne in colonne:
				if nom_colonne == tab_assoc[attribut]:
					exec("self." + attribut + "= colonne[nom_colonne]")


	def __str__(self):
		"""
			Méthode qui permet d'afficher une installation
		"""
		return "[" + self.nom + ", " + self.num + ", " + self.commune + ", " + self.code_insee + "]"
