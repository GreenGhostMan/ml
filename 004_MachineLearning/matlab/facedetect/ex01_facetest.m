clear; clc; close all;
faceDetector = vision.CascadeObjectDetector;
I  = imread('training\pyaesoanaung\11.jpg');
bbox = step(faceDetector,I);
im2 = imcrop(I,bbox);
im3 = imresize(im2, [250 250]);
imv = im3(:);
%imshow(I);
imshow(im3);
% imwrite(im3,'5.jpg');