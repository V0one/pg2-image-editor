from PIL import Image
from PIL import ImageFilter
from logger import *
from Importation import *

input_folder = "img/default"  # Dossier contenant les images
output_folder = "img/modified"  # Dossier pour sauvegarder les images modifiés 

def blur (image, n , nom) :
    blured_img = image.filter(ImageFilter.GaussianBlur(n))

    blured_img.save("img/modified/" + nom)

def grey (image, nom) :
    image_gray = image.convert("L")
    image_gray.show() 
    image_gray.save("img/modified/" + nom)

def dilated_img (image, nom) :
    image_dilated = image.filter(ImageFilter.MaxFilter(3))
    image_dilated.show()

def apply_filter_images(liste_images, effect):
    """
    Applique un filtre de flou aux images et les sauvegarde.

    Args:
        images (list): Liste de tuples (nom_fichier, PIL.Image.Image) représentant les images à flouter.
        output_folder (str): Chemin vers le dossier où sauvegarder les images floutées.
    """
    try:
        # Crée le dossier de sortie s'il n'existe pas
        #os.makedirs(output_folder, exist_ok=True)
        for img in liste_images:
            # Applique le filtre de flou
            img_filter = img[1].filter(effect)
            # Génère le chemin du fichier de sortie
            output_path = "img/modified/" + img
            # Sauvegarde l'image floutée
            img_filter.save(output_path)
            print(f"{effect} à été applique à toute les images dans default : {output_path}")
            log(f"{effect} à été applique à toute les images dans default : {output_path}")

    except Exception as e:
        print(f"Erreur lors de l'application du filtre : {e}")