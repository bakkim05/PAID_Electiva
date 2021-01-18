import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


A = Image.open("images/linea1.jpg")
A = np.array(A).astype(np.double)

A[A<0.5] = 0
A[A>=0.5] = 1

h1 = 1
thetas = np.deg2rad(np.arange(0,180,h1))

m,n,_ = np.shape(A)
d = np.sqrt(m**2 + n**2)
h2 = 1
rhos = np.arange(-d,d,h2)

Acumulador = np.zeros((len(thetas),len(rhos)))
[x_borde, y_borde,_] = np.where(A)

for i in range(len(x_borde)):
    for theta_indice in range(len(thetas)):
        theta = thetas[theta_indice]
        rho = x_borde[i]*np.cos(theta) + y_borde[i]*np.cos(theta)
        rho_indice = np.argmin(np.abs(rhos-rho))
        Acumulador[theta_indice,rho_indice] += 1

[xp,yp] = np.where(Acumulador == np.max(np.max(Acumulador)))
thetaMax = thetas[xp]
rhoMax = rhos[yp]

print(thetaMax)
print(rhoMax)