from PIL import Image
from PIL import ImageFilter
from logger import *
import os
from Importation import *
from PIL import ImageFont, ImageDraw

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

#apply_blur_filter(images, output_folder)


def image_rotated(images, output_folder, angle):
    '''
    Pivote les images selon l'angle saisi et les sauvegarde.

    Args:
        images (list): Liste de tuples (nom_fichier, PIL.Image.Image) représentant les images à pivoter.
        output_folder (str): Chemin vers le dossier où sauvegarder les images pivoters.
        angle (float): Angle de rotation en degrés.
    '''
    try:
        # Crée le dossier de sortie s'il n'existe pas
        os.makedirs(output_folder, exist_ok=True)
        for img in images:
            # Applique la rotation
            rotated_img = img[1].rotate(angle, expand=True)
            # Génère le chemin du fichier de sortie
            output_path = os.path.join(output_folder, f"rotated_{img[0]}")
            # Sauvegarde l'image pivoter
            rotated_img.save(output_path)
            print(f"Image pivoter sauvegardée : {output_path}")

    except Exception as e:
        print(f"Erreur lors de la rotation des images : {e}")

# Chemins des dossiers
input_folder = "img/default"  # Dossier contenant les images
output_folder_rotate = "img/modified/rotate"  # Dossier pour sauvegarder les images pivoters

# Importation des images
images_list = import_images_from_folder(input_folder)

# Application de la rotation
angle = 40
image_rotated(images_list, output_folder_rotate, angle)
