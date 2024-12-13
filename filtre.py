from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageEnhance, ImageOps
from logger import *
from Importation import *

input_folder = "img/default/"  # Dossier contenant les images
output_folder = "img/modified/"  # Dossier pour sauvegarder les images modifiés 

#Fonction qui applique un filtre de flou gaussien à une image.
def blur (image,n) :
    try :
        # Applique le filtre de flou gaussien à l'image avec une intensité n.
        blured_img = image.filter(ImageFilter.GaussianBlur(n))
        log(f"L'image à bien été  flouté")
        return blured_img
    except Exception as e :
        # Log l'erreur en cas d'échec de l'application du filtre.
        log (f"Erreur lors de l'application du filtre flou {e}")
        print(f"Erreur lors de l'application du filtre flou {e}")

#Fonction qui convertie une image en noir et blanc
def grey(image):
    try:
        image_gray = image.convert("L")
        log(f"L'image a bien été convertie en noir et blanc")

        # Retourne l'image convertie.
        return image_gray
    except Exception as e:
        # Log l'erreur en cas d'échec de l'application du filtre.
        log(f"Erreur lors de l'application du filtre noir et blanc : {e}")
        print(f"Erreur lors de l'application du filtre noir et blanc : {e}")

#Fonction qui applique il dilatation sur l'image
def dilated(image, n):
    try:
        image_dilated = image.filter(ImageFilter.MaxFilter(n))
        log(f"L'image a bien été dilatée")

        # Retourne l'image dilatée.
        return image_dilated
    except Exception as e:
        # Log l'erreur en cas d'échec de l'application du filtre.
        log(f"Erreur lors de l'application du filtre dilatation : {e}")
        print(f"Erreur lors de l'application du filtre dilatation : {e}")

#Fonction qui redimensionne une image
def apply_dimensions_filter(images, scale):
    try:
        taille = images.size
        img_resized = images.resize((taille[0] * scale,taille[1] * scale))  # Nouvelle taille (largeur, hauteur)
        log("L'image à bien été redimensionnée")
        #retourne l'image redimensionnée
        return img_resized
    except Exception as e:
        # Log l'erreur en cas d'échec de l'application du filtre.
        log(f"Erreur lors de l'application du filtre de redimention : {e}")
        print(f"Erreur lors de l'application du filtre de redimention : {e}")

#Fonction qui permet d'écrire sur une image
def apply_writing_filter(images, position, text):
    try:
        # Récupère la taille de l'image sous forme de tuple (largeur, hauteur)
        size = images.size 

        # Vérifie si la position donnée est hors des limites de l'image
        if position[0] > size[0] or position[1] > size[1] or position[0] < 0 or position[1] < 0:
            # Affiche un message d'erreur si la position est invalide
            print(f"La position donnée est en dehors de l'image : Taille de l'image {size} et taille donnée {position}")
            log(f"La position donnée est en dehors de l'image : Taille de l'image {size} et taille donnée {position}")
            return 
        
        # Charge la police d'écriture (Arial, taille 60)
        font = ImageFont.truetype("arial.ttf", 60) 
        # Crée un objet de dessin pour l'image
        draw = ImageDraw.Draw(images)
        # Ajoute le texte à la position spécifiée avec la couleur noire
        draw.text((position[0], position[1]), text, fill="black", font=font)
        log("Le texte a bien été placé sur l'image")       
        # Retourne l'image modifiée
        return images

    except Exception as e:
        # Log l'erreur en cas d'échec de l'application du filtre.
        log(f"Erreur lors de l'application du filtre d'écriture : {e}")
        print(f"Erreur lors de l'application du filtre d'écriture : {e}")


def apply_custom_aquarelle_filter(image):
    """
    Applique un effet aquarelle à une image.

    :param image: Objet PIL.Image représentant l'image d'entrée.
    :return: L'image modifiée avec un effet aquarelle.
    """
    try:
        # Étape 1 : Adoucir l'image en appliquant un flou gaussien
        blurred = image.filter(ImageFilter.GaussianBlur(3))

        # Étape 2 : Renforcer les contours de l'image pour imiter un dessin
        edges = image.filter(ImageFilter.CONTOUR)

        # Étape 3 : Combiner les calques flou et contours avec un effet d'opacité
        combined = Image.blend(blurred, edges, 0.4)

        print(f"Effet aquarelle appliqué et sauvegardé")
        log(f"Effet aquarelle appliqué et sauvegardé")
        return combined

    except Exception as e:
        # Log l'erreur en cas d'échec de l'application du filtre.
        print(f"Erreur lors de l'application du filtre aquarelle : {e}")
        log(f"Erreur lors de l'application du filtre aquarelle : {e}")

def image_rotated(images, angle):
    """
    Pivote une image selon un angle donné.

    Args:
        images (PIL.Image.Image): L'image à pivoter.
        angle (float): Angle de rotation en degrés.
    :return: L'image pivotée.
    """
    try:
        # Étape 1 : Appliquer la rotation à l'image
        rotated_img = images.rotate(angle, expand=True)

        print(f"Image pivotée et sauvegardée")
        log(f"Image pivotée et sauvegardée")
        return rotated_img

    except Exception as e:
        # Log l'erreur en cas d'échec de l'application du filtre.
        print(f"Erreur lors de la rotation des images : {e}")
        log(f"Erreur lors de la rotation des images : {e}")

def apply_filter_images(liste_images, nom_effect, param):
    """
    Applique un filtre spécifique à une liste d'images.

    Args:
        liste_images (list): Liste de tuples (nom_fichier, PIL.Image.Image) représentant les images.
        nom_effect (str): Nom du filtre à appliquer (par exemple : "blur", "grey", "aquarell").
        param (list): Paramètres nécessaires au filtre (par exemple : position, texte, etc.).
    :return: Liste d'images modifiées sous forme de tuples (nom_fichier, image_modifiée).
    """
    # Dictionnaire avec les noms des filtres et à quoi il correspondent
    dico = {"blur" : blur , "grey"  : grey , "dilate"  : dilated, "aquarell" : apply_custom_aquarelle_filter, "resize" : apply_dimensions_filter, "rotate" : image_rotated , "text" : apply_writing_filter}
    list_img_modified = []
    try:
        # Boucle à travers les images pour appliquer le filtre spécifié
        for img in liste_images:
            if nom_effect == "grey" or nom_effect == "aquarell":
                # Applique le filtre avec l'image en parametre
                img_filter = dico[nom_effect](img[1])
            elif nom_effect == "text":
                # Applique le filtre texte en utilisant des paramètres spécifiques
                img_filter = dico[nom_effect](img[1], (int(param[0]), int(param[1])), param[2])
            else:
                # Applique les autres filtres avec un paramètre (ici il est de 50)
                img_filter = dico[nom_effect](img[1], 50)

            # Ajoute l'image modifiée à la liste
            list_img_modified.append((img[0], img_filter))

            print(f"{nom_effect.upper()} a été appliqué à toutes les images")
            log(f"{nom_effect} a été appliqué à toutes les images")
        
        # Retourne la liste d'images modifiées
        return list_img_modified

    except Exception as e:
        # Log l'erreur en cas d'échec de l'application du filtre.
        log(f"Erreur lors de l'application du filtre : {e}")
        print(f"Erreur lors de l'application du filtre : {e}")


def create_gif_from_images(input_folder, output_path, duration=500):
    """
    Convertit une série d'images en un GIF animé.

    Args:
        input_folder (str): Dossier contenant les images à utiliser pour le GIF.
        output_path (str): Chemin du fichier GIF ou dossier de sauvegarde.
        duration (int): Durée d'affichage de chaque image en millisecondes.
    """
    images = []
    try:
        # Si output_path est un dossier, créer un chemin par défaut pour le fichier
        if os.path.isdir(output_path):
            output_path =  "output.gif"
        else:
            # Créer le dossier parent si nécessaire
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Vérifie et force l'extension .gif
        if not output_path.lower().endswith(".gif"):
            print("L'extension .gif manquait. Correction automatique...")
            output_path += ".gif"

        # Liste et trie les fichiers du dossier d'entrée
        for file_name in sorted(os.listdir(input_folder)):
            file_path = os.path.join(input_folder, file_name)
            if file_name.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".tiff")):
                try:
                    img = Image.open(file_path)
                    images.append(img)
                    print(f"Image ajoutée au GIF : {file_name}")
                except Exception as e:
                    print(f"Erreur lors de l'ouverture de l'image {file_name} : {e}")

        # Vérifie qu'il y a des images valides
        if not images:
            print("Erreur : Aucune image valide trouvée pour créer un GIF.")
            return

        # Génère le GIF
        try:
            images[0].save(
                output_path,
                save_all=True,
                append_images=images[1:],
                duration=duration,
                loop=0
            )
            print(f"GIF créé avec succès : {output_path}")
        except Exception as e:
            print(f"Erreur lors de la création du GIF : {e}")
    except Exception as e:
        print(f"Erreur lors de l'accès au dossier {input_folder} ou {output_path} : {e}")

def create_single_image_gifs(input_folder, output_folder, duration=500):
    """
    Crée un GIF par image dans le dossier de sortie, avec un seul cycle par GIF.

    Args:
        input_folder (str): Dossier contenant les images.
        output_folder (str): Dossier où enregistrer les GIF.
        duration (int): Durée d'affichage de l'image dans le GIF (millisecondes).
    """
    try:
        # Crée le dossier de sortie s'il n'existe pas
        os.makedirs(output_folder, exist_ok=True)

        # Parcourt les fichiers du dossier d'entrée
        for file_name in sorted(os.listdir(input_folder)):
            if file_name.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".tiff")):
                file_path = os.path.join(input_folder, file_name)
                try:
                    # Ouvre l'image
                    img = Image.open(file_path)

                    # Crée un nom de fichier de sortie pour le GIF
                    gif_name = os.path.splitext(file_name)[0] + ".gif"
                    gif_path = os.path.join(output_folder, gif_name)

                    # Sauvegarde l'image comme un GIF avec un cycle unique
                    img.save(
                        gif_path,
                        save_all=True,     # Indique qu'on génère un GIF
                        append_images=[],  # Pas d'images supplémentaires
                        duration=duration, # Durée de l'image dans le cycle
                        loop=1             # Un seul cycle
                    )
                    print(f"GIF créé : {gif_path}")
                except Exception as e:
                    print(f"Erreur lors de la création du GIF pour {file_name} : {e}")
    except Exception as e:
        print(f"Erreur lors de l'accès aux dossiers : {e}")


def gif_gestion (input_folder, outplut_folder, duration=500):
    create_gif_from_images(input_folder, output_folder, duration), create_single_image_gifs(input_folder, output_folder, duration)

    
gif_gestion(input_folder, output_folder,500)
