import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

kernel = np.ones((3,3))
def Dilation(img, kernel):
    r, c = img.shape
    if np.max(img) == 255:
        img = img / 255
    image_or = img.copy()
    img[0, :] = 0
    img[:, 0] = 0
    img[r - 1, :] = 0
    img[:, c - 1] = 0
    image = img.copy()
    for i in range(r-2):
        for j in range(c-2):
            if image[i+1,j+1]*kernel[1,1] == 1:
                image_or[i:i+3,j:j+3] = image_or[i:i+3,j:j+3] + kernel[0:3,0:3]
    new_image = np.int64(image_or>0)
    return  new_image

def Erosion(img, kernel):
    r , c =img.shape
    if np.max(img) == 255:
        img = img / 255
    image = np.zeros(img.shape)
    for i in range(r - 2):
        for j in range(c - 2):
            flag = np.sum(img[i:i + 3, j:j + 3] * kernel[0:3, 0:3])
            if flag == 9:
                image[i+1,j+1] = img[i+1,j+1]

    new_image = np.int64(image > 0)
    return  new_image

def DistTans(img,kernel):
    image = np.zeros(img.shape)
    while (img.any() == 1):
        erode = Erosion(img,kernel)
        image = image + erode
        img = erode
    return image




def Ske(img):
    kernel = cv.getStructuringElement(cv.MORPH_CROSS, (3, 3))
    SE = cv.getStructuringElement(cv.MORPH_CROSS, (3, 3))
    new_image = np.zeros(img.shape)
    c=0
    w, h = kernel.shape
    size = int(w/2)
    image = img.copy()
    while (img.any() == 1):
        img = cv.erode(image, kernel)
        temp = img.copy()
        # open
        temp = cv.erode(temp, SE)
        temp = cv.dilate(temp, SE)
        temp = img - temp
        # set result
        new_image += temp
        c += 1
        print(c)
        w +=1
        kernel = cv.getStructuringElement(cv.MORPH_CROSS, (2*w+1, 2*w+1))
    return new_image,c

def try_try(img,c):
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3))
    SE = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3))
    new_image = np.zeros(img.shape)
    r = 0
    w, h = kernel.shape
    size = int(w/2)
    image = img.copy()
    for i in range(c-1):
        img = cv.erode(image, kernel)
        temp = img.copy()
        # open
        temp = cv.erode(temp, SE)
        temp = cv.dilate(temp, SE)
        temp = img - temp
        # set result
        #new_image += temp
        r += 1
        print("there%d"%r)
        w +=1
        kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (2*w+1, 2*w+1))
        new_image =  temp
    return new_image , w

def recons(img,r):
    new_image = np.zeros(img.shape)
    c = r
    image = img.copy()
    for i in range(r-1):
        temp2,h = try_try(img,c)
        #cv.imshow("here",temp2)
        SE = cv.getStructuringElement(cv.MORPH_ELLIPSE, (2*h-1, 2*h-1))
        temp3 = cv.dilate(temp2,SE)
        new_image+=temp3
        c = c-1
    return np.uint8(new_image)

def Stad_edg(img,kernel):
    erode = Erosion(img,kernel)
    dilate = Dilation(img,kernel)
    new_image = dilate - erode
    return new_image

def ext_edg(img,kernel):
    dilate = Dilation(img,kernel)
    ret, img = cv.threshold(img, 0, 1, cv.THRESH_BINARY | cv.THRESH_OTSU)
    new_image = dilate - img
    return new_image

def int_edg(img,kernel):
    erode = Erosion(img,kernel) *255
    #ret, img = cv.threshold(img, 0, 1, cv.THRESH_BINARY | cv.THRESH_OTSU)
    new_image = img - erode
    return new_image

def condtionalDilate(img,kernel):
    w,h = img.shape
    line = float(0.5)
    img_line = np.zeros([w, h], dtype='int')
    img_line[:, int(h * line)-5:int(h * line)+5] = 255
    pic = img_line.copy()

    b = 0
    while (True):
        # print(c)
        img_line = Dilation(img_line, kernel).astype(np.int)
        temp = img_line.copy()
        img_line = img_line & img  # 0 & 1
        img_line = img_line.astype(np.int)
        res = temp == img_line
        a = np.sum(res == False)
        if (a == b):
            break
        b = a

    img_l = img_line * 255
    return img_l,pic