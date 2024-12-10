from PIL import Image
from PIL import ImageFilter
from logger import *
import os
from Importation import *

def apply_blur_filter(images, effect , n):
    """
    Applique un filtre de flou aux images et les sauvegarde.

    Args:
        images (list): Liste de tuples (nom_fichier, PIL.Image.Image) représentant les images à flouter.
        output_folder (str): Chemin vers le dossier où sauvegarder les images floutées.
    """
    try:
        # Crée le dossier de sortie s'il n'existe pas
        os.makedirs(output_folder, exist_ok=True)
        for img in images:
            # Applique le filtre de flou
            blurred_img = img[1].filter(ImageFilter.GaussianBlur(100))
            # Génère le chemin du fichier de sortie
            output_path = os.path.join(output_folder, f"blurred_{img[0]}")

            # Sauvegarde l'image floutée
            blurred_img.save(output_path)
            print(f"Image floutée sauvegardée : {output_path}")

    except Exception as e:
        print(f"Erreur lors de l'application du filtre de flou : {e}")

input_folder = "img/default"  # Dossier contenant les images
output_folder = "img/modified"  # Dossier pour sauvegarder les images floutées

images_list = import_images_from_folder(input_folder)
print(images_list[0][1])

apply_blur_filter(images, output_folder)



