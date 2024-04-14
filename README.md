# Projet : Prédiction de la capacité de remboursement des prêts pour l’United States Small Business Administration, US SBA


## Contexte

L'US SBA a été fondée en 1953 dans le but d'aider les petites entreprises à obtenir du crédit. Les petites entreprises ont été la principale source de création d'emplois aux États-Unis, favorisant ainsi la création d'opportunités d'emploi et la réduction du chômage.

L'enjeu de ce projet est de prédire si les entreprises seront capables de rembourser leur prêt. Il s'agit donc d'une tâche de classification binaire, où le prêt peut être accordé ou non.

## Objectifs du Projet

### Partie 1 : Nettoyage, EDA et Modélisation

Cette phase fondamentale est décomposée en plusieurs étapes, à savoir:

- Nettoyage du jeu de données.
- Analyse du jeu de données en utilisant des techniques d'analyse univariée, bivariée, et des tests statistiques.
- Préparation des données pour le modèle en effectuant des pré-traitements, la sélection des features, le feature engineering, etc.
- Entraînement du modèle de prédiction avec les algorithmes choisis.

### Partie 2 : Mise en Production : Création de l'Application et de l'API

Il s'agit ici de: 

- Utiliser FastAPI pour rendre accessible le modèle via une API.
- Développer une interface graphique avec Django pour consommer l'API.
- Créer une application web composée de l'API pour servir le modèle et d'une application web (Django) pour consommer l'API.

---
*Ce projet est réalisé dans le cadre de la formation en data science chez Simplon.*
