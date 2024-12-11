from Importation import *
from logger import * 
from PIL import Image
from PIL import ImageFilter
import os
import sys

def main():
    """Point d'entrée principal pour le script CLI."""
    if len(sys.argv) < 2:
        print("Usage : python3 main.py [--log | --help | --filters <filtre> --i <input_folder> --o <output_folder>]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "--log":
        logs = read_logs()
        print("=== Logs ===")
        for log in logs:
            print(log.strip())

    elif command == "--help":
        print("=== HELP ===")
        print("Usage exemple :")
        print("  --filters \"gray&rotate:55\" --i <input_folder> --o <output_folder>")
        print("Options :")
        print("  gray        : Applique un filtre de niveau de gris")
        print("  rotate:<deg>: Applique une rotation de <deg> degrés")
        print("  --log       : Affiche les logs de l'application")
        print("  --help      : Affiche ce message d'aide")

    elif command == "--filters":
        if len(sys.argv) < 6:
            print("Usage : python3 main.py --filters <filtre> --i <input_folder> --o <output_folder>")
            sys.exit(1)

        filters = sys.argv[2]
        input_folder = sys.argv[4]
        output_folder = sys.argv[6]

        if not os.path.exists(input_folder):
            log(f"Erreur : le dossier source n'existe pas : {input_folder}")
            sys.exit(1)

        log(f"Application des filtres : {filters}")
        log(f"Dossier source : {input_folder}")
        log(f"Dossier destination : {output_folder}")

        process_images_in_folder(input_folder, output_folder, filters)

    else:
        print(f"Commande inconnue : {command}")
        print("Usage : python3 main.py [--log | --help | --filters]")

if __name__ == "__main__":
    main()
