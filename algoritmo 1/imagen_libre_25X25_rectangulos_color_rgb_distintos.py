# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Características de construcción para la imagen
img= np.zeros((25,25,3), dtype= np.uint8)

# Dibujo en pantalla
img[5:12,7:10,1]= 200
img[6:8,4:9,0]= 115
img[7:11,8:14,2]= 225

# Conversión de formato BGR a RGB
rgb= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Características de la salida por pantalla
plt.imshow(rgb)
plt.show()
cv2.waitKey(0)