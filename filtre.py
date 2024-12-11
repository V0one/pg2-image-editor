from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageEnhance, ImageOps
from logger import *
from Importation import *

input_folder = "img/default"  # Dossier contenant les images
output_folder = "img/modified"  # Dossier pour sauvegarder les images modifiés 

def blur (image,n) :
    try :
        blured_img = image.filter(ImageFilter.GaussianBlur(n))
        log(f"L'image à bien été  flouté")
        return blured_img
    except Exception as e :
        log (f"Erreur lors de l'application du filtre flou {e}")
        print(f"Erreur lors de l'application du filtre flou {e}")

def grey (image) :
    try : 
        image_gray = image.convert("L")
        log(f"L'image à bien été convertie en noir et blanc")
        return image_gray
    except Exception as e :
        log(f"Erreur lors de l'application du filtre noir et blanc {e}")
        print(f"Erreur lors de l'application du filtre noir et blanc {e}")

def dilated (image , n) :
    try : 
        image_dilated = image.filter(ImageFilter.MaxFilter(n))
        log(f"L'image à bien été  dilaté")
        return image_dilated
    except Exception as e : 
        log(f"Erreur lors de l'applicaion du filtre dilatation {e}")
        print(f"Erreur lors de l'applicaion du filtre dilatation {e}")

def apply_dimensions_filter(images, scale):
    try:
        taille = images.size
        img_resized = images.resize((taille[0] * scale,taille[1] * scale))  # Nouvelle taille (largeur, hauteur)
        log("L'image à bien été redimensionnée")
        return img_resized
    except Exception as e:
        log(f"Erreur lors de l'application du filtre de redimention : {e}")
        print(f"Erreur lors de l'application du filtre de redimention : {e}")

def apply_writing_filter(images, position, text):
    try:
        size = images.size 
        if position[0] > size[0] or position[1] > size[1] or position[0] < 0 or position[1] < 0 :
            print(f"La position donnée est en dehors de l'image : Taille de l'image {size} et taille donnée {position}")
            log(f"La position donnée est en dehors de l'image : Taille de l'image {size} et taille donnée {position}")
            return 
        fonte = ImageFont.truetype("Avenir.ttc", size=40)
        draw = ImageDraw.Draw(images)
        draw.text((position[0], position[1]), text , fill="black", font=fonte)
        log("Le texte à bien été placé sur l'image")
        return draw
    except Exception as e:
        log(f"Erreur lors de l'application du filtre de ecriture : {e}")
        print(f"Erreur lors de l'application du filtre de ecriture : {e}")

def apply_custom_aquarelle_filter(image):
    """
    Applique un effet aquarelle similaire à l'exemple fourni.

    :param image: Objet PIL.Image représentant l'image d'entrée.
    :param output_path: Chemin de sauvegarde pour l'image modifiée.
    :return: L'image modifiée.
    """
    try:

        # Étape 1 : Adoucir l'image avec un flou gaussien
        blurred = image.filter(ImageFilter.GaussianBlur(3))

        #Étape 2 : Renforcer les contours pour imiter le dessin
        edges = image.filter(ImageFilter.CONTOUR)

        #Étape 3 : Combiner les calques avec un effet d'opacité
        combined = Image.blend(blurred, edges, 0.4)
        #Sauvegarde de l'image modifiée
        print(f"Effet aquarelle appliqué et sauvegardé : ")
        log(f"Effet aquarelle appliqué et sauvegardé :")
        return combined

    except Exception as e:
        print(f"Erreur lors de l'application du filtre aquarelle : {e}")        

def apply_filter_images(liste_images, nom_effect, param):
    """
    Applique un filtre de flou aux images et les sauvegarde.

    Args:
        images (list): Liste de tuples (nom_fichier, PIL.Image.Image) représentant les images à flouter.
        output_folder (str): Chemin vers le dossier où sauvegarder les images floutées.
    """

    dico = {"blur" : blur , "grey"  : grey , "dilated_img"  : dilated, "aquarell" : apply_custom_aquarelle_filter, "resize" : apply_dimensions_filter }
    list_img_modified = []
    try:
        # Crée le dossier de sortie s'il n'existe pas
        for img in liste_images:
            if nom_effect == "grey" or nom_effect == "" :
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


liste_images = import_images_from_folder()

img =  apply_dimensions_filter(liste_images[0][1],3)

#apply_filter_images(liste_images,"grey", None)
#img.show()