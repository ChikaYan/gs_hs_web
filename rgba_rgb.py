import imageio
import numpy as np

img_path = './teaser.png'

img = imageio.imread(img_path) / 255.

img = img[...,:3] * img[...,3:] + (1-img[...,3:])

imageio.imsave(img_path, (img*255).astype(np.uint8))

