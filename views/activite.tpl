<!doctype html>
<html lang='fr'>

<head>

		<meta charset="utf-8">
		<link rel="shortcut icon" href="/static/img/favicon.ico">
		<!-- Custom CSS -->
        <link href="/static/css/styles.css" rel="stylesheet">
        <link href="/static/css/font-awesome.css" rel="stylesheet">
       	<!-- Map Leaflet -->
       	<link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet-0.7.3/leaflet.css" />
       	<script src="http://cdn.leafletjs.com/leaflet-0.7.3/leaflet.js"></script>
		
		<title>Activités Sportives des Pays de la Loire | Baptiste GAUTHIER & Simon BESSENAY</title>
		
</head>

			<script>
	    		function InitialiserCarte(latitude, longitude) {
	
				    var map = L.map('map').setView([latitude, longitude], 16);

				    // create the tile layer with correct attribution
				    var tuileUrl = 'http://{s}.tile.osm.org/{z}/{x}/{y}.png';
				    
				    var attrib = 'Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors';
				    
				    var marker = L.marker([latitude, longitude]).addTo(map);

				    var osm = L.tileLayer(tuileUrl, {
				        attribution: attrib
				    });

				    osm.addTo(map);

				}

	    	</script>

<body onload="InitialiserCarte({{ !latitude }}, {{ !longitude }});">
	
		<!-- navbar -->
		<header>
		
			<div class="navbar">
			
				<!-- logo -->
				<a href="/index"><b class="logo"></b></a>
				
				<!-- links -->
				<ul>
				<li><a href="/index"><i class="fa fa-search fa-lg"></i><b>Rechercher une autre activité</b></a></li>
				
			</div>
			
		</header>
	
	
		<!-- contents -->
		<div class="contents">
      		{{ !res }}
	    </div>

	    <div id="map" style="height: 500px">
	    	
	    </div>
	
		<!-- footer -->
		<footer>
		
				<div class="footer-texte">
				
					<!-- Left Footer -->
					<div class="footer-left">
						&copy; 2016 - <b>Baptiste GAUTHIER & Simon BESSENAY</b>
					</div>

					<!-- Right Footer -->
					<div class="footer-right">
						Université de Nantes - IUT de Nantes - Département Informatique
					</div>
					
				</div>
			
		</footer>
	
</body>
</html>

