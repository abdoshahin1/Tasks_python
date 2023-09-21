from PIL import Image

# open the image
myimage = Image.open(r"D:\backend\python\photo\wp3185033.jpg")

# show the image
myimage.show()

# crop the image
image_crop = (100, 200, 150, 250)
test = myimage.crop(image_crop)
test.show()
# convert the image to black and white
test1 = myimage.convert("L")
test1.show()
