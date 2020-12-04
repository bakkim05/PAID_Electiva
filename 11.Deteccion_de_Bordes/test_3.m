clc; clear; close all
pkg load image
A=imread('images/linea3.jpg');
%Convertir la imagen en binaria
B=im2double(A);
B(B<0.5)=0; B(B>=0.5)=1;
imshow(B)

%Calcular la discretización de theta y rho
%1. Theta: Tomar valores en [0,180] / [0, pi]
h1=0.1;
thetas=deg2rad(0:h1:180);
%2. Rho: Toma valores en [-d,d], donde d=sqrt(m^2+n^2), y [m,n]=size(B)
[m,n]=size(B);
d=sqrt(m^2+n^2);
h2=0.1;
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

lineas_intentos=10;

for r=1:lineas_intentos
  %Encontrar máxima posicion del Acumulador
  [xp,yp]=find(Acumulador==max(max(Acumulador)));
  %Observacion: Si el máximo se repite más de una vez, entonces 
  %             'x' y 'y' son vectores que tienen las posiciones

  %Graficar

  for k=1:length(xp)
    thetaMax=thetas(xp(k));
    rhoMax=rhos(yp(k));

    if abs(sin(thetaMax))<10^-4
      x_v=rhoMax/cos(thetaMax);
      line([n 1], [x_v x_v],'LineWidth',2)  
    else
      %Calcular pendiente
      pendiente=-cos(thetaMax)/sin(thetaMax);
      interseccion=rhoMax/sin(thetaMax);
      %Necesitamos el punto (1,y1)
      y1=pendiente*1+interseccion;
      %Necesitamos el punto (m,ym)
      ym=pendiente*m+interseccion;
      %Necesitamos el punto (x1,1)
      x1=(1-interseccion)/pendiente;
      %Necesitamos el punto (xn,n)
      xn=(n-interseccion)/pendiente;
      if pendiente>0
        if 0<y1
          line([y1 n], [1 xn],'LineWidth',2)  
        else
          line([1 ym], [x1 m],'LineWidth',2)  
        end    
      else
        if y1>m
          line([ym n], [m xn],'LineWidth',2)  
        else
          line([y1 1], [1 x1],'LineWidth',2)  
        end    
      end  
    end
    Acumulador(xp(k),yp(k))=0;
  end
end
