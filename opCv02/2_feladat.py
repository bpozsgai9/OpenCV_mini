import numpy as np
import cv2

img = np.ndarray((500, 1000, 3), np.uint8) #8bit RGB 1000x500px

#háttérszín fehér
img.fill(255)

# Kör rajzolása az (50, 100) középponttal, 40 sugárral, vörös színnel, kitöltve
cv2.circle(img, (50, 100), 50, (0, 0, 255), -1)
cv2.circle(img, (200, 100), 50, (255, 0, 0), 5)

#vonal(háttér, honnan, hova, szín, vastagság)
cv2.line(img, (125, 25), (125, 175), (0, 255, 0), 5)
cv2.line(img, (300, 25), (300, 175), (200, 200, 200), 10)
cv2.line(img, (550, 25), (550, 175), (0, 0, 0), 5)
cv2.line(img, (700, 25), (700, 175), (255, 0, 255), 5)

#téglalap(háttér, (bal_felso_x, bal_felso_y), (jobb_also_x, jobb_also_y), (b, g, r), vastagsag)
cv2.rectangle(img, (350, 25), (500, 175), (3, 183, 252), -1)

#elipszis(háttér, (kozep_x, kozep_y), (fotengely_hossz, mellektengely_hossz), fotengely_szog, kezdoszog, zaroszog, (b, g, r), vastagsag)
cv2.ellipse(img, (600, 100), (50, 75), 180, 90, 270, (0,0,255), -1)

#szöveg(háttér, 'Szoveg', (bazispont_x, bazispont_y), font, betumeret, (b, g, r), vastagsag, vonaltipus)
cv2.putText(img, 'Ke\'zzel se i\'rok ilyen sze\'pen!', (0, 400), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX , 2, (255, 255, 0), 2, cv2.LINE_AA)

#sokszög, itt háromszög
triangle = np.array([[750, 25], [850, 100], [750, 175]], np.int32)
cv2.fillPoly(img, pts=[triangle], color=(0, 255, 0))


# Kép megjelenítése ablakban
cv2.imshow('image', img)
cv2.waitKey(0)

#Fájlba mentés
#cv2.imwrite('test.png', img)

cv2.destroyAllWindows()