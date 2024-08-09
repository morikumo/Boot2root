Apres ip a on recupere notre ip local car on est en resaux en acces par pont sur la vm par conséquant sur une plage d'ip de notre machine

on detecte notre ip : 192.168.108.190/25

nmap 192.168.108.190/25 > files.txt 

On lance la VM pour voir quel ip elle prend dans un 2eme file

nmap 192.168.108.190/25 > files2.txt 

On fait un diff :

> Host is up (0.00043s latency).
405a406,416
> Nmap scan report for 192.168.108.150
> Host is up (0.00016s latency).
> Not shown: 994 closed ports
> PORT    STATE SERVICE
> 21/tcp  open  ftp
> 22/tcp  open  ssh
> 80/tcp  open  http
> 143/tcp open  imap
> 443/tcp open  https
> 993/tcp open  imaps

C'est ce qui sortait de notre diff

Du coup l'ip 192.168.108.150

On fait un curl pour test :

curl https://192.168.108.150

On recupere bien du texte dedans :

Exemple :

<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
	<title>Hack me if you can</title>
	<meta name='description' content='Simple and clean HTML coming soon / under construction page'/>
	<meta name='keywords' content='coming soon, html, html5, css3, css, under construction'/>	
	<link rel="stylesheet" href="style.css" type="text/css" media="screen, projection" />
	<link href='http://fonts.googleapis.com/css?family=Coustard' rel='stylesheet' type='text/css'>

</head>
<body>
	<div id="wrapper">
		<h1>Hack me</h1>
		<h2>We're Coming Soon</h2>
		<p>We're wetting our shirts to launch the website.<br />
		In the mean time, you can connect with us trought</p>
		<p><a href="https://fr-fr.facebook.com/42Born2Code"><img src="fb.png" alt="Facebook" /></a> <a href="https://plus.google.com/+42Frborn2code"><img src="+.png" alt="Google +" /></a> <a href="https://twitter.com/42born2code"><img src="twitter.png" alt="Twitter" /></a></p>
	</div>
</body>
</html>

On voit du 42 un peu partout et hack me if you can. De sacré indice pour que l'on comprenne que l'on est au bonne endroit.

On va sur un navigateur pour tester ca, et il y a bien une page.

Etape 1 terminé.


Une fois arrivé au site il n'y a rien d'exploitable actuellement.

On va donc chercher un outil pour chercher les repertoire qu'il y a dans le site a partir de l'ip

On va utiliser dirb avec l'option -r pour empecher la recursivité:

```bash
➜  ~ dirb https://192.168.108.150/ -r

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Fri Aug  9 15:47:14 2024
URL_BASE: https://192.168.108.150/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt
OPTION: Not Recursive

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: https://192.168.108.150/ ----
+ https://192.168.108.150/cgi-bin/ (CODE:403|SIZE:292)                                            
==> DIRECTORY: https://192.168.108.150/forum/                                                     
==> DIRECTORY: https://192.168.108.150/phpmyadmin/                                                
+ https://192.168.108.150/server-status (CODE:403|SIZE:297)                                       
==> DIRECTORY: https://192.168.108.150/webmail/                                                   
                                                                                                  
-----------------
END_TIME: Fri Aug  9 15:47:15 2024
DOWNLOADED: 4612 - FOUND: 2
```

On a plusieurs site a vérifier.

/forum est une liste des messages

-forum-homepage

-forum-login-homepage

-forum-lmezard-passwd

-forum-login

Une fois connecté on va dans sur le profile lmazard, on trouve une adresse mail.

on va essayer de se connecter a webmail.

/webmail une boite mail

2 messages, un inutile un pour les mdp de la db phpmyadmin

/phpmyadmin pour ce connecter a la db

root/Fg-'kKXBj87E:aJ$

username : root
mdp: Fg-'kKXBj87E:aJ$

Une fois dessus on voit que l'on peut faire des requete sql ou voir ce qui est existant dessus on a deja dans la page mlf2_userdata sur la page de gauche on a les mail de tout le monde et les mdp hashé de tout le monde et d'autres info a considéré

