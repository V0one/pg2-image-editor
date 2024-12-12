from Importation import *
from logger import * 
from filtre import *
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
        for log1 in logs:
            print(log1.strip())

    elif command == "--help":
        print("=== HELP ===")
        print("Usage exemple :")
        print("  --filters \"gray&rotate:55\" --i <input_folder> --o <output_folder>")
        print("Options :")
        print("  gray        : Applique un filtre noir et blanc sur l'image")
        print("  rotate: <deg>: Applique une rotation de <deg> degrés")
        print("  dilate : <lvl> : Applique un effet de dilatation")
        print("  blur <lvl>: Applique un effet de flou")
        print("  resize  <scaling> : Modifie la taille d'une image avec un scaling")
        print("  write <position -> X:Y:text> : Permet d'écrire sur une image avec la position")
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
            print(f"Erreur : le dossier source n'existe pas : {input_folder}")
            log(f"Erreur : le dossier source n'existe pas : {input_folder}")
            sys.exit(1)

        log(f"Application des filtres : {filters}")
        log(f"Dossier source : {input_folder}")
        log(f"Dossier destination : {output_folder}")

        processing(input_folder, output_folder, filters)

    else:
        print(f"Commande inconnue : {command}")
        print("Usage : python3 main.py [--log | --help | --filters]")


input_folder = "img/default/"
output_folder = "img/modified/"

liste_image = import_images_from_folder(input_folder)


def processing(input_folder, output_folder, filter) :
    tableau_img = import_images_from_folder(input_folder)
    tableau_filtre = filter.split("&")
    for filtre in tableau_filtre :
        if ":" in filtre :
            tableau_filtre_et_param = filtre.split(":")
            if len(tableau_filtre_et_param) > 3 and tableau_filtre_et_param[0] == "text": 
                tableau_img = apply_filter_images(tableau_img, tableau_filtre_et_param[0],[tableau_filtre_et_param[1],tableau_filtre_et_param[2],tableau_filtre_et_param[3]])
            else :
                tableau_img = apply_filter_images(tableau_img,tableau_filtre_et_param[0],int(tableau_filtre_et_param[1]))
        else :
            tableau_img = apply_filter_images(tableau_img, filtre, None)
    for image in tableau_img :
        image[1].save(output_folder + "/" + image[0])
        


if __name__ == "__main__":
    main()


