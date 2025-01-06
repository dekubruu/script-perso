import pandas as pd
import os
import logging

# Création du dossier 'resultats' si absent
os.makedirs("resultats", exist_ok=True)

# Configuration des logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("resultats/consolidation.log"),
        logging.StreamHandler()
    ]
)

def consolider_fichiers_csv(fichiers_csv, fichier_sortie="resultats/fusionne.csv"):
    """
    Fusionne plusieurs fichiers CSV en un fichier unique.

    Args:
        fichiers_csv (list): Liste des chemins des fichiers CSV à fusionner.
        fichier_sortie (str): Chemin du fichier de sortie.

    Returns:
        bool: True si la fusion réussit, False sinon.
    """
    try:
        if not fichiers_csv:
            logging.error("Aucun fichier CSV fourni pour la fusion.")
            return False

        dataframes = []
        colonnes_reference = None

        # Lecture des fichiers CSV
        for chemin in fichiers_csv:
            if not os.path.exists(chemin):
                logging.error(f"Le fichier '{chemin}' est introuvable.")
                return False
            try:
                df = pd.read_csv(chemin)
                if colonnes_reference is None:
                    colonnes_reference = df.columns
                elif not df.columns.equals(colonnes_reference):
                    logging.error(f"Les colonnes du fichier '{chemin}' ne correspondent pas aux autres fichiers.")
                    return False
                dataframes.append(df)
                logging.info(f"Chargement réussi : {chemin}")
            except Exception as e:
                logging.error(f"Erreur lors de la lecture du fichier '{chemin}': {e}")
                return False

        # Fusion des DataFrames
        resultat_consolide = pd.concat(dataframes, ignore_index=True)
        resultat_consolide.to_csv(fichier_sortie, index=False)
        logging.info(f"Fichier consolidé créé avec succès : {fichier_sortie}")
        return True

    except Exception as e:
        logging.error(f"Erreur inattendue : {e}")
        return False
