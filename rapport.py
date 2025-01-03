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
        logging.FileHandler("../resultats/rapporteur.log"),
        logging.StreamHandler()
    ]
)

def creer_rapport(fichier_fusionne, chemin_export="../resultats/rapport_final.csv"):
    """
    Crée un rapport synthétique des inventaires.

    Args:
        fichier_fusionne (str): Chemin du fichier CSV fusionné.
        chemin_export (str): Chemin du fichier CSV de sortie.

    Returns:
        bool: True si le rapport a été créé avec succès, False sinon.
    """
    try:
        # Charger le fichier fusionné
        donnees = pd.read_csv(fichier_fusionne)

        # Calculer les statistiques
        inventaire_par_article = donnees.groupby("Article").agg(
            Quantite_Totale=("Quantite", "sum"),
            Valeur_Totale=("Prix Unitaire", lambda x: (x * donnees.loc[x.index, "Quantite"]).sum())
        )

        # Réinitialiser l'index pour inclure 'Article' comme colonne
        inventaire_par_article = inventaire_par_article.reset_index()

        # Calculer les totaux globaux
        quantite_totale = inventaire_par_article["Quantite_Totale"].sum()
        valeur_totale = inventaire_par_article["Valeur_Totale"].sum()

        # Ajouter une ligne TOTAL
        ligne_totale = pd.DataFrame(
            data={"Article": ["TOTAL"], "Quantite_Totale": [quantite_totale], "Valeur_Totale": [valeur_totale]}
        )
        rapport_final = pd.concat([inventaire_par_article, ligne_totale], ignore_index=True)

        # Enregistrer le rapport sans sauvegarder l'index
        os.makedirs(os.path.dirname(chemin_export), exist_ok=True)
        rapport_final.to_csv(chemin_export, index=False)
        logging.info(f"Rapport exporté avec succès : {chemin_export}")
        return True

    except Exception as e:
        logging.error(f"Erreur lors de l'export du rapport : {e}")
        return False
