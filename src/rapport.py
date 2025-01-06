import pandas as pd
import os
import logging

# Configuration du système de journalisation
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("resultats/rapport.log"),
        logging.StreamHandler()
    ]
)

def generer_rapport(fichier_csv, fichier_sortie="resultats/rapport_recapitulatif.csv"):
    """
    Crée un rapport synthétique des stocks à partir d'un fichier consolidé.

    Args:
        fichier_csv (str): Chemin vers le fichier CSV consolidé.
        fichier_sortie (str): Chemin pour enregistrer le fichier de rapport généré.

    Returns:
        bool: Indique si le rapport a été généré avec succès ou non.
    """
    try:
        if not os.path.exists(fichier_csv):
            logging.error(f"Le fichier '{fichier_csv}' est introuvable.")
            return False

        # Lecture du fichier consolidé
        donnees = pd.read_csv(fichier_csv)

        # Création du rapport avec regroupement par catégorie
        rapport = donnees.groupby("Categorie").agg(
            Quantite_Totale=("Quantite", "sum"),
            Valeur_Totale=("Prix Unitaire", lambda prix: (prix * donnees.loc[prix.index, "Quantite"]).sum())
        ).reset_index()

        # Calcul des totaux globaux
        total_quantite = rapport["Quantite_Totale"].sum()
        total_valeur = rapport["Valeur_Totale"].sum()

        # Ajout d'une ligne TOTAL au rapport final
        ligne_total = pd.DataFrame(
            {"Categorie": ["TOTAL"], "Quantite_Totale": [total_quantite], "Valeur_Totale": [total_valeur]}
        )
        rapport_final = pd.concat([rapport, ligne_total], ignore_index=True)

        # Sauvegarde du rapport dans un fichier CSV
        os.makedirs(os.path.dirname(fichier_sortie), exist_ok=True)
        rapport_final.to_csv(fichier_sortie, index=False)
        logging.info(f"Rapport généré avec succès : {fichier_sortie}")
        return True

    except Exception as e:
        logging.error(f"Erreur inattendue lors de la création du rapport : {e}")
        return False
