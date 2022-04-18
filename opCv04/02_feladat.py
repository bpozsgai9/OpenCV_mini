import cv2
import numpy as np

#olvas-megjelenít
im = cv2.imread('car_numberplate_rs.jpg', cv2.IMREAD_COLOR)
mask = cv2.imread('car_numberplate_rs_mask.png', cv2.IMREAD_COLOR)

white = { 
    'lower' : np.array([100, 100, 100]),
    'upper' : np.array([255, 255, 255])
}

masked = cv2.bitwise_and(im, mask)
white = cv2.inRange(masked, white['lower'], white['upper'])
cv2.imshow('treshold mask', white)

cv2.waitKey(0)
cv2.destroyAllWindows()