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
#input_folder = "img/default/"  # Dossier contenant les images
#output_folder = "img/modified"  # Dossier pour sauvegarder les images modifiés 

#images_list = import_images_from_folder(input_folder)


#apply_blur_filter(images, output_folder)


from PIL import Image, ImageFilter, ImageOps, ImageEnhance

def apply_custom_aquarelle_filter(image, output_path):
    """
    Applique un effet aquarelle similaire à l'exemple fourni.
    
    :param image: Objet PIL.Image représentant l'image d'entrée.
    :param output_path: Chemin de sauvegarde pour l'image modifiée.
    :return: L'image modifiée.
    """
    try:

        # Étape 1 : Adoucir l'image avec un flou gaussien
        blurred = image.filter(ImageFilter.GaussianBlur(2))
        
        # Étape 2 : Renforcer les contours pour imiter le dessin
        edges = image.filter(ImageFilter.CONTOUR)
        
        # Étape 3 : Combiner les calques avec un effet d'opacité
        combined = Image.blend(blurred, edges, alpha=0.5)

        
        # Étape 4 : Augmenter la luminosité et le contraste
        enhancer = ImageEnhance.Brightness(combined)
        brightened = enhancer.enhance(1.5)  # Augmente la luminosité
        

        contrast = ImageEnhance.Contrast(brightened)
        
        final_image = contrast.enhance(1.3)  # Augmente le contraste
        
        # Étape 5 : Ajout d'un effet "vignette" ou bordure blanche
        vignette = ImageOps.expand(final_image, border=30, fill="white")
        
  
        
        # Sauvegarde de l'image modifiée
        vignette.save(output_path)
        print(f"Effet aquarelle appliqué et sauvegardé : {output_path}")

        return blurred
    
    except Exception as e:
        print(f"Erreur lors de l'application du filtre aquarelle : {e}")
        

img = Image.open("img/defualt/1.jpeg")
img.show()

