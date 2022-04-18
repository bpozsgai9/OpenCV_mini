import cv2

def onTrackbarChange(pos):
    global im1, im2

    
    weight = pos / 100.0
    print(str(1 - weight))
    #imblend = cv2.multiply(im1, weight) + cv2.multiply(im2, 1 - weight)
    imblend = cv2.addWeighted(im1, weight, im2, 1 - weight, 0)
    cv2.imshow('imblend', imblend)

im1 = cv2.imread('ct04.png', cv2.IMREAD_GRAYSCALE)
#im1 = cv2.imread('mr04.png', cv2.IMREAD_GRAYSCALE)
im2 = cv2.imread('pet04.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow('im1', im1)
cv2.imshow('im2', im2)

impadd = im1 + im2
cv2.imshow('impadd', impadd)

imocvadd = cv2.add(im1, im2)
cv2.imshow('imocvadd', imocvadd)

imblend = cv2.multiply(im1, 0.25) + cv2.multiply(im2, 0.75)
cv2.imshow('imblend', imblend)

cv2.createTrackbar('Weight', 'imblend', 50, 100, onTrackbarChange)
onTrackbarChange(50)

cv2.waitKey(0)
cv2.destroyAllWindows()
