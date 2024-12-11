from PIL import Image
from logger import *
import os

def import_images_from_folder(folder_path):
    """
    Importe toutes les images d'un dossier donné.

    Args:
        folder_path (str): Chemin vers le dossier contenant les images.

    Returns:
        list: Liste des objets PIL.Image.Image représentant les images importées.
    """
    if not os.path.exists(folder_path):
        print(f"Le dossier '{folder_path}' n'existe pas.")
        log(f"Le dossier '{folder_path}' n'existe pas.")
    images = []
    # Parcourir tous les fichiers du dossier
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        # Vérifier si c'est un fichier image
        if os.path.isfile(file_path) and file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
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
images = import_images_from_folder(folder_path) 

#if images:
 #   for image in images :
  #      image[1].show()

