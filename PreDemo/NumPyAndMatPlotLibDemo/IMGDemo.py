import numpy as np
from PIL import Image

# im = np.array(Image.open("zmm.jpg").convert('L'))#变黑白
im = np.array(Image.open("img/zmm.jpg"))
# print(im[0][1])

# b = im * (100/255)+150#变淡
b=im*0.8

im = Image.fromarray(b.astype('uint8'))
im.save("img/zmmc.png")
