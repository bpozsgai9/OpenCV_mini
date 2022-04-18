import cv2

def onTrackbarChange(pos):
	global img, substraced

	weight = pos / 100.0
	print(weight)
	weighted = cv2.addWeighted(img, weight, substraced, 1 - weight, 0)
	cv2.imshow("Weighted", weighted)

img = cv2.imread("musk.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original", img)

blured = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow("Gauss blured", blured)

substraced = cv2.multiply(img, 0.25) + cv2.multiply(blured, 0.75)
cv2.imshow("Substraced", substraced)

weighted = cv2.multiply(img, 0.25) + cv2.multiply(substraced, 0.75)
cv2.imshow("Weighted", weighted)

cv2.createTrackbar('Weight', 'Weighted', 50, 100, onTrackbarChange)
onTrackbarChange(0)

cv2.waitKey(0)
cv2.destroyAllWindows()