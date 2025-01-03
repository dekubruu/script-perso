import pandas as pd
import os
import logging

# Créer le dossier 'resultats' s'il n'existe pas
os.makedirs("../resultats", exist_ok=True)
# Configurer les logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("../resultats/fusion.log"),
        logging.StreamHandler()
    ]
)

def fusionner_fichiers_csv(fichiers_csv, chemin_sortie="../resultats/fusionne.csv"):
    """
    Fusionne plusieurs fichiers CSV en un seul fichier.

    Args:
        fichiers_csv (list): Liste des chemins des fichiers CSV à fusionner.
        chemin_sortie (str): Chemin du fichier CSV de sortie.

    Returns:
        bool: True si la fusion a réussi, False sinon.
    """
    try:
        # Vérifier si la liste de fichiers est vide
        if not fichiers_csv:
            logging.error("Aucun fichier CSV fourni pour la fusion.")
            return False

        # Charger et valider chaque fichier
        tableaux = []
        for fichier in fichiers_csv:
            if not os.path.exists(fichier):
                logging.error(f"Le fichier '{fichier}' est introuvable.")
                return False
            try:
                tableau = pd.read_csv(fichier)
                tableaux.append(tableau)
                logging.info(f"Fichier chargé : {fichier}")
            except Exception as e:
                logging.error(f"Erreur lors de la lecture du fichier '{fichier}': {e}")
                return False

        # Vérifier que tous les fichiers ont les mêmes colonnes
        colonnes_reference = tableaux[0].columns
        for i, tableau in enumerate(tableaux):
            if not tableau.columns.equals(colonnes_reference):
                logging.error(f"Les colonnes du fichier {fichiers_csv[i]} ne correspondent pas.")
                return False

        # Fusionner les fichiers CSV
        donnees_fusionnees = pd.concat(tableaux, ignore_index=True)
        logging.info("Fusion des fichiers CSV effectuée avec succès.")

        # Sauvegarder le fichier fusionné
        os.makedirs(os.path.dirname(chemin_sortie), exist_ok=True)
        donnees_fusionnees.to_csv(chemin_sortie, index=False)
        logging.info(f"Fichier fusionné enregistré : {chemin_sortie}")
        return True

    except Exception as e:
        logging.error(f"Erreur inattendue : {e}")
        return False
