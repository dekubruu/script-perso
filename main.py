import argparse
from fusion import fusionner_fichiers_csv
from exploration import effectuer_recherche
from rapporteur import creer_rapport

def programme_principal():
    # Initialisation de l'argumentation
    parser = argparse.ArgumentParser(description="Système d'administration d'inventaire")
    parser.add_argument(
        "operation",
        choices=["fusion", "exploration", "rapport"],
        help="Opération à exécuter : fusion, exploration ou rapport"
    )
    parser.add_argument(
        "--sources",
        nargs="+",
        help="Liste des fichiers CSV à fusionner (obligatoire pour 'fusion')"
    )
    parser.add_argument(
        "--champ",
        help="Nom de la colonne à utiliser pour l'exploration (obligatoire pour 'exploration')"
    )
    parser.add_argument(
        "--cible",
        help="Valeur à rechercher dans la colonne spécifiée (obligatoire pour 'exploration')"
    )
    parser.add_argument(
        "--export",
        help="Chemin du fichier d'export pour le rapport (optionnel pour 'rapport')",
        default="../outputs/rapport_final.csv"
    )

    args = parser.parse_args()

    # Gestion des opérations
    if args.operation == "fusion":
        if not args.sources:
            print("Erreur : Vous devez fournir une liste de fichiers avec --sources pour la fusion.")
            return

        succes = fusionner_fichiers_csv(args.sources)
        if succes:
            print("Fusion des fichiers terminée avec succès.")
        else:
            print("Échec de la fusion.")

    elif args.operation == "exploration":
        if not args.champ or not args.cible:
            print("Erreur : Vous devez fournir un champ (--champ) et une cible (--cible) pour l'exploration.")
            return

        fichier_fusionne = "../outputs/fusionne.csv"
        resultats = effectuer_recherche(fichier_fusionne, args.champ, args.cible)
        if resultats is not None and not resultats.empty:
            print("Résultats de l'exploration :")
            print(resultats)
        else:
            print("Aucun résultat trouvé ou une erreur est survenue.")

    elif args.operation == "rapport":
        fichier_fusionne = "../outputs/fusionne.csv"
        succes = creer_rapport(fichier_fusionne, args.export)
        if succes:
            print(f"Rapport exporté avec succès : {args.export}")
        else:
            print("Une erreur est survenue lors de l'export du rapport.")

if __name__ == "__main__":
    programme_principal()