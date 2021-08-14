# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Tipo de imagen que se construye
# im= np.zeros((5,10), dtype= np.uint8)
im= np.zeros((5,10,3), dtype= np.uint8)


# Dibujamos pixeles gris
# im[1,1]= 255
# im[3,3]= 100

# Dibujamos filas gris
# im[2,0:10]= 125
# Dibujamos columnas gris
# im[0:5,4]= 200

# Dibujamos matrices gris
# im[3:10,6:9]= 225

#dibujamos pixel de color
# 0 es azul
# 1 es verde
# 2 es rojo
im[0,0,0]= 255
im[0,2,1]= 255
im[0,4,2]= 255

# Dibujamos filas gris
im[2,3:10,2]= 125
# Dibujamos columnas gris
im[3:5,4,0]= 200



# coversión de formato BGR a RGB
rgb= cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

# Imagen en escala de grises
# plt.imshow(im, cmap= 'gray')
# plt.imshow(im)
# Imagen en escala RGB
plt.imshow(rgb)
plt.show()
# mantener la ventana abierta hasta que el usuario la cierre
cv2.waitKey(0)