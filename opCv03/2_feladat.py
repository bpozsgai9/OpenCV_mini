import cv2
import numpy as np

img = cv2.imread('03_pr_formula.png', cv2.IMREAD_COLOR)
img_height = img.shape[0]
img_width = img.shape[1]

canvas = np.ndarray((img_height, img_width, 3), dtype=np.uint8)
canvas.fill(0)

for i in range(len(img)):
  if 0 in img[i]:
        canvas[i] = img[i]

cv2.imshow('canvas', canvas)
cv2.waitKey(0)