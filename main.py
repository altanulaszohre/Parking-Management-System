from sre_constants import SUCCESS
import cv2
import pickle
import cvzone
import numpy as np

cap = cv2.VideoCapture('park_video.mp4')

with open('Car_Park_Pos','rb') as f:
        posList=pickle.load(f)

a, b=33,68

def checkParkingSpace(imgPro,):
    spaceCounter=0
    for pos in posList:
        x,y=pos
        imgCrop=imgPro[y:y+b,x:x+a]
        #cv2.imshow(str(x*y),imgCrop)
        count=cv2.countNonZero(imgCrop)
        cvzone.putTextRect(img,str(count),(x,y),scale=1,thickness=2,offset=0,colorR=(12,23,28))

        if count<500:
            color=(0,255,0)
            tickness=5
            spaceCounter+=1
        else:
            color=(0,0,255)
            tickness=1
        cv2.rectangle(img,pos,(pos[0]+a,pos[1]+b),color,tickness)
    cvzone.putTextRect(img,str(spaceCounter),(70,70),scale=3,thickness=3,offset=15,colorR=(100,255,29))



while True:

    if cap.get(cv2.CAP_PROP_POS_FRAMES)==cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)
    
    success,img=cap.read()
    
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur=cv2.GaussianBlur(imgGray,(3,3),1)
    imgT=cv2.adaptiveThreshold(imgBlur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)
    imgM=cv2.medianBlur(imgT,5)
    kernel=np.ones((3,3),np.uint8)
    imgD=cv2.dilate(imgM,kernel,iterations=1)
    checkParkingSpace(imgD)
    cv2.imshow('auz',img)
    #cv2.imshow('imageGray',imgGray)
    #cv2.imshow('imageBlur',imgBlur)
    #cv2.imshow('imageThreshold',imgT)
    #cv2.imshow('imageMedian',imgM)
    cv2.waitKey(57)
    
