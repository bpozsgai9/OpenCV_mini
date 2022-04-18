import cv2
import numpy as np

img = cv2.imread("musk.jpg", cv2.IMREAD_UNCHANGED)
cv2.imshow("Original", img)

blured = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow("Gauss blured", blured)

substraced = img - blured
cv2.imshow("Substraced", substraced)

weighted = cv2.addWeighted(img, 1, substraced, 0, 0.0)
cv2.imshow("Weighted", weighted)

cv2.waitKey(0)
cv2.destroyAllWindows()