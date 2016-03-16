sys.path.insert(0, '../class')

from Installation import Installation
from Equipement import Equipement
from Activite import Activite

import csv

class ListesDonnees:

   def lireCSV(nomFichier):
       fichier = csv.reader(open(nomFichier,"r"))
       return fichier

   def creerInstallations(fichier):
       listeInstallations = []
       header = True
       for row in fichier:
           if header:
               header = False
               continue
           uneInstallation = Installation(row[0], row[1], row[2], row[4], row[5], row[6], row[7], row[9], row[10])
           if ((uneInstallation not in listeInstallations) and (row[1] is not "")):
               listeInstallations.append(uneInstallation)
       return listeInstallations

   def creerEquipements(fichier):
       listeEquipements = []
       header = True
       for row in fichier:
           if header:
               header = False
               continue
           unEquipement = Equipement(row[5], row[4], row[7], row[2])
           if ((unEquipement not in listeEquipements) and (row[4] is not "")):
               listeEquipements.append(unEquipement)
       return listeEquipements

   def creerActivites(fichier):
       listeActivites = []
       header = True
       for row in fichier:
           if header:
               header = False
               continue
           uneActivite = Activite(row[5], row[4], row[2])
           if ((uneActivite not in listeActivites) and (row[4] is not "")):
               listeActivites.append(uneActivite)
       return listeActivites

