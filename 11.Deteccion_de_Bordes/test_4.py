import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

A = Image.open("images/cuadro.jpg")
A = np.asarray(A).astype("float64")/255
A = A[:,:,0]

Bx = [[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]]
Bx = [[-1, -2, -1],[0, 0, 0],[1, 2, 1]]

Cx = np.convolve(A,Bx,"same")
Cy = np.convolve(A,By,"same")
C = np.sqrt(np.dot(Cx,Cx)) + np.dot(Cy,Cy))


C[C<0.5] = 0
C[C>=0.5] = 1

B = C

h1 = 1
thetas = np.deg2rad(np.arange(0,180+h1,h1))


m,n = np.shape(B)
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

for r in range(len(lineas_intentos)):
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
            plt.plot([n 1], [xv xv])
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