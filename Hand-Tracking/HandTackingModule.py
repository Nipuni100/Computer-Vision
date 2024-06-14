import cv2
import mediapipe as mp
import time

class HandDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode  #We are creating an object, it's self
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon= trackCon

        self.mpHands= mp.solutions.hands
        self.hands= self.mpHands.Hands(self.mode,self.maxHands,self.detectionCon,self.trackCon) #We will go with the default values 
        self.mpDraw= mp.solutions.drawing_utils

    def findHands(self,img,draw=True):
 
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # imgRGB= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results= self.hands.process(imgRGB)  #process the image 
        # print(results.multi_hand_landmarks)  #check whetehr we detect something

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks: #Go through each hand
                if draw :
                    #To draw all points
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)  #original image

        return img
                # for id, lm in enumerate(handLms.landmark): #exact index number of our 
                #     # print(id,lm)
                #     h, w, c= img.shape #taking the height, width and the channel
                #     cx, cy = int(lm.x * w), int(lm.y * h)  #it's not for a specifc one
                #     print(id, cx, cy)

                #     if id==4: #id==0 :- palm, id==4 :- finger tip thumb
                #         cv2.circle(img, (cx, cy), 25, (255,0,255), cv2.FILLED)




def main():
    pTime =0
    cTime =0

    cap= cv2.VideoCapture(0)
    detector= HandDetector()

    while True:

        #For running the web cam
        success, img = cap.read()
        img=detector.findHands(img)

        cTime= time.time()
        fps= 1/(cTime-pTime)
        pTime= cTime

        cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)

if __name__== "__main__" :
    main()