import cv2
import numpy as np


def GetTheLittle(size,pic,i,j):

    gap = int(size/2)
    mat = pic[i-gap:i+gap+1,j-gap:j+gap+1]

    mat = mat.astype(np.int16)
    #print(mat)
    return mat

def GDilation(img, SE):
    w, h = img.shape

    # img.dtype = 'bool'
    (SE_w, SE_h) = SE.shape
    # print(SE)
    img_R = np.array([w, h])
    img_R = img.copy()

    # Dilation
    gap = int(SE_w / 2)

    for i in range(gap, w - gap):
        for j in range(gap, h - gap):
            mat = GetTheLittle(SE_h,img,i,j)
            # if np.max(mat) != np.min(mat): # cannot become faster
            mat = mat + SE
            max = int(np.max(mat))
            # img_R[i-gap:i+gap+1,j-gap:j+gap+1] = max
            img_R[i, j] = max
    return img_R


def GErosion(img, SE):
    w, h = img.shape

    # img.dtype = 'bool'
    (SE_w, SE_h) = SE.shape
    # print(SE)
    img_R = np.array([w, h])
    img_R = img.copy()

    # Dilation
    gap = int(SE_w / 2)

    for i in range(gap, w - gap):
        for j in range(gap, h - gap):
            mat = GetTheLittle(SE_h, img, i, j)
            mat = abs(mat - SE)
            min = int(np.min(mat))
            # img_R[i-gap:i+gap+1,j-gap:j+gap+1] = min
            img_R[i, j] = min

    return img_R


def GOpen(img, SE):
    img_RE = GErosion(img, SE)
    img_RED = GDilation(img_RE, SE)

    return img_RED


def GClose(img, SE):
    img_RD = GDilation(img, SE)
    img_RDE = GErosion(img_RD, SE)
    return img_RDE