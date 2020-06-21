import cv2
import numpy as np
from P5_GrayMorphology1 import *


def stad_Gradient(img,SE):
    erode = GErosion(img,SE)
    dilate = GDilation(img,SE)
    new_image = dilate -erode
    return  new_image

def int_Gradient(img,SE):
    erode = GErosion(img,SE)
    new_image = img -erode
    return  new_image

def ext_Gradient(img,SE):
    dilate = GDilation(img,SE)
    new_image = dilate -img
    return  new_image


def NotExcedd(img, img_mask):
    w, h = img.shape
    img_R = img.copy()
    for i in range(w):
        for j in range(h):
            if img[i, j] > img_mask[i, j]:
                img_R[i, j] = img_mask[i, j]
    return img




def OBR(img):
    w, h = img.shape
    SE = np.ones([3, 3], dtype='int')
    img_O = GOpen(img, SE)

    img_R = np.empty([w, h])
    while (True):
        img_O = GDilation(img_O, SE)
        img_R = NotExcedd(img_O, img)
        if ((img_R == img_O).any()):
            break
    return img_R




def CBR(img):
    w, h = img.shape
    SE = np.ones([3, 3], dtype='int')
    img_C = GClose(img, SE)

    img_R = np.empty([w, h])
    while (True):
        img_C = GDilation(img_C, SE)
        img_R = NotExcedd(img_C, img)
        if ((img_R == img_C).any()):
            break
    return img_R