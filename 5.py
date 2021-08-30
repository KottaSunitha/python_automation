from PIL import Image

image = Image.open(r"C:\Users\sk21163\Downloads\panda_PNG2.png")
jpg = image.convert('RGB')
jpg.save(r"C:\Users\sk21163\Downloads\panda_PNG23.jpg")
print("success")
