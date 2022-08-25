import cv2 as cv;
import numpy as np;
import matplotlib.pyplot as plt;

img = cv.imread('./image/disease.jpg')

plt.imshow(img)

# cv.imshow('image', img)
cv.waitKey(0)