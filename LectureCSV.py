import csv
from Installation import Installation
from Equipement import Equipement
from Activite import Activite

class LectureCSV:
	"""
		Classe qui va permettre de lire un fichier CSV
	"""
	@staticmethod
	def lecture(fichier, classe):
		"""
			Méthode qui permet de lire un fichier CSV et de créer des objets grâce aux données de celui-ci et de la classe passée en paramètre
		"""
		tableau = []

		try:
			# On ouvre le fichier CSV
			with open(fichier, 'r') as csvfile:
				reader = csv.DictReader(csvfile)
				# On créer les installations et on les stock dans une liste
				for row in reader:
					tableau.append(classe(row))
					#print(classe(row))

			return tableau
		except Exception as e:
			print(e)
