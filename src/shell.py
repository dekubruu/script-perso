import os


def main():
    print("Bienvenue dans le shell interactif de gestion d'inventaire.")
    print("Commandes disponibles :")
    print("  fusion      - Fusionner plusieurs fichiers CSV")
    print("  recherche   - Rechercher un produit dans les fichiers consolidés")
    print("  rapport     - Générer un rapport d'inventaire")
    print("Tapez 'help' pour la liste des commandes, ou 'exit' pour quitter.\n")

    while True:
        command = input("inventaire> ").strip()

        if command in ("exit", "quit"):
            print("Fermeture du shell.")
            break
        elif command == "help":
            afficher_aide()
        elif command.startswith("fusion"):
            executer_fusion()
        elif command.startswith("recherche"):
            executer_recherche()
        elif command.startswith("rapport"):
            executer_rapport()
        else:
            print(f"Commande inconnue : {command}. Tapez 'help' pour la liste des commandes.")


def afficher_aide():
    print("Commandes disponibles :")
    print("  fusion      - Fusionner plusieurs fichiers CSV")
    print("  recherche   - Rechercher un produit dans les fichiers consolidés")
    print("  rapport     - Générer un rapport d'inventaire")
    print("  help        - Afficher cette aide")
    print("  exit, quit  - Quitter le shell")


def executer_fusion():
    sources = input("Entrez les chemins des fichiers sources séparés par un espace : ").strip()
    if not sources:
        print("Erreur : Vous devez spécifier au moins un fichier source.")
        return

    command = f"python main.py fusion --sources {sources}"
    os.system(command)


def executer_recherche():
    champ = input("Entrez le champ de recherche (ex: Produit, Catégorie, etc.) : ").strip()
    valeur = input("Entrez la valeur à rechercher : ").strip()

    if not champ or not valeur:
        print("Erreur : Vous devez spécifier à la fois un champ et une valeur.")
        return

    command = f"python main.py recherche --champ {champ} --valeur {valeur}"
    os.system(command)


def executer_rapport():
    chemin_export = input("Entrez le chemin d'export du rapport : ").strip()
    if not chemin_export:
        print("Erreur : Vous devez spécifier un chemin d'export.")
        return

    command = f"python main.py rapport --export {chemin_export}"
    os.system(command)


if __name__ == "__main__":
    main()
