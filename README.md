# pg2-image-editor

# Ce programme a pour but de pouvoir modifier des images en leur rajoutant des filtres (Flou, Texte, Aquarell ...) 

importation.py

Ce code permet  d'importer toutes les images d'un dossier donné.
Il charge les fichiers image (format .png, .jpg, .jpeg, .bmp, .tiff) à partir d'un répertoire spécifique et les ouvres en utilisant la 
bibliothèque PILLOW qui sont ensuite retourner sous forme de liste d'objet.

Prérequis
-Python 3.10(au minimum)
-Pillow
-Un module personnalisé logger pour la gestion des logs

Pour installer les dépendances entrer cette ligne de commande dans votre terminal "pip install Pillow"

La fonction 'import_images_from_folder' vérifie si le dossier existe et s'il n'existe pas un message d'erreur est envoyer,
elle initialise ensuite une liste vide qui stockera toutes les images importées sous forme de tuple.
La fonction parcourt tous les fichiers du dossier à l'aide de os.listdir(folder_path). Pour chaque fichier dans le dossier, elle construit son chemin complet en utilisant os.path.join(folder_path, file_name).

Pour chaque fichier, on vérifie si c'est bien un fichier image valide (c'est-à-dire un fichier avec l'extension .png, .jpg, .jpeg, .bmp ou .tiff) et l'ouvre si c'est une image.
Si l'image a été ouverte correctement (c'est-à-dire que l'objet image n'est pas None), elle est ajoutée à la liste images sous forme de tuple.

Après avoir parcouru tous les fichiers, la fonction affiche le nombre total d'images importées et enregistre cette information dans le log et retourne la liste images, qui contient toutes les images validées.


filtre.py

Les différentes fonctions permettent de filtrer des images (noir et blanc, floutage, dilatation, pivotation, redimension, écrire sur l'image)
Pour appliquer le filtre entrer dans votre termianl de commande "python3 filtre.py"


La fonction 'blur' permet de flouter l'image, en prenant en parametres images, le nom et n(n sert a définir le degres de floutage 100 étant le maximum).
Elle retourne l'image flouté sinon elle affiche 'Erreur lors de l'application du filtre flou'.

La fonction 'grey' permet de convertir une image en noir et blanc en prenant en parametres l'image et le nom.
Elle retourne l'image en noir et blanc sinon elle affiche 'Erreur lors de l'application du filtre noir et blanc'.

La fonction 'dilated_img' permet de dilater une image en prenant en parametres l'image et le nom et n(n sert a définir le degres de dilatation ).
Elle retourne l'image dilaté sinon elle affiche '"Erreur lors de l'applicaion du filtre dilatation'.

La fonction 'apply_dimensions_filter' permet de modifier la hauteur et la largeur d'une image en prenant en parametres l'image et le scale.
Elle retourne l'image redimensionnée sinon elle affiche 'Erreur lors de l'application du filtre de redimention'.

La fonction 'image_rotated' permet de modifier l'angle de l'image en prenant en paremetre l'image et l'angle, l'angle de l'image pourra etre définit par l'utilisateur.
Elle retourne l'image pivoté en noir et blanc sinon elle affiche 'Erreur lors de la rotation des images'.

La fonction 'apply_writing_filter' permet d'écrire sur une image en prenant en parametres l'image, la posistion et le texte.
Elle retourne l'image avec le texte entrée par l'utilisateur sinon elle affiche 'Erreur lors de l'application du filtre de ecriture'.
