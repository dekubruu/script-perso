import pandas as pd
import os
import logging

# Créer le dossier 'resultats' s'il n'existe pas
os.makedirs("resultats", exist_ok=True)

# Configurer les logs
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
    Consolide plusieurs fichiers CSV en un seul fichier.

    Args:
        fichiers_csv (list): Liste des chemins des fichiers CSV à consolider.
        fichier_sortie (str): Chemin du fichier CSV de sortie.

    Returns:
        bool: True si la consolidation a réussi, False sinon.
    """
    try:
        # Vérifier si la liste de fichiers est vide
        if not fichiers_csv:
            logging.error("Aucun fichier CSV fourni pour la consolidation.")
            return False

        # Charger les fichiers et vérifier les colonnes
        dataframes = []
        colonnes_reference = None
        for fichier in fichiers_csv:
            if not os.path.exists(fichier):
                logging.error(f"Le fichier '{fichier}' est introuvable.")
                return False
            try:
                df = pd.read_csv(fichier)
                if colonnes_reference is None:
                    colonnes_reference = df.columns
                elif not df.columns.equals(colonnes_reference):
                    logging.error(f"Les colonnes du fichier '{fichier}' ne correspondent pas aux autres fichiers.")
                    return False
                dataframes.append(df)
                logging.info(f"Fichier chargé avec succès : {fichier}")
            except Exception as e:
                logging.error(f"Erreur lors de la lecture du fichier '{fichier}': {e}")
                return False

        # Fusionner les fichiers
        df_consolide = pd.concat(dataframes, ignore_index=True)
        df_consolide.to_csv(fichier_sortie, index=False)
        logging.info(f"Fichier consolidé enregistré avec succès : {fichier_sortie}")
        return True

    except Exception as e:
        logging.error(f"Erreur inattendue lors de la consolidation : {e}")
        return False
