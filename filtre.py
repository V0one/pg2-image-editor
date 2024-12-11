from PIL import Image
from PIL import ImageFilter
from Importation import *

 
img = Image.open("img/default/1.jpeg")
print(img)


def blur (image, n , nom) :
    blured_img = image.filter(ImageFilter.GaussianBlur(n))

    blured_img.save("img/modified/" + nom)


blur(img,100, "1.jpeg")


def grey (image, nom) :
    image_gray = image.convert("L")
    image_gray.show() 
    image_gray.save("img/modified/" + nom)

def dilated_img (image, nom) :
    image_dilated = image.filter(ImageFilter.MaxFilter(3))
    image_dilated.show()

dilated_img(img,"aaa")    
