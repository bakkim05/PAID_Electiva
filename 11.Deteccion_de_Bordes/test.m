clc; clear; close all
pkg load image
A=imread('images/linea1.jpg');
%Convertir la imagen en binaria
B=im2double(A);
B(B<0.5)=0; B(B>=0.5)=1;
imshow(B)

%Calcular la discretización de theta y rho
%1. Theta: Tomar valores en [0,180] / [0, pi]
h1=1;
thetas=deg2rad(0:h1:180);
%2. Rho: Toma valores en [-d,d], donde d=sqrt(m^2+n^2), y [m,n]=size(B)
[m,n]=size(B);
d=sqrt(m^2+n^2);
h2=1;
rhos=-d:h2:d;

%Crear matriz de acumulación
Acumulador=zeros(length(thetas),length(rhos));

%Llenar la matriz de acumulación

[x_b,y_b]=find(B);

for i=1:length(x_b) %Recorrer los puntos del borde
  for theta_ind=1:length(thetas)
    theta=thetas(theta_ind);
    rho=x_b(i)*cos(theta)+y_b(i)*sin(theta);
    [~,rho_ind]=min(abs(rhos-rho));
    Acumulador(theta_ind,rho_ind)+=1;
  end  
end

%Mostrar graficamente el comportamiento del acumulador
%figure
%surface(thetas,rhos,Acumulador','EdgeColor','none')
%xlabel('rho')
%ylabel('theta')

%Encontrar la posición donde el Acumulador alcanza el máxima
[xp,yp]=find(Acumulador==max(max(Acumulador)));


%Graficar
thetaMax = thetas(xp(1));
rhoMax = rhos(yp(1));

pendiente = -cos(thetaMax)/sin(thetaMax);
interseccion = rhoMax/sin(thetaMax);

%Para graficar una linea recta, se utiliza el comando line
%Necesitamos un dos puntos
%Punto1 (1,y1)
y1 = pendiente*1 + interseccion;
%Punto2 (xn,n)
xn = (n-interseccion)/pendiente;

%Graficar la linea rectangle
line([y1 1], [1 xn], "LineWidth", 2)