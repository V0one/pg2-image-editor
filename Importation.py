from PIL import Image
from logger import *
import os

def import_images_from_folder():
    """
    Importe toutes les images d'un dossier donné.

    Args:
        folder_path (str): Chemin vers le dossier contenant les images.

    Returns:
        list: Liste des objets PIL.Image.Image représentant les images importées.
    """
    images = []
    # Parcourir tous les fichiers du dossier
    for file_name in os.listdir("img/default"):
        file_path = "img/default/" + file_name
        # Vérifier si c'est un fichier image
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            image = Image.open(file_path)
            if image is not None:
                images.append((file_name, image))
            else:
                print(f"Impossible de lire l'image : {file_name}")
                log(f"Impossible de lire l'image : {file_name}")
    
    print(f"{len(images)} images ont été importées depuis '{folder_path}'.")
    log(f"{len(images)} images ont été importées depuis '{folder_path}'.")
    return images

folder_path = "img/default"  #Chemin vers le dossier contenant les images
#images = import_images_from_folder() 
#print(images)

#if images:
#    for image in images :
#        image[1].show()

