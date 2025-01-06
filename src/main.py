import argparse
from consolidation import consolider_fichiers_csv
from recherche import rechercher_donnees
from rapport import generer_rapport


def main():
    """
    Point d’entrée principal du programme de gestion d'inventaire.
    Gère les options de ligne de commande pour les opérations de fusion, recherche et rapport.
    """
    # Initialisation de l'analyseur d'arguments
    parser = argparse.ArgumentParser(description="Système de gestion d'inventaire")
    parser.add_argument(
        "operation",
        choices=["fusion", "recherche", "rapport"],
        help="Opération à exécuter : fusion, recherche ou rapport"
    )
    parser.add_argument(
        "--sources",
        nargs="+",
        help="Liste des fichiers CSV à fusionner (obligatoire pour 'fusion')"
    )
    parser.add_argument(
        "--champ",
        help="Nom de la colonne à utiliser pour la recherche (obligatoire pour 'recherche')"
    )
    parser.add_argument(
        "--valeur",
        help="Valeur à rechercher dans la colonne spécifiée (obligatoire pour 'recherche')"
    )
    parser.add_argument(
        "--export",
        help="Chemin du fichier d'export pour le rapport (optionnel pour 'rapport')",
        default="resultats/rapport_recapitulatif.csv"
    )

    # Analyse des arguments
    args = parser.parse_args()

    # Exécution de l'opération spécifiée
    if args.operation == "fusion":
        if not args.sources:
            print("Erreur : Vous devez fournir une liste de fichiers avec --sources pour la fusion.")
            return

        if consolider_fichiers_csv(args.sources):
            print("Fusion des fichiers terminée avec succès.")
        else:
            print("Échec de la fusion.")

    elif args.operation == "recherche":
        if not args.champ or not args.valeur:
            print("Erreur : Vous devez fournir un champ (--champ) et une valeur (--valeur) pour la recherche.")
            return

        fichier_consolide = "resultats/fusionne.csv"
        resultats = rechercher_donnees(fichier_consolide, args.champ, args.valeur)
        if resultats is not None and not resultats.empty:
            print("Résultats de la recherche :")
            print(resultats)
        else:
            print("Aucun résultat trouvé ou une erreur est survenue.")

    elif args.operation == "rapport":
        fichier_consolide = "resultats/fusionne.csv"
        if generer_rapport(fichier_consolide, args.export):
            print(f"Rapport exporté avec succès : {args.export}")
        else:
            print("Une erreur est survenue lors de l'export du rapport.")


if __name__ == "__main__":
    main()
