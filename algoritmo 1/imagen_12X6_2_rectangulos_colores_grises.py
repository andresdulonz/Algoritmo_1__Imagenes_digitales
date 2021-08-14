# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Características de construcción para la imagen
img= np.zeros((12,6), dtype= np.uint8)

# Dibujo en pantalla
img[1:8,1:3]= 10
img[6:10,2:5]= 20

# Características de la salida por pantalla
plt.imshow(img, cmap='gray')
plt.show()
cv2.waitKey(0)