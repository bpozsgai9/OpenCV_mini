import cv2

def mouse_move(event, x, y, flags, param):

    global img
    img_height = img.shape[0]
    img_width = img.shape[1]

    if event == cv2.EVENT_MOUSEMOVE:
        
        img = img_clear.copy()
        #vonal kereszttől le és fel
        cv2.line(img, (x, y), (x, img_height), (0, 0, 255), 1)
        cv2.line(img, (x, y), (x, 0), (0, 0, 255), 1)

        #vonal kereszttől balra és jobbra
        cv2.line(img, (x, y), (img_width, y), (0, 0, 255), 1)
        cv2.line(img, (x, y), (0, y), (0, 0, 255), 1)

        #célkereszt karika
        cv2.circle(img, (x, y), 30, (0, 0, 255), 1)

        #megjelenít
        cv2.imshow('KERESZT', img)


img = cv2.imread("pls.jpg")
img_clear = img.copy()
cv2.imshow('KERESZT', img)

cv2.setMouseCallback('KERESZT', mouse_move)

cv2.waitKey(0)