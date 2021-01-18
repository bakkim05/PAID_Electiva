import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

A = Image.open("images/linea1.jpg")
A = np.asarray(A).astype("float64")/255
A = A[:,:,0]
A[A>=0.5]=1
A[A<0.5]=0
plt.imshow(A, cmap=plt.cm.gray)

h1 = 1
thetas = np.deg2rad(np.arange(0,180+h1,h1))

m,n = np.shape(A)
d = np.sqrt(m**2 + n**2)
h2 = 1
rhos = np.arange(-d,d,h2)

Acumulador = np.zeros((len(thetas),len(rhos)))
x_borde,y_borde = np.nonzero(A)

for i in range(len(x_borde)):
    for theta_indice in range(len(thetas)):
        theta = thetas[theta_indice]
        rho = x_borde[i]*np.cos(theta) + y_borde[i]*np.sin(theta)
        rho_indice = np.argmin(np.abs(rhos-rho))
        Acumulador[theta_indice,rho_indice] += 1

xp,yp = np.unravel_index(np.argmax(Acumulador,axis=None),Acumulador.shape)
thetaMax = thetas[xp]
rhoMax = rhos[yp]
pendiente = -np.cos(thetaMax) / np.sin(thetaMax)
interseccion = rhoMax / np.sin(thetaMax)

y1 = pendiente*1 + interseccion
xn = (n-interseccion)/pendiente

plt.plot([y1, n],[1, xn])
plt.xlim([0,n])
plt.ylim([m,0])
plt.show() 