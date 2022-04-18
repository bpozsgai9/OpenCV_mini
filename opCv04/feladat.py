import cv2
import numpy as np

im = cv2.imread('shapes_10.jpg', cv2.IMREAD_COLOR)
cv2.imshow('Eredeti', im)

blue = { 
    'lower' : np.array([120, 0, 0]),
    'upper' : np.array([255, 100, 100]) 
}

red = { 
    'lower' : np.array([0, 0, 120]),
    'upper' : np.array([100, 100, 255])
}

green = { 
    'lower' : np.array([[0, 120, 0]]),
    'upper' : np.array([100, 255, 100])
} #:(

yellow = { 
    'lower' : np.array([0, 120, 0]),
    'upper' : np.array([100, 255, 255])
}

res_blue = cv2.inRange(im, blue['lower'], blue['upper'])
#cv2.imshow('blue', res_blue)

res_red = cv2.inRange(im, red['lower'], red['upper'])
#cv2.imshow('red', res_red)

res_green = cv2.inRange(im, green['lower'], green['upper'])
cv2.imshow('green', res_green)

res_yellow = cv2.inRange(im, yellow['lower'], yellow['upper'])
#cv2.imshow('yellow', res_yellow)

cv2.waitKey(0)
cv2.destroyAllWindows()