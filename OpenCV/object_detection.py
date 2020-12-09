import cv2
import numpy as np

cv2.namedWindow('TrackBar')
cv2.namedWindow('Another TrackBar')

img = cv2.imread('photos/color_ball.jpg', 1)

cv2.imshow('Image', img)

k = cv2.waitKey()
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("photos/small_book_copy.png", book_img)
    cv2.destroyAllWindows()
