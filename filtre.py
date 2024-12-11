from PIL import Image
from PIL import ImageFilter
from logger import *
from Importation import *

input_folder = "img/default"  # Dossier contenant les images
output_folder = "img/modified"  # Dossier pour sauvegarder les images modifiés 

def blur (image,n) :
    blured_img = image.filter(ImageFilter.GaussianBlur(n))
    return blured_img

def grey (image) :
    image_gray = image.convert("L")
    return image_gray

def dilated (image) :
    image_dilated = image.filter(ImageFilter.MaxFilter(3))
    return image_dilated

def apply_dimentions_filter(images,tuple):
    try:
        img_resized = images.resize(tuple[0],tuple[1])  # Nouvelle taille (largeur, hauteur)
        return img_resized
    except Exception as e:
        log(f"Erreur lors de l'application du filtre de redimention : {e}")
        print(f"Erreur lors de l'application du filtre de redimention : {e}")

def apply_filter_images(liste_images, nom_effect, param):
    """
    Applique un filtre de flou aux images et les sauvegarde.

    Args:
        images (list): Liste de tuples (nom_fichier, PIL.Image.Image) représentant les images à flouter.
        output_folder (str): Chemin vers le dossier où sauvegarder les images floutées.
    """

    dico = {"blur" : blur , "grey"  : grey , "dilated_img"  : dilated}
    list_img_modified = []
    try:
        # Crée le dossier de sortie s'il n'existe pas
        for img in liste_images:
            if nom_effect == "grey" :
                img_filter = dico[nom_effect](img[1])
            else : 
                img_filter = dico[nom_effect](img[1],param)
            # Génère le chemin du fichier de sortie
            output_path = "img/modified/" + img[0]
            # Sauvegarde l'image floutée
            list_img_modified.append(img_filter)
            print(f"{nom_effect} à été applique à toute les images dans default : {output_path}")
            log(f"{nom_effect} à été applique à toute les images dans default : {output_path}")
            return list_img_modified

    except Exception as e:
        log(f"Erreur lors de l'application du filtre : {e}")
        print(f"Erreur lors de l'application du filtre : {e}")

dico = {"blur" : blur , "grey"  : grey , "dilated_img"  : dilated }
liste_images = import_images_from_folder()
img = dico["blur"](liste_images[0][1], 100)
apply_filter_images(liste_images,"grey", None)
#img.show()