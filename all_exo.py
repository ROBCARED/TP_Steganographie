from PIL import Image

image_path = input("Entrez le chemin de votre image : ")
print("Image sélectionnée :", image_path)
img = Image.open(image_path)
img.show()