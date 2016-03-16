import mysql.connector
from mysql.connector import errorcode

class BaseDonnees:

   """Classe définissant une base de données caractérisée par :
   - sa connexion"""

   def __init__(self):
      connexion = None

   def connexion(self):
      try:
         BaseDonnees.connexion = mysql.connector.connect(user='E146223N', password='E146223N', database='E146223N', host='infoweb')
      except mysql.connector.Error as erreur:
         if erreur.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Le couple login / mot de passe n'est pas correct.")
         elif erreur.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de données n'éxiste pas.")
         else:
            print(erreur)
      else:
         print("La connexion a corectement été ouverte.")
      
   def deconnexion(self):
      BaseDonnees.connexion.close()
      print("La connexion a corectement été fermée.")

   def addInstallation(self, listeInstallations):
      uneInstallation = ("INSERT INTO installation VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
      curseurInstallation = BaseDonnees.connexion.cursor()
      for installation in listeInstallations:
         dataInstallation = (installation.nom, installation.numero, installation.commune, installation.codePostal, installation.lieuDit, installation.numeroVoie, installation.nomVoie, installation.longitude, installation.latitude)
         curseurInstallation.execute(uneInstallation, dataInstallation)
         BaseDonnees.connexion.commit()

   def addEquipement(self, listeEquipements):
      unEquipement = ("INSERT INTO equipement VALUES (%s, %s, %s, %s);")
      curseurEquipement = BaseDonnees.connexion.cursor()
      for equipement in listeEquipements:
         dataEquipement = (equipement.nom, equipement.numero, equipement.type, equipement.numeroInstallation)
         curseurEquipement.execute(unEquipement, dataEquipement)
         BaseDonnees.connexion.commit()

   def addActivite(self, listeActivites):
      uneActivite = ("INSERT INTO activite VALUES (%s, %s, %s);")
      curseurActivite = BaseDonnees.connexion.cursor()
      for activite in listeActivites:
         dataActivite = (activite.nom, activite.numero, activite.numeroEquipement)
         curseurActivite.execute(uneActivite, dataActivite)
         BaseDonnees.connexion.commit()

