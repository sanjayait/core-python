from PIL import Image,ImageEnhance
import os

# Change image extension
# img1=Image.open('a.jpg')
# img1.save('a1.pdf')

# resize of image
# img1.thumbnail((250,150))  # tuple (250,150)
# img1.save('asmall.jpg')

# sharpness / color / brightness / contrast
img1=Image.open('a.jpg')
# setter=ImageEnhance.Color(img1)
setter=ImageEnhance.Brightness(img1)
setter.enhance(2).show('') # You can save file also

