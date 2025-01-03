import pandas as pd
import logging
import os

# Créer le dossier 'resultats' s'il n'existe pas
os.makedirs("../resultats", exist_ok=True)
# Configurer les logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("../resultats/exploration.log"),
        logging.StreamHandler()
    ]
)

def effectuer_recherche(fichier_fusionne, champ, cible):
    """
    Effectue une recherche dans un fichier fusionné en fonction d'un champ donné.

    Args:
        fichier_fusionne (str): Chemin du fichier CSV fusionné.
        champ (str): Colonne sur laquelle appliquer la recherche (ex : 'Article', 'Prix Unitaire').
        cible (str, int, float): Valeur à rechercher.

    Returns:
        pd.DataFrame or None: Résultats de la recherche ou None si erreur.
    """
    try:
        # Charger le fichier fusionné
        donnees = pd.read_csv(fichier_fusionne)

        # Vérifier si le champ existe
        if champ not in donnees.columns:
            logging.error(f"Le champ '{champ}' n'existe pas dans le fichier.")
            return None

        # Appliquer le filtre
        if isinstance(cible, (int, float)):
            resultats = donnees[donnees[champ] == cible]  # Égalité stricte
        else:
            resultats = donnees[donnees[champ].str.contains(cible, case=False, na=False)]

        logging.info(f"Recherche réalisée avec succès : {len(resultats)} résultats trouvés.")
        return resultats

    except Exception as e:
        logging.error(f"Erreur lors de l'exploration : {e}")
        return None
