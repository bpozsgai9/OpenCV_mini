
import cv2

img = cv2.imread('me.PNG', cv2.IMREAD_GRAYSCALE)
#cv2.imshow('Original', img)

blurred = cv2.GaussianBlur(img, (0, 0), 2.0)
#cv2.imshow('Blurred', blurred)

edges = cv2.Canny(blurred, 200, 800, None, 5, True)
cv2.imshow('Canny portre`', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
