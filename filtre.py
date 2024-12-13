from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageEnhance, ImageOps
from logger import *
from Importation import *

input_folder = "img/default/"  # Dossier contenant les images
output_folder = "img/modified/"  # Dossier pour sauvegarder les images modifiés 

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
        font = ImageFont.truetype("arial.ttf", 60)
        draw = ImageDraw.Draw(images)
        draw.text((position[0], position[1]), text , fill="black", font=font)
        log("Le texte à bien été placé sur l'image")
        return images
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

def image_rotated(images, angle):
    '''
    Pivote les images selon l'angle saisi et les sauvegarde.

    Args:
        images (list): Liste de tuples (nom_fichier, PIL.Image.Image) représentant les images à pivoter.
        output_folder (str): Chemin vers le dossier où sauvegarder les images pivoters.
        angle (float): Angle de rotation en degrés.
    '''
    try:
            # Applique la rotation
            rotated_img = images.rotate(angle, expand=True)
            # Génère le chemin du fichier de sortie
            # Sauvegarde l'image pivoter
            print(f"Image pivoté et sauvegardé")
            log (f"Image pivoté et sauvegardé ")
            return rotated_img
    except Exception as e:
        print(f"Erreur lors de la rotation des images : {e}")
        log(f"Erreur lors de la rotation des images : {e}")


def apply_filter_images(liste_images, nom_effect, param):
    """
    Applique un filtre de flou aux images et les sauvegarde.

    Args:
        images (list): Liste de tuples (nom_fichier, PIL.Image.Image) représentant les images à flouter.
        output_folder (str): Chemin vers le dossier où sauvegarder les images floutées.
    """

    dico = {"blur" : blur , "grey"  : grey , "dilate"  : dilated, "aquarell" : apply_custom_aquarelle_filter, "resize" : apply_dimensions_filter, "rotate" : image_rotated , "text" : apply_writing_filter}
    list_img_modified = []
    try:
        # Crée le dossier de sortie s'il n'existe pas
        for img in liste_images:
            if nom_effect == "grey" or nom_effect == "aquarell" :
                img_filter = dico[nom_effect](img[1])
            elif nom_effect == "text" :
                img_filter = dico[nom_effect](img[1],(int(param[0]),int(param[1])),param[2])
            else : 
                img_filter = dico[nom_effect](img[1],50)
            list_img_modified.append((img[0],img_filter))
            print(f"{nom_effect.upper()} à été applique à toute les images")
            log(f"{nom_effect} à été applique à toute les images")
        return list_img_modified

    except Exception as e:
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
            output_path = os.path.join(output_path, "output.gif")
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

    return create_gif_from_images(input_folder, output_folder, duration), create_single_image_gifs(input_folder, output_folder, duration)

    
gif_gestion(input_folder, output_folder,500)