import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt



#kernel = np.array([[1,0],[1,1]])
def dilation(img, kernel):
    r, c = img.shape
    image_or = img.copy()
    img[0, :] = 0
    img[:, 0] = 0
    img[r - 1, :] = 0
    img[:, c - 1] = 0
    image = img.copy()
    for i in range(r-1):
        for j in range(c-1):
            if image[i+1,j+1]*kernel[1,1] == 1:
                image_or[i:i+2,j:j+2] = image_or[i:i+2,j:j+2] + kernel[0:2,0:2]
    new_image = np.int64(image_or>0)
    return  new_image

def erosion(img, kernel):
    r, c = img.shape
    image = np.zeros(img.shape)
    for i in range(r-1):
        for j in range(c-1):
            flag = np.sum(img[i:i+2,j:j+2]*kernel[0:2,0:2])
            if  flag== 3:
                image[i+1,j+1] = img[i+1,j+1]

    new_image = np.int64(image>0)
    return  new_image

def opening(img, kernel):
    img_erode = erosion(img,kernel)
    new_image = dilation(img_erode,kernel)
    return new_image

def closing(img, kernel):
    img_dilate = dilation(img,kernel)
    new_image = erosion(img_dilate,kernel)
    return new_image