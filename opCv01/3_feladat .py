import cv2

imgPath = 'trex.jpg'
img = cv2.imread(imgPath)

while True:
    cv2.imshow('trex', img)
    key = cv2.waitKey(1000)
    
    flipped = cv2.flip(img, 1)
    cv2.imshow('trex', flipped)
    key = cv2.waitKey(1000)

    if key == 27 or key == ord('q'):
        break
    
    
cv2.destroyAllWindows()

