import cv2


imgPath = 'trex.jpg'
img = cv2.imread(imgPath)

# Kép megjelenítése ablakban
cv2.imshow('trex original', img)
cv2.waitKey(2000)

# Tükrözés a függőleges középtengelyre és megjelenítés
flipped = cv2.flip(img, 1)
cv2.imshow('trex flipped y', flipped)
cv2.waitKey(2000)

# Tükrözés mindkét középtengelyre és megjelenítés
flipped2 = cv2.flip(img, -1)
cv2.imshow('trex flipped xy', flipped2)
cv2.waitKey(2000)

# Összes ablak bezárása
cv2.destroyAllWindows()