pkg load image
A = imread('Imagenes_5/noir.jpg');
subplot(2,2,1)
imshow(A)
title('Imagen original')

subplot(2,2,2)
imhist(A)
title('Histograma de la imagen A')

A = double(A);
r_min = min(min(A)); 
r_max = max(max(A));
s_min = r_min+75; % s_min debe ser m�s grande que r_min
s_max = r_max+75; % s_max debe ser m�s peque�o que r_max

% Operaci�n de estiramiento
B = ((s_max-s_min)/(r_max-r_min))*(A-r_min) + s_min;
B = uint8(B);
subplot(2,2,3)
imshow(B)
title('Imagen original corregida')

subplot(2,2,4)
imhist(B)
title('Histograma de la imagen B')