# Système de Gestion d'Inventaire - Script Python

## **Présentation**
Ce projet est un script Python permettant de :
- Consolider plusieurs fichiers CSV contenant des stocks en un fichier unique.
- Rechercher des informations dans un fichier CSV consolidé selon un champ et une valeur donnés.
- Générer un rapport récapitulatif des stocks par catégorie.

Le script fonctionne via une interface en ligne de commande et gère les erreurs grâce à un système de logs.

---

## **Installation**

### **Prérequis**
- Python 3.x installé sur votre machine.
- Bibliothèque Python : `pandas`

### **Étapes d'installation**
1. **Cloner le dépôt Git** :
   ```bash
   git clone <url_du_depot_git>
   cd script-perso/src
   ```
2. **Installer les dépendances** :
   ```bash
   pip install pandas
   ```
3. **Vérifier la présence des dossiers** :
   Assurez-vous que les dossiers suivants existent :
   - `data` : contient les fichiers CSV à fusionner.
   - `resultats` : contiendra les fichiers consolidés et les rapports.

---

## **Utilisation**

Le script propose trois opérations principales :

### **1. Fusion des fichiers CSV**
Cette opération permet de consolider plusieurs fichiers CSV en un seul fichier.

**Commande** :
```bash
python main.py fusion --sources ../data/categorie1.csv ../data/categorie2.csv
```
- Le fichier fusionné sera enregistré dans `resultats/fusionne.csv`.

---

### **2. Recherche dans le fichier consolidé**
Cette opération permet d'effectuer une recherche selon un champ et une valeur spécifiés.

**Commande** :
```bash
python main.py recherche --champ Produit --valeur Pomme
```

### **3. Génération d'un rapport récapitulatif**
Cette opération permet de créer un rapport récapitulatif des stocks par catégorie avec les totaux globaux.

**Commande** :
```bash
python main.py rapport --export resultats/rapport_personnalise.csv
```
- Le rapport sera enregistré dans le fichier `resultats/rapport_personnalise.csv`.

---
