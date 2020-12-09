import cv2
import numpy as np

#img = np.zeros((512,512,3), np.uint8)
img = cv2.imread('189book.png',1)
def click_event(event,x,y,flags,param):
    # if event == cv2.EVENT_LBUTTONDOWN:
    #     print(x,y)
    #     strxy = str(x)+', '+str(y)
    #     font = cv2.FONT_HERSHEY_SIMPLEX
    #     cv2.putText(img,strxy,(x,y),font,0.5,(255,255,0),1,cv2.LINE_AA)
    #     cv2.imshow('image',img)
    
    # if event == cv2.EVENT_RBUTTONDOWN:
    #     blue = img[x,y,0]
    #     green = img[x,y,1]
    #     red = img[x,y,2]

    #     strxy = str(blue)+', '+str(green)+', '+str(red)
    #     font = cv2.FONT_HERSHEY_SIMPLEX
    #     cv2.putText(img,strxy,(x,y),font,0.5,(0,255,255),1,cv2.LINE_AA)
    #     cv2.imshow('image',img)
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),5,(0,0,0),-1)
        cv2.imshow('image',img)
        points.append((x,y))
        if len(points)>=2:
            cv2.line(img,points[-1],points[-2],(255,0,255),5)
            cv2.imshow('image',img)

points = []
cv2.imshow('image',img)
cv2.setMouseCallback('image', click_event)
k = cv2.waitKey()
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite("mouseclick.png", img)
    cv2.destroyAllWindows()