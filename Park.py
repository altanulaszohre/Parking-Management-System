from turtle import width
import cv2
import pickle

img=cv2.imread('park_img.png')

a, b=33,68

try:
    with open('Car_Park_Pos','rb') as f:
        posList=pickle.load(f)
except:        
    posList=[]

def mouseClick(events,x,y,flags,params):
    if events==cv2.EVENT_LBUTTONDOWN:
        posList.append((x,y))
    if events==cv2.EVENT_RBUTTONDOWN:
        for i,pos in enumerate(posList):
            x1,y1=pos
            if x1<x<x1+a and y1<y<y1+b:
                posList.pop(i)    

    with open('Car_Park_Pos','wb')as f:
        pickle.dump(posList,f)            

while True:
    img=cv2.imread('park_img.png')
    for pos in posList:
        cv2.rectangle(img,pos,(pos[0]+a,pos[1]+b),(255,0,0),2)
    cv2.imshow("image",img)
    cv2.setMouseCallback("image",mouseClick)
    cv2.waitKey(1)