% imshow(), size()
clear; close; clc;
img = imread('apple.jpg');
img2 = rgb2gray(img);

a = size(img);
b = size(img2);

imshow(img);
figure;
imshow(img2);
