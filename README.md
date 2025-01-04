# Gestion d'Inventaire - Automatisation

## **Présentation**
Ce projet est une solution automatisée de gestion d'inventaire pour une entreprise locale. Il permet de :
- **Consolider** plusieurs fichiers CSV contenant les stocks.
- **Rechercher rapidement** des informations dans les stocks (par produit, catégorie, prix, etc.).
- **Générer un rapport récapitulatif** des stocks avec des totaux globaux.

Le programme fonctionne uniquement en **ligne de commande** et génère des logs pour suivre les différentes opérations.

---

## **Installation**
### **Prérequis**
- Python 3.x installé sur votre machine
- Bibliothèque Python : `pandas`

### **Étapes d'installation**
1. **Cloner le dépôt Git** :
   ```bash
   git clone <url_du_depot_git>
   cd gestion-inventaire
   ```

2. **Installer les dépendances** :
   ```bash
   pip install pandas
   ```

3. **Créer les dossiers nécessaires** :
   Si les dossiers `src/resultats` et `src/data` n'existent pas, créez-les manuellement :
   ```bash
   mkdir -p src/resultats src/data
   ```

---

## **Utilisation**
Le programme s'exécute via le fichier `main.py` et propose trois opérations principales :

### **1. Fusion des fichiers CSV**
Cette opération consolide plusieurs fichiers CSV en un seul.

**Commande :**
```bash
python main.py fusion --sources ../data/categorie1.csv ../data/categorie2.csv
```

**Exemple :**
```bash
python main.py fusion --sources ../data/categorie1.csv ../data/categorie2.csv
```
Le fichier fusionné sera enregistré dans `src/resultats/fusionne.csv`.

### **2. Recherche dans les stocks**
Cette opération permet de rechercher des informations dans le fichier consolidé selon un champ et une valeur donnés.

**Commande :**
```bash
python main.py recherche --champ <nom_colonne> --valeur <valeur>
```

**Exemple :**
```bash
python main.py recherche --champ Produit --valeur Pomme
```

### **3. Génération d’un rapport récapitulatif**
Cette opération génère un rapport récapitulatif des stocks par catégorie avec des totaux globaux.

**Commande :**
```bash
python main.py rapport --export resultats/rapport_personnalise.csv
```

**Exemple :**
```bash
python main.py rapport --export resultats/rapport_personnalise.csv
```
Le fichier de rapport sera créé dans le chemin spécifié.

---

## **Fonctionnalités détaillées**
- **Fusion des fichiers CSV** : 
  - Vérifie que les fichiers existent et ont des colonnes cohérentes.
  - Produit un fichier unique contenant toutes les lignes des fichiers source.

- **Recherche rapide** :
  - Permet de rechercher des informations selon un champ spécifique.
  - Supporte la recherche exacte pour les types numériques et partielle (insensible à la casse) pour les chaînes de caractères.

- **Génération de rapport** :
  - Calcule la quantité totale et la valeur totale par catégorie.
  - Ajoute une ligne de total global au rapport.

---

## **Notes**
- Les logs des opérations sont générés dans le dossier `src/resultats` sous forme de fichiers `.log`.
- En cas d'erreur (fichier introuvable, colonne inexistante), le programme affiche un message clair et enregistre les détails dans les logs.

---

## **Auteur**
Ce projet a été réalisé dans le cadre d’un exercice pratique visant à développer une solution automatisée de gestion d’inventaire.

---

