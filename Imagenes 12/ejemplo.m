%Compresion y Reconstruccion: Ejemplo con Imagenes
clc; clear; close all
pkg load image
pkg load signal



A = imread("lena.jpg");
subplot(1,2,1)
imshow(A)
title("Imagen Original")

A = double(A);

save("img_original.mat","A");

%Paso 1: Compresion
[m,~] = size(A);
k = m/8; %La imagen tiene k x k bloques de 8 x 8

C = cell(k,k); %Arreglo que contiene en cada entrada el vector comprimido de cada bloque

comp = 50; %Compresion
num_pix = 0;

for i=1:k
     for j=1:k
          Bloque = A(8*(i-1)+1:8*i , 8*(j-1)+1:8*j); %Obtener los bloques 8 x 8
          x = jpeg_compresion(Bloque, comp); %IMPELEMENTAR FUNCION x = jpeg_compresion(A, comp)
          C(i,j) = x;
          num_pix=num_pix+length(x)
     end
end

save("img_comprimida.mat","C")

%Paso 2: Reconstruccion
Ar = zeros(512,512);
for i=1:k
     for j=1:k
          x = cell2mat(C(i,j));
          Aux = jpeg_decompresion(x,comp); %Descomprimir en una matriz de 8x8 %IMPLEMENTAR FUNCION x = jpeg_decompresion(A,comp)

          Ar(8*(i-1)+1:8*i , 8*(j-1)+1:8*j) = Aux; %Asignar a la imagen de salida
          end
end

Ar = uint8(Ar);
subplot(1,2,2);
imshow(Ar);
title("Imagen Reconstruida")