# 1. Start with webcam
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time
import os

cap=cv2.VideoCapture(0)
detector= HandDetector(maxHands=1)

offset= 20
imgSize=300

folder="Data/A"
counter = 0

while True:

    #This part is for video camera
    sucess, img = cap.read()
    hands, img = detector.findHands(img)

#crop the hand image
    if hands:
        hand= hands[0]  #only one hand
        x, y, w, h = hand['bbox'] #give the values

        imgWhite =np.ones((imgSize,imgSize,3), np.uint8)*255 #0-255
        imgCrop = img[y-offset:y+h+offset, x-offset:x+w+offset] #starting and ending height and width

        #fixing some errors so putting exception conditions
        # if imgCrop is not None and imgCrop.size != 0:
        #     cv2.imshow("ImageCrop", imgCrop)
        # else:
        #     print("Error: Image is empty or has a size of zero.")

        imgCropShape=imgCrop.shape
        

        aspectRatio=h/w

        if aspectRatio>1:
            k=imgSize/h
            wCalculated=math.ceil(w*k)
            imgResize=cv2.resize(imgCrop,(wCalculated,imgSize))
            imgResizeShape=imgResize.shape
            #to center the image
            wGap=math.ceil((imgSize-wCalculated)/2)
            imgWhite[:,wGap:wCalculated+wGap] =imgResize

        else:
            k=imgSize/w
            hCalculated=math.ceil(h*k)
            imgResize=cv2.resize(imgCrop,(imgSize,hCalculated))
            imgResizeShape=imgResize.shape
            #to center the image
            hGap=math.ceil((imgSize-hCalculated)/2)
            imgWhite[hGap:hCalculated+hGap, :] =imgResize



        cv2.imshow("ImageCrop", imgCrop)
        cv2.imshow("ImageWhite", imgWhite)

    cv2.imshow("Image", img) #show image
    key=cv2.waitKey(1)
    # if key == ord('q'):
    if key==ord('S') or key == ord('s'):
        counter+=1
        filename = f'{folder}/Image_{time.time()}.jpg'
        cv2.imwrite(filename, imgWhite)
        # cv2.imwrite(f'{folder}/Image_{time.time()}.jpg',imgWhite)
        print(counter)

