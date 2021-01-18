import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

A = Image.open("images/linea3.jpg")
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

lineas_intentos = 10

for r in range(lineas_intentos):
    #HAY UN PROBLEMA AQUI
    #XP RETORNA UN UNICO NUMERO Y DEBERIA RETORNAR UN ARRAY
    xp,yp = np.where(Acumulador == np.max(np.max(Acumulador)))

    y1 = 0
    xn = 0

    for k in range(len(xp)):
        thetaMax = thetas[k]
        rhoMax = rhos[k]

        if (np.abs(np.sin(thetaMax)) < 10**-5):
            xv = rhoMax / np.cos(thetaMax)
            plt.plot([n, 1], [xv, xv])
        else:
            pendiente = -np.cos(thetaMax) / np.sin(thetaMax)
            interseccion = rhoMax / np.sin(thetaMax)

            y1 = pendiente*1 + interseccion
            ym = pendiente*m + interseccion

            x1 = (1-interseccion)/pendiente
            xn = (n-interseccion)/pendiente

            if (pendiente > 0):
                if (0 < y1):
                    plt.plot([y1, n], [1, xn])
                else:
                    plt.plot([1, ym], [x1, m])
            else:
                if (y1 > m):
                    plt.plot([ym, n], [m, xn])
                else:
                    plt.plot([y1, 1], [1 , x1])

    plt.plot([y1, n], [1, xn])

plt.xlim([0,n])
plt.ylim([m,0])
plt.show() 