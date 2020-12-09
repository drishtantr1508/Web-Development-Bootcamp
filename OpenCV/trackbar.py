import cv2
import numpy as np

# img = np.zeros((300,512,3), np.uint8)

# def trackbar_test(x):
#     print(x)

# cv2.namedWindow('Image')

# cv2.createTrackbar('B','Image',0,255,trackbar_test)
# cv2.createTrackbar('G','Image',0,255,trackbar_test)
# cv2.createTrackbar('R','Image',0,255,trackbar_test)
# cv2.createTrackbar('switch', 'Image',0,1,trackbar_test)
# while(1):
#     cv2.imshow("Image",img)
#     k = cv2.waitKey(1) & 0xFF
#     if k == 27:
#         break
#     if k==27:
#         cv2.destroyAllWindows()
#     b = cv2.getTrackbarPos('B','Image')
#     g = cv2.getTrackbarPos('G','Image')
#     r = cv2.getTrackbarPos('R','Image')
#     s = cv2.getTrackbarPos('switch','Image')

#     if s==0:
#         img[:] = 0
#     else:
#         img[:] = [b,g,r]



def trackbar_test(x):
    print(x)
cv2.namedWindow('Image')
cv2.createTrackbar('B','Image',0,255,trackbar_test)
cv2.createTrackbar('G','Image',0,255,trackbar_test)
cv2.createTrackbar('R','Image',0,255,trackbar_test)
cv2.createTrackbar('CP','Image',0,400,trackbar_test)
#cv2.createTrackbar('Switch','Image',0,1,trackbar_test)
cv2.createTrackbar('Gray0/Color1','Image',0,1,trackbar_test)
while(1):
    img = cv2.imread('189book.png',1)
    img = cv2.resize(img,(1600,800))
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    if k==27:
        cv2.destroyAllWindows()

    b = cv2.getTrackbarPos('B','Image')
    g = cv2.getTrackbarPos('G','Image')
    r = cv2.getTrackbarPos('R','Image')
    #s = cv2.getTrackbarPos('switch','Image')
    cp = cv2.getTrackbarPos('CP','Image')
    gc = cv2.getTrackbarPos('Gray0/Color1','Image')

    font = cv2.FONT_HERSHEY_SIMPLEX

    cv2.putText(img, str(cp), (50, 150), font, 6, (b,g,r), 10)

    if gc==0:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        pass

    img = cv2.imshow('Image',img)


    