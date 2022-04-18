import cv2

imgPath = 'trex.jpg'
img = cv2.imread(imgPath)

cv2.imshow('trex', img)

while True:
    key = cv2.waitKey()
    flipped = None
    
    if key == ord('h'):
        #vízszintes tükrözés
        flipped = cv2.flip(img, 0)

    elif key == ord('v'):
        #függőleges tükrözés
        flipped = cv2.flip(img, 1)
    
    elif key == ord('q') or key == 27: #27 == esc
        break;
    
    cv2.imshow('trex', flipped)

cv2.destroyAllWindows()

