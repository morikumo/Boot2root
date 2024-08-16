
---

# README: Projet Turtle Graphics

## Introduction
Ce projet utilise un fichier nommé `turtle` qui, après inspection avec la commande `file`, s'avère être un fichier texte ASCII. Ce fichier contient une série d'instructions qui semblent dessiner quelque chose en utilisant une méthode de programmation graphique simpliste connue sous le nom de Turtle Graphics.

## Contenu du Fichier Turtle
Le fichier `turtle` contient des instructions répétitives qui impliquent des rotations et des avancées. Voici un extrait des commandes :
```plaintext
Tourne gauche de 1 degrees
Avance 1 spaces
Tourne gauche de 1 degrees
Avance 1 spaces
...
```

## Interprétation et Execution
Le nom `turtle` et le style des commandes sont des indices qui suggèrent l'utilisation de Turtle Graphics, un outil pédagogique pour apprendre la programmation en dessinant avec des commandes simples. Les commandes pertinentes pour ce projet, selon la syntaxe de Turtle Graphics en Python, incluent `right`, `left`, `forward`, et `backward`.

### Traduction des Commandes
Les commandes du fichier doivent être traduites dans un format utilisable par un interpréteur Turtle Graphics. Par exemple, les commandes peuvent être converties en Python comme suit :
```python
import turtle

t = turtle.Turtle()

t.left(1)
t.forward(1)
t.left(1)
t.forward(1)
...

turtle.done()
```

### Visualisation
Après traduction, les commandes peuvent être exécutées sur une plateforme telle que https://pythonsandbox.com/turtle pour visualiser le résultat. La série de commandes forme progressivement les lettres du mot "SLASH".

## Décodage du Message
La deuxième partie du challenge, "Can you digest the message? :)", suggère une opération de hachage. La recherche du terme "digest" associée au hachage mène à MD5, une méthode de hachage couramment utilisée.

### Hachage MD5
Le mot "SLASH" est ensuite converti en un hachage MD5 :
```plaintext
MD5 de "SLASH" : 646da671ca01bb5d84dbb5fb2238dc8e
```

## Connexion au Compte Utilisateur
Le hachage MD5 est utilisé comme mot de passe pour se connecter à l'utilisateur `zaz` :
```plaintext
su zaz
Mot de passe : 646da671ca01bb5d84dbb5fb2238dc8e
```

---
