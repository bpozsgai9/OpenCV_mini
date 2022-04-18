import cv2

cv2.namedWindow('Track')
cv2.resizeWindow('Track', 500, 500)

def track(x):
    print(x)

cv2.createTrackbar('min', 'Track', 0, 255, track)

cv2.waitKey(0)
cv2.destroyAllWindows()