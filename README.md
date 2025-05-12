# Projet Python – Générateur de mots de passe sécurisé

Projet personnel réalisé en Python, visant à créer un **générateur de mots de passe automatique et personnalisable**, avec une évaluation de la robustesse et une copie automatique dans le presse-papiers.

## Présentation

Ce projet consiste à développer un programme en Python permettant de générer des mots de passe sécurisés selon les préférences de l'utilisateur : utilisation ou non de majuscules, minuscules, chiffres et symboles. Le mot de passe est ensuite évalué et copié automatiquement dans le presse-papiers grâce à la bibliothèque `pyperclip`.

Le générateur garantit l'inclusion d'au moins un caractère de chaque type sélectionné, tout en assurant une longueur minimale de 8 caractères.

## Auteur du projet

- Julien CHAN PENG

## Contenu du projet

- `mdp_generator.py` – Script principal du générateur de mot de passe

## Fonctionnalités implémentées

- Sélection interactive des types de caractères à inclure (majuscules, minuscules, chiffres, symboles)
- Vérification de la longueur minimale et gestion des erreurs d'entrée utilisateur
- Génération aléatoire avec inclusion obligatoire de chaque type sélectionné
- Mélange aléatoire des caractères pour éviter des motifs prévisibles
- Évaluation de la **force du mot de passe** selon plusieurs critères (longueur, diversité)
- Copie automatique du mot de passe dans le **presse-papiers** via `pyperclip`

## Concepts utilisés

- Manipulation de chaînes de caractères (`string.ascii_*`, `string.punctuation`)
- Gestion des entrées utilisateurs (`input`, `try/except`)
- Sélection aléatoire sécurisée (`random.choice`, `random.shuffle`)
- Contrôle des conditions de sécurité (minimum de complexité)
- Utilisation de bibliothèques externes (`pyperclip`)

## Résultats obtenus

- Génération de mots de passe robustes en quelques secondes
- Interface en ligne de commande simple et intuitive
- Mots de passe **adaptés aux besoins spécifiques de l'utilisateur**
- **Renforcement de la sécurité** en obligeant des types de caractères diversifiés

## Limites et pistes d’amélioration

- Interface graphique non disponible (projet en mode console uniquement)
- Pas d’option d’enregistrement automatique des mots de passe générés
- Évaluation de sécurité encore perfectible (score basé sur un système simple)

## Enseignements

Ce projet m’a permis de :
- Approfondir l’usage des bibliothèques Python pour la **manipulation de chaînes et de caractères aléatoires**
- M'exercer à la **gestion des erreurs utilisateur** en ligne de commande
- Implémenter une **logique de sécurité informatique de base**
- Utiliser des bibliothèques externes comme `pyperclip` pour améliorer l’expérience utilisateur


