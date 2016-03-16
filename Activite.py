import csv
from Equipement import Equipement

class Activite:
	"""
		Classe définissant une activité caractérisée par :
		- son id qui sert de clé primaire
		- son numéro
		- son nom
		- l'id de l'équipement
	"""
	def __init__(self, colonne):
		"""
			Constructeur de la classe activité
		"""
		tab_assoc = {
			"num": "ActCode",
			"nom": "ActLib",
			"id_equipement": "EquipementId"
		}

		for attribut in tab_assoc:
			for nom_colonne in colonne:
				if nom_colonne == tab_assoc[attribut]:
					exec("self." + attribut + "= colonne[nom_colonne]")


	def __str__(self):
		"""
			Méthode qui permet d'afficher une activité
		"""
		return "[" + self.num + ", " + self.nom + ", " + self.id_equipement + "]"

	