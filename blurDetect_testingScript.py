import os
import glob
import cv2
import sys
import numpy as np
import math
def isblur( file_location ) :
	im1=cv2.imread(file_location,0)
	h,w=im1.shape
	sizfilt=round(h/25)
	if(sizfilt%2==0):
		sizfilt=sizfilt+1
	imm=cv2.medianBlur(im1,sizfilt);
	diffvar=cv2.Laplacian(im1, cv2.CV_64F).var()
	if diffvar>100:
		print("Not Blurry")
		flag= 1
	else:
		print("Blurry");
		flag= 0
	print(diffvar)
	return flag

def main() : 
	path= sys.argv[1];
	total_count=0;
	blurry_count=0
	non_blurry=0
	for root, dirs, files in os.walk(path):
		for f in files:
			total_count=total_count+1;
			filename=os.path.join(root,f);
			if (isblur(filename)) :
				non_blurry=non_blurry+1;
			else :
				blurry_count=blurry_count+1;
	print(blurry_count);
	print(non_blurry);
	print(total_count);

main()			

