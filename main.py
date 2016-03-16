from LectureCSV import LectureCSV
from Installation import Installation
from Equipement import Equipement
from Activite import Activite
from BD import BD
from libs.bottle import route, template, run, static_file, get, post, request, view
import views
from BD import BD

bd = BD()

@route('/static/<filepath:path>')
def file_stac(filepath):
	return static_file(filepath,root="./static")

@route('/')
@route('/index')
@view('views/index.tpl')
def index():
	res = ""
	return {"body" : res}

@post('/activites')
@view('views/recherche.tpl')
def search_activity():
	nomActivite = request.forms.get('nomActivite')
	lieu = request.forms.get('lieu')
	resultat_recherche = bd.recherche(nomActivite, lieu)
	liste = ""
	if len(resultat_recherche) == 0:
		liste = "<div class='contents'><h2><i class='fa fa-exclamation-triangle'></i>Aucune activité sportive ne correspond à votre recherche...</h2><p>Vous pouvez toujours faire une nouvelle recherche pour trouver l'activité sportive de vos rêves !</p></div>"
	else:
		liste = ""
		for i in resultat_recherche:
			numRue = i[6]
			if numRue == 0:
				numRue = ""
			liste += "<div class='activite'><div id='header'><b>" + str(i[5]) + "</b></div><div id='section'><table><tr><td><i class='fa fa-briefcase'></i></td><td>" + str(i[3]) + "</td></tr><tr><td><i class='fa fa-suitcase'></i></td><td>" + str(i[1]) + "</td></tr><tr><td><i class='fa fa-map-marker'></i></td><td>" + str(numRue) + " rue " + str(i[7]) + " " + str(i[8]) + ", " + str(i[9]) + "</td></tr></table><a href=/activite/" + str(i[0]) + " target='_blank'>Plus d'informations...</a></div></div>"
	return {"liste" : liste}

@route('/activite/<identifiant:int>')
@view('views/activite.tpl')
def activite(identifiant):
	activite = bd.get_installation(identifiant)
	res = "<p>" + str(activite[0]) + "</p>"
	location = str(activite[0][9]).replace("[", "").replace("]", "").split(",")
	latitude = location[0]
	longitude = location[1]
	return {"res" : res, "latitude" : latitude, "longitude" : longitude}


run(host='localhost', port=8080)
