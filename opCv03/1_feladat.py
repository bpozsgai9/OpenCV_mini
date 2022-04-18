import cv2
import numpy as np

img = cv2.imread("logo.png")
img_height = img.shape[0]
img_width = img.shape[1]

canvas = np.ndarray((img_height + 30, img_width + 30, 3), np.uint8)
canvas_height = img.shape[0]
canvas_width = img.shape[1]
canvas.fill(255)

#print(type(img))

for i in range(len(img)):
	for j in range(len(img[i])):
		canvas[i + 15][j + 15] = img[i][j]

line_weight = 15
border_color_inner = (0, 0, 255)
border_color_outer = (0, 255, 255)

#belső
cv2.rectangle(canvas, (30, 30), (img_width, img_height), border_color_inner, line_weight)

#külső
cv2.rectangle(canvas, (15, 15), (canvas_width + 15, canvas_height + 15), border_color_outer, line_weight)


cv2.imshow('logo', canvas)
cv2.waitKey(0)