#Below line of codes tells about the usage of pillow for  image manipulation. 

# load and show an image with Pillow
from PIL import Image
from numpy import asarray

# load the image from diectory
image = Image.open('/root/Desktop/Weed2_.jpg')

# summarize some details about the image
print(image.format)
print(image.mode)
print(image.size)

#convert image as a numpy array
data = asarray(image)
print(data)
#printing the shape of image
print(data.shape)

# show the image
image.show()
