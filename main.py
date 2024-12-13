from Importation import *
from logger import * 
from filtre import *
from PIL import Image
from PIL import ImageFilter
import os
import sys

def main():
    """
    Point d'entrée principal pour le script CLI.

    Le script CLI permet d'appliquer les différents filtres sur des images à partir d'une ligne de commande.
    Les commandes disponibles sont:
        --log : Affiche les logs de l'application.
        --help : Affiche les aides d'utilisation.
        --filters : Applique des filtres choisit sur les images du dossier ou sont stocker les images.
    """
    if len(sys.argv) < 2:
        print("Usage : python3 main.py [--log | --help | --filters <filtre> --i <input_folder> --o <output_folder>] | --gif")
        sys.exit(1)

    command = sys.argv[1]

    if command == "--log":
        # Affiche les logs enregistrés.
        print("=== Logs ===")
        showlog()

    elif command == "--help":
        # Affiche un guide pour aider l'utilisateur.
        print("=== HELP ===")
        print("Usage exemple :")
        print("  --filters 'gray&rotate:55' --i <input_folder> --o <output_folder>")
        print("L'input_folder et l'output_folder doivent être écrits de la sorte: dossier/ avec les images dedans.")
        print("Options :")
        print("  grey             : Applique un filtre noir et blanc sur l'image prend pas de paramètre")
        print("  rotate:<deg>     : Applique une rotation de <deg> degrés")
        print("  dilate:<lvl>     : Applique un effet de dilatation <lvl>w")
        print("  blur:<lvl>       : Applique un effet de flou")
        print("  resize:<scaling> : Modifie la taille d'une image avec un scaling")
        print("  text:<X:Y:text>  : Permet d'écrire sur une image avec la position en (X , Y)")
        print("  --log            : Affiche les logs de l'application")
        print("  --gif            : Convertit toutes le images du dossier en gif et génere un gif avec toutes les images.")
        print("  --help           : Affiche ce message d'aide")

    elif command == "--filters":
        # Applique des filtres aux images dans un dossier source et sauvegarde le résultat.
        if len(sys.argv) < 6:
            print("Usage : python3 main.py --filters <filtre> --i <     input_folder> --o <output_folder>")
            sys.exit(1)

        filters = sys.argv[2]
        input_folder = sys.argv[4]
        output_folder = sys.argv[6]

        if not os.path.exists(input_folder):
            print(f"Erreur : le dossier source n'existe pas : {input_folder}")
            log(f"Erreur : le dossier source n'existe pas : {input_folder}")
            sys.exit(1)

        # Log des informations concernant l'opération
        log(f"Application des filtres : {filters}")
        log(f"Dossier source : {input_folder}")
        log(f"Dossier destination : {output_folder}")

        # appelle de la fonction pour filtrer et traiter les images
        processing(input_folder, output_folder, filters)
    elif command == "--gif" :
        input_folder = sys.argv[3]
        output_folder = sys.argv[5]
        gif_gestion(input_folder,output_folder, 500)

        
    else:
        # Si une commande tapper est inconnue
        print(f"Commande inconnue : {command}")
        print("Usage : python3 main.py [--log | --help | --filters]")

def processing(input_folder, output_folder, filter) :
    """
    Traite les images en appliquant une série de filtres.




    Args:
        input_folder (str): Chemin du dossier source contenant les images.
        output_folder (str): Chemin du dossier destination pour les images traitées.
        filter (str): Chaîne de filtres à appliquer, séparés par "&".
    """
    try :
        
         # Importer les images depuis le dossier source
        tableau_img = import_images_from_folder(input_folder)
        # Découper les filtres s'ils sont multiples
        tableau_filtre = filter.split("&")

        for filtre in tableau_filtre :
            if ":" in filtre :
                # Filtre avec paramètres 
                tableau_filtre_et_param = filtre.split(":")
                # Si le filtre est "text" (écriture sur image), passer les paramètres spécifiques
                if len(tableau_filtre_et_param) > 3 and tableau_filtre_et_param[0] == "text": 
                    tableau_img = apply_filter_images(tableau_img, tableau_filtre_et_param[0],[tableau_filtre_et_param[1],tableau_filtre_et_param[2],tableau_filtre_et_param[3]])
                else :
                    # Appliquer le filtre avec un paramètre entier
                    tableau_img = apply_filter_images(tableau_img,tableau_filtre_et_param[0],int(tableau_filtre_et_param[1]))
            else :
                # Filtre sans paramètre
                tableau_img = apply_filter_images(tableau_img, filtre, None)
        # Sauvegarder les images dans le dossier de destination
        for image in tableau_img :
            image[1].save(output_folder  + image[0])
    except AttributeError as e:
        print(f"Il y a eu un probleme lors du process d'image : {e}")
        log(f"Il y a eu un probleme lors du process d'image : {e}")
    except Exception as e :
        print(f"Il ya une erreur lors du process d'image : {e}, veuillez vérifiez le dossier ainsi que les filtre remplis et leurs valeurs")
        log(f"Il ya une erreur lors du process d'image : {e}, veuillez vérifiez le dossier ainsi que les filtre remplis et leurs valeurs")
if __name__ == "__main__":
    main()
