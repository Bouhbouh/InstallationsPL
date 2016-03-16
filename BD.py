import mysql.connector as sql
from Activite import Activite
from Installation import Installation
from Equipement import Equipement
from LectureCSV import LectureCSV

class BD:

	"""
		Constructeur de la classe BD
		- Il permet d'initialiser la connexion à la base de données
	"""
	def __init__(self):
		config = {
		  'user': 'E145355U',
		  'password': 'E145355U',
		  'database': 'E145355U',
		  'host': 'infoweb'
		}

		try:
			self.connexion = sql.connect(**config)
			self.cur = self.connexion.cursor()
		except sql.Error as err:
			 print("Something went wrong in connexion: {}".format(err))

	"""
		Fonction qui permet l'insertion de données dans la table activite
	"""
	def insert_activite(self, num, nom, id_equipement):
		try:
			self.cur.execute("INSERT INTO activite(num, nom, id_equipement) VALUES(%s, %s, %s)", (num, nom, id_equipement))
			self.connexion.commit()
		except sql.Error as err:
			print("Something went wrong in activite: {}".format(err))


	"""
		Fonction qui permet l'insertion de données dans la table installation
	"""
	def insert_installation(self, nom, num, commune, code_insee, code_postal, num_voie, nom_voie, location):
		try:
			self.cur.execute("INSERT INTO installation VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", (nom, num, commune, code_insee, code_postal, num_voie, nom_voie, location))
			self.connexion.commit()
		except sql.Error as err:
			print("Something went wrong in installation: {}".format(err))

	"""
		Fonction qui récupère toutes les informations d'une installation
	"""
	def get_installation(self, identifiant):
		results = []
		try:
			self.cur.execute("SELECT i.num, i.nom, i.commune, a.nom, e.nom_equip, i.num_voie, i.nom_voie, i.code_postal, i.commune, i.location FROM installation i JOIN equipement e ON i.num = e.num JOIN activite a ON e.id_equipement = a.id_equipement WHERE i.num = {}".format(identifiant))
			for i in self.cur:
				results.append(i)
		except sql.Error as err:
			print("Something went wrong in get_installation: {}".format(err))
		return results


	"""
		Fonction qui permet l'insertion de données dans la table equipement
	"""
	def insert_equipement(self, nom, num, id_equipement, nom_equip):
		try:
			self.cur.execute("INSERT INTO equipement VALUES(%s, %s, %s, %s)", (nom, num, id_equipement, nom_equip))
			self.connexion.commit()
		except sql.Error as err:
			print("Something went wrong in equipement: {}".format(err))


	"""
		Recherche à partir du nom de l'activité et du lieu
	"""
	def recherche(self, nomActivite, lieu):
		results = []
		try:
			self.cur.execute("SELECT i.num, i.nom, e.id_equipement, e.nom_equip, a.num, a.nom, i.num_voie, i.nom_voie, i.code_postal, i.commune, i.location FROM installation i JOIN equipement e ON i.num = e.num JOIN activite a ON e.id_equipement = a.id_equipement WHERE i.commune = %s AND a.nom LIKE %s", (lieu, '%' + nomActivite + '%'))
			for i in self.cur:
				results.append(i)
			self.connexion.commit()
		except sql.Error as err:
			print("Something went wrong in research: {}".format(err))
		return results
	


# MAIN #
base = BD()

"""
installations = LectureCSV.lecture('data/installations.csv', Installation)
for instal in installations:
	print(instal)
	base.insert_installation(instal.nom, instal.num, instal.commune, instal.code_insee, instal.code_postal, instal.num_voie, instal.nom_voie, instal.location)

equipements = LectureCSV.lecture('data/equipements.csv', Equipement)
for eq in equipements:
	print(eq)
	base.insert_equipement(eq.num, eq.nom, eq.id_equipement, eq.nom_equip)

activites = LectureCSV.lecture('data/activites.csv', Activite)
for activite in activites:
	print(activite)
	base.insert_activite(activite.num, activite.nom, activite.id_equipement)

res = base.recherche('vtt', 'Nantes')
for i in res:
	print(i)
print(base.get_installation(440010002))
"""