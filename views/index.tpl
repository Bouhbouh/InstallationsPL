<!doctype html>
<html lang='fr'>

<head>

		<meta charset="utf-8">
		<link rel="shortcut icon" href="/static/img/favicon.ico">
		<!-- Custom CSS-->
        <link href="/static/css/styles.css" rel="stylesheet">
        <link href="/static/css/font-awesome.css" rel="stylesheet">
		
		<title>Activités Sportives des Pays de la Loire | Baptiste GAUTHIER & Simon BESSENAY</title>

		
</head>

<body>
	
		<!-- navbar -->
		<header>
		
			<div class="navbar">
			
				<!-- logo -->
				<a href="index.html"><b class="logo"></b></a>
				
			</div>
			
		</header>
	
	
		<!-- contents -->
		<div class="contents">
		{{ !body }}
		
         <h1>Activités sportives des Pays de la Loire</h1>

         <form id="search-activity" action="/activites" method="post">
         
         <input type="text" class="inputs" name="lieu" placeholder="Recherchez une ville..." required /><br/>
         <input type="text" class="inputs" name="nomActivite" placeholder="Recherchez une activite..." required /> 
         
         
		
		   <div class="bouton">
            <button type="submit" class="btn btn-primary btn-lg outline"><i class="fa fa-search fa-lg"></i>Rechercher une activité</button>
		   </div>
		   
         </form>
         
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

