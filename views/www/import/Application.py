from ListesDonnees import ListesDonnees
from BaseDonnees import BaseDonnees

# Location des fichiers
nomFichierInstallations = "../data/installations.csv"
nomFichierEquipements = "../data/equipements.csv"
nomFichierActivites = "../data/activites.csv"

# Création des fichiers
fichierInstallations = ListesDonnees.lireCSV(nomFichierInstallations)
fichierEquipements = ListesDonnees.lireCSV(nomFichierEquipements)
fichierActivites = ListesDonnees.lireCSV(nomFichierActivites)

# Création des listes
listeInstallations = ListesDonnees.creerInstallations(fichierInstallations)
listeEquipements = ListesDonnees.creerEquipements(fichierEquipements)
listeActivites = ListesDonnees.creerActivites(fichierActivites)

#Création de la base de données
baseDeDonnees = BaseDonnees()
baseDeDonnees.connexion()
baseDeDonnees.addInstallation(listeInstallations)
baseDeDonnees.addEquipement(listeEquipements)
baseDeDonnees.addActivite(listeActivites)
baseDeDonnees.deconnexion()

