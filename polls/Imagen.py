from PIL import Image, ImageFilter
try:
    original = Image.open("Lenna.png")
except:
    print "Unable to load image"