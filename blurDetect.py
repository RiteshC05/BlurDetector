import cv2
import sys
import numpy as np
import math
file_location=sys.argv[1];
im1=cv2.imread(file_location,0)
h,w=im1.shape
sizfilt=round(h/25)
if(sizfilt%2==0):
	sizfilt=sizfilt+1
imm=cv2.medianBlur(im1,sizfilt);
diffvar=cv2.Laplacian(im1, cv2.CV_64F).var()
if diffvar>100:
	print("Not Blurry")
else:
	print("Blurry");
print(diffvar)


