# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Características de construcción para la imagen
img= np.zeros((8,15), dtype= np.uint8)

# Dibujo en pantalla
img[1,5]= 255
img[3,7]= 200
img[5,9]= 125

# Características de la salida por pantalla
plt.imshow(img, cmap= 'gray')
plt.show()
cv2.waitKey(0)