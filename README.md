# Microlearning Maths Lycée : Arithmétique Interactive

Bienvenue dans **microlearning**, une application web interactive conçue pour révolutionner l'apprentissage de l'arithmétique au lycée grâce à la pédagogie du microlearning, le tout développé avec [Streamlit](https://streamlit.io/).

## Pourquoi le microlearning ?

Le **microlearning** est une méthode d'apprentissage moderne qui consiste à acquérir des connaissances par petites unités, de façon ciblée, interactive et régulière. Cette approche :
- Favorise la mémorisation à long terme grâce à des sessions courtes et répétées.
- Permet de se concentrer sur une notion à la fois, évitant la surcharge cognitive.
- S'adapte parfaitement aux rythmes d'apprentissage individuels.
- Encourage l'apprentissage actif par l'expérimentation et la pratique immédiate.

## À propos de l'application

`app.py` propose une expérience d'apprentissage unique et interactive, idéale pour :
- Les élèves souhaitant réviser efficacement les bases de l'arithmétique.
- Les enseignants cherchant un outil pédagogique dynamique pour illustrer les concepts en classe.
- Toute personne désirant renforcer ses compétences en mathématiques de façon ludique et autonome.

### Ce qui rend cette application parfaite pour le microlearning :
- **Contenus courts et ciblés** : Chaque propriété ou théorème est présenté de façon concise, avec formules et exemples concrets.
- **Interactivité immédiate** : Les utilisateurs peuvent manipuler des calculatrices et résoudre des équations en temps réel.
- **Feedback instantané** : Les résultats et solutions s'affichent immédiatement, favorisant l'auto-correction et la compréhension.
- **Navigation intuitive** : L'interface claire permet de passer rapidement d'une notion à l'autre selon ses besoins.

## Fonctionnalités principales

- **Résumé interactif des propriétés et théorèmes fondamentaux** :
  - Division euclidienne, PGCD, PPCM, nombres premiers, congruence, théorème de Gauss, etc.
  - Chaque notion est accompagnée d'exemples pour faciliter la compréhension.
- **Calculatrice arithmétique intelligente** :
  - Calcule le PGCD et le PPCM de deux entiers.
  - Vérifie si chaque nombre est premier.
  - Idéal pour tester rapidement des cas concrets.
- **Résolution d'équations diophantiennes linéaires** :
  - Saisissez les coefficients pour obtenir la solution particulière et la solution générale de l'équation `ax + by = c`.
  - Affichage détaillé des étapes et des formules utilisées.

## Prérequis

- Python 3.7 ou supérieur
- [pip](https://pip.pypa.io/en/stable/installation/)

## Installation

1. **Téléchargez et extrayez le fichier ZIP fourni** dans un dossier local de votre choix (par exemple `microlearning`).

2. **Ouvrez un terminal ou une invite de commandes dans ce dossier**.

3. **Installez les dépendances** :

```bash
pip install -r requirements.txt
```

> **Note :** Le seul paquet nécessaire est `streamlit`, déjà listé dans `requirements.txt`. Aucun autre module externe n'est requis pour exécuter `app.py`.

## Lancement de l'application

Dans le dossier du projet, lancez la commande suivante :

```bash
python -m streamlit run app.py
```

Cela ouvrira automatiquement l'application dans votre navigateur par défaut. Si ce n'est pas le cas, suivez le lien affiché dans le terminal.

## Structure du projet

- `app.py` : Code principal de l'application Streamlit.
- `requirements.txt` : Liste des dépendances Python nécessaires (ici, uniquement `streamlit`).

---

**Adoptez le microlearning pour progresser en arithmétique, à votre rythme et avec plaisir !** 
