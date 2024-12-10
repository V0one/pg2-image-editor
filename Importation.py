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
    images = []
    try:
        # Vérifie que le dossier existe
        if not os.path.exists(folder_path):
            log(f"Le dossier '{folder_path}' n'existe pas.")
            raise FileNotFoundError(f"Le dossier '{folder_path}' n'existe pas.")

        # Parcours tous les fichiers du dossier
        for filename in os.listdir(folder_path):
            # Construction du chemin complet du fichier
            file_path = os.path.join(folder_path, filename)

            # Vérifie si c'est une image valide
            try:
                with Image.open(file_path) as img:
                    images.append(img.copy())  # Copie l'image pour éviter les problèmes de fermeture
            except (IOError, SyntaxError):
                log(f"Le fichier '{filename}' n'est pas une image valide, il est ignoré.")
                print(f"Le fichier '{filename}' n'est pas une image valide, il est ignoré.")
        
        if not images:
            log("Aucune image valide n'a été trouvée dans le dossier.")
            print("Aucune image valide n'a été trouvée dans le dossier.")
        return images

    except Exception as e:
        log(f"Erreur lors de l'importation des images : {e}")
        print(f"Erreur lors de l'importation des images : {e}")
        return []

# Exemple d'utilisation
folder = "img/default/"  # Remplacez par le chemin de votre dossier
images_list = import_images_from_folder(folder)

print(f"{len(images_list)} image(s) importée(s).")
