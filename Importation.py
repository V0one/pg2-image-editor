from PIL import Image
from logger import *

import os

def import_images_from_folder(input_folder):
    """
    Importe toutes les images d'un dossier donné.

    Args:
        folder_path (str): Chemin vers le dossier contenant les images.

    Returns:
        list: Liste des objets PIL.Image.Image représentant les images importées.
    """
    images = []
    # Parcourir tous les fichiers du dossier
    for file_name in os.listdir(input_folder):
        file_path = input_folder + file_name
        # Vérifier si c'est un fichier image
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            image = Image.open(file_path)
            if image is not None:
                images.append((file_name, image))
            else:
                print(f"Impossible de lire l'image : {file_name}")
                log(f"Impossible de lire l'image : {file_name}") 
    if len(images) == 0 :
        print(f"Le dossier rentré {input_folder} ne contient pas d'images")
        log(f"Le dossier rentré {input_folder} ne contient pas d'images")
    else :
        print(f"{len(images)} images ont été importées depuis '{folder_path}'.")
        log(f"{len(images)} images ont été importées depuis '{folder_path}'.")
    return images

def process_images_in_folder(input_folder, output_folder, filters):
    """Traite toutes les images dans un dossier et applique les filtres."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        if os.path.isfile(input_path):
            try:
                output_path = os.path.join(output_folder, filename)
                img = import_images_from_folder(folder_path)
                if img:
                    img.save(output_path)
                    log(f"Image traitée et sauvegardée : {output_path}")
                else:
                    log(f"Échec du traitement pour l'image : {input_path}")
            except Exception as e:
                log(f"Erreur inattendue avec le fichier {filename} : {e}")




folder_path = "img/default"  #Chemin vers le dossier contenant les images
#images = import_images_from_folder() 
#print(images)

#if images:
#    for image in images :
#        image[1].show()

