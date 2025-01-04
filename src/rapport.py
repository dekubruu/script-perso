import pandas as pd
import os
import logging

# Configurer les logs
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
    Génère un rapport récapitulatif des stocks à partir d'un fichier CSV consolidé.

    Args:
        fichier_csv (str): Chemin du fichier CSV consolidé.
        fichier_sortie (str): Chemin du fichier CSV où enregistrer le rapport.

    Returns:
        bool: True si le rapport a été généré avec succès, False sinon.
    """
    try:
        # Vérifier que le fichier existe
        if not os.path.exists(fichier_csv):
            logging.error(f"Le fichier '{fichier_csv}' est introuvable.")
            return False

        # Charger les données
        donnees = pd.read_csv(fichier_csv)

        # Calculer les statistiques
        rapport = donnees.groupby("Categorie").agg(
            Quantite_Totale=("Quantite", "sum"),
            Valeur_Totale=("Prix Unitaire", lambda x: (x * donnees.loc[x.index, "Quantite"]).sum())
        ).reset_index()

        # Calculer les totaux globaux
        quantite_totale = rapport["Quantite_Totale"].sum()
        valeur_totale = rapport["Valeur_Totale"].sum()

        # Ajouter une ligne TOTAL
        ligne_totale = pd.DataFrame(
            data={"Categorie": ["TOTAL"], "Quantite_Totale": [quantite_totale], "Valeur_Totale": [valeur_totale]}
        )
        rapport_final = pd.concat([rapport, ligne_totale], ignore_index=True)

        # Enregistrer le rapport
        os.makedirs(os.path.dirname(fichier_sortie), exist_ok=True)
        rapport_final.to_csv(fichier_sortie, index=False)
        logging.info(f"Rapport généré avec succès : {fichier_sortie}")
        return True

    except Exception as e:
        logging.error(f"Erreur inattendue lors de la génération du rapport : {e}")
        return False
