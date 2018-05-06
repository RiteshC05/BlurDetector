%BlurDetector - This code is used to detect if a given image is blurry or
%of good quality
%Author - Ritesh Chidambaram
%Email-riteshchidambaram@gmail.com
im1=imread('filename');%give your filename
gray1=rgb2gray(im1);%converts to grayscale
sizfilt=round(size(gray1)/20);%takes into consideration the size of the image while filtering
imm=medfilt2(gray1,sizfilt);%median filter
diffim=imm-gray1;%Calculates the difference image
% var1=var(im2double(gray1(:)));
% var2=var(im2double(imm(:)));
diffvar=var(im2double(diffim(:)));%VAriance of difference image
if diffvar > 0.004%thresholding
    disp("Not blurry");
else
    disp("Blurry");
end
