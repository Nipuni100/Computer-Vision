import cv2
import mediapipe as mp
import time

cap= cv2.VideoCapture(0)

mpHands= mp.solutions.hands
hands= mpHands.Hands() #We will go with the default values 

while True:

    #For running the web cam
    success, img = cap.read()
    imgRGB= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results= hands.process(imgRGB)  #process the image 
    print(results.multi_hand_landmarks)  #check whetehr we detect something

    cv2.imshow("Image", img)
    cv2.waitKey(1)
