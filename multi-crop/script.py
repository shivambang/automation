import sys
import cv2
import matplotlib.pyplot as plt

r, c = [int(i) for i in sys.argv[1:]]
img = cv2.imread('1.jpg')
height, width, channels = img.shape
b = width/c
h = height/r
for i in range(r):
    for j in range(c):
        y = int(j*h)
        x = int(i*b)
        crop_img = img[x+4:x+int(h)-32, y+12:y+int(h)-8] # Crop from {x, y, w, h } => {0, 0, 300, 400}

        cv2.imwrite(f"images/{4}-{j+1}-{i}.jpg", crop_img)
