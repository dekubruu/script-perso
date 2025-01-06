import pandas as pd
import logging
import os

# Configuration du journal de logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("resultats/recherche.log"),
        logging.StreamHandler()
    ]
)

def rechercher_donnees(fichier_csv, champ, valeur):
    """
    Effectue une recherche dans un fichier CSV consolidé selon un champ et une valeur donnés.

    Args:
        fichier_csv (str): Chemin vers le fichier CSV consolidé.
        champ (str): Nom de la colonne à utiliser pour la recherche.
        valeur (str, int, float): Valeur à rechercher.

    Returns:
        pd.DataFrame or None: DataFrame contenant les résultats ou None en cas d'erreur.
    """
    try:
        if not os.path.exists(fichier_csv):
            logging.error(f"Le fichier '{fichier_csv}' est introuvable.")
            return None

        # Lecture du fichier CSV
        donnees = pd.read_csv(fichier_csv)

        # Validation de l'existence de la colonne
        if champ not in donnees.columns:
            logging.error(f"Le champ '{champ}' n'existe pas dans le fichier CSV.")
            return None

        # Application de la recherche selon le type de valeur
        if isinstance(valeur, (int, float)):
            resultats = donnees[donnees[champ] == valeur]
        else:
            resultats = donnees[donnees[champ].str.contains(str(valeur), case=False, na=False)]

        logging.info(f"Recherche complétée avec succès : {len(resultats)} résultats trouvés.")
        return resultats

    except Exception as e:
        logging.error(f"Erreur inattendue lors de la recherche : {e}")
        return None
