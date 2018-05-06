# BlurDetector
Classifies images into blurry and good quality images using Median filter

This repository contains two files.

1) A matlab implmentation
2) Python OpenCV implementation 

The Matlab file uses the Median filter and the difference image to calculate the blur of an image

The Python file uses the Laplacian filter to calculate the blur

blurDetect.py- To use the blurDetect.py use the below command on commandprompt. Make sure You have python 3.6 and OpenCV 3 installed.

USAGE - python blurDetect.py [fullpathname]

fullpathname - This should include the full path name of where the image that you want to check for quality is located.

example - C:/Users/ritesh/test.jpg

