# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Características de construcción para la imagen
img= np.zeros((9,8,3), dtype= np.uint8)

# Dibujo en pantalla
img[2,2,2]= 255
img[2,5,0]= 255
img[5,2,1]= 175

# Conversión de formato BGR a RGB
rgb= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Características de la salida por pantalla
plt.imshow(rgb)
plt.show()