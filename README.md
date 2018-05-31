# CV_project - Fatbardha Hoxha - University of Trento


VOLLEYBALL PROJECT - COMPUTER VISION 
-----------------------------------------------------------------------
 * Library required:
 	- OpnCV 2 -> import cv2
 	- numpy   -> import numpy

 * How to Run the code
 You can run this code with the video that you want.

 1) Add the desired video at line 35:
 	cap = cv2.VideoCapture('test720.mp4')

 2) Select the proper ROI for the video selected:
    #ROI for test720.mp4
    frame2 = frame[20:970, 500:800]

 3) Inizialize the parameters that will be used to evaluate the distance:
 	#distance video to object in meters
 	KNOWN_DISTANCE = 6.00

	#object width in meters
	KNOWN_WIDTH = 0.25

	#object width in pixels
	w_pixel=10.0 
