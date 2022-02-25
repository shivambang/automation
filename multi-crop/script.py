import sys
import cv2
import matplotlib.pyplot as plt

r, c = [int(i) for i in sys.argv[1:]]
img = cv2.imread('2.jpg')
height, width, channels = img.shape
b = width/c
h = height/r
# print(b, h)
for i in range(r):
    for j in range(c):
        y = int(j*b)
        x = int(i*h)
        crop_img = img[x+64:int(x+h)-16, y+32:int(y+b)-32] # Crop from {x, y, w, h } => {0, 0, 300, 400}
        # print(x, x+int(h), y, y+int(b))
        cv2.imshow("cropped", crop_img)
        cv2.waitKey(0)
        # cv2.imwrite(f"images/{4}-{2*(j+1)}-{i}.jpg", crop_img)
