import pandas as pd
import logging
import os

# Configurer les logs
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
    Recherche des données dans un fichier CSV en fonction d'un champ et d'une valeur donnés.

    Args:
        fichier_csv (str): Chemin du fichier CSV consolidé.
        champ (str): Nom de la colonne sur laquelle appliquer la recherche.
        valeur (str, int, float): Valeur à rechercher.

    Returns:
        pd.DataFrame or None: Résultats de la recherche ou None si une erreur survient.
    """
    try:
        # Vérifier que le fichier existe
        if not os.path.exists(fichier_csv):
            logging.error(f"Le fichier '{fichier_csv}' est introuvable.")
            return None

        # Charger le fichier CSV
        donnees = pd.read_csv(fichier_csv)

        # Vérifier que la colonne existe
        if champ not in donnees.columns:
            logging.error(f"Le champ '{champ}' n'existe pas dans le fichier CSV.")
            return None

        # Appliquer la recherche
        if isinstance(valeur, (int, float)):
            resultats = donnees[donnees[champ] == valeur]  # Recherche exacte pour les types numériques
        else:
            resultats = donnees[donnees[champ].str.contains(str(valeur), case=False, na=False)]

        logging.info(f"Recherche réalisée avec succès : {len(resultats)} résultats trouvés.")
        return resultats

    except Exception as e:
        logging.error(f"Erreur inattendue lors de la recherche : {e}")
        return None
