import cv2
import os



def import_images_from_folder(folder_path):
    """
    Importer toutes les images d'un dossier.
    
    Args:
        folder_path (str): Chemin vers le dossier contenant les images.
        
    Returns:
        list: Liste des images chargées sous forme de matrices NumPy.
    """
    images = []
    if not os.path.exists(folder_path):
        print(f"Le dossier '{folder_path}' n'existe pas.")
        return images

    # Parcourir tous les fichiers du dossier
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        # Vérifier si c'est un fichier image
        if os.path.isfile(file_path) and file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            image = cv2.imread(file_path)
            if image is not None:
                images.append(image)
            else:
                print(f"Impossible de lire l'image : {file_name}")
    
    print(f"{len(images)} images ont été importées depuis '{folder_path}'.")
    return images


folder_path = "img/default"
images = import_images_from_folder(folder_path)

# Exemple pour afficher une image importée
if images:
    cv2.imshow("Image Exemple", images[0])
    cv2.waitKey(0)
    cv2.destroyAllWindows()
