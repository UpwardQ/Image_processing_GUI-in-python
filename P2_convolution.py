import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def Roberts(img):
    r , c = img.shape
    new_img = np.zeros(img.shape)
    new_imageX = np.zeros(img.shape)
    new_imageY = np.zeros(img.shape)
    suanziX = np.array([[-1, 0], [0, 1]])
    suanziY = np.array([[0, -1], [1, 0]])
    image = cv.copyMakeBorder(img, 1, 1, 1, 1, cv.BORDER_DEFAULT)  # 外圈复制一圈
    for i in range(r):
        for j in range(c):
            new_imageX[i,j] = abs(np.sum(image[i:i+2,j:j+2] * suanziX))
            new_imageY[i, j] = abs(np.sum(image[i:i + 2, j:j + 2] * suanziY))
            new_img[i , j ] = (new_imageX[i , j ] * new_imageX[i , j ] + new_imageY[i , j ] *
                                       new_imageY[i , j ]) ** 0.5
    return np.uint8(new_imageX),np.uint8(new_imageY),np.uint8(new_img)


def Sobel(img):
    r, c = img.shape
    new_image = np.zeros((r, c))
    new_imageX = np.zeros(img.shape)
    new_imageY = np.zeros(img.shape)
    s_suanziX = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])      # X方向
    s_suanziY = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    for i in range(r-2):
        for j in range(c-2):
            new_imageX[i+1, j+1] = abs(np.sum(img[i:i+3, j:j+3] * s_suanziX))
            new_imageY[i+1, j+1] = abs(np.sum(img[i:i+3, j:j+3] * s_suanziY))
            new_image[i+1, j+1] = (new_imageX[i+1, j+1]*new_imageX[i+1,j+1] + new_imageY[i+1, j+1]*new_imageY[i+1,j+1])**0.5
    return np.uint8(new_imageX),np.uint8(new_imageY),np.uint8(new_image)
    # return np.uint8(new_imageY)
    #return np.uint8(new_image)  # 无方向算子处理的图像


def Prewitt(img):
    r, c = img.shape
    new_image = np.zeros((r, c))
    new_imageX = np.zeros(img.shape)
    new_imageY = np.zeros(img.shape)
    p_suanziX = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])  # X方向
    p_suanziY = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    for i in range(r-2):
        for j in range(c-2):
            new_imageX[i+1, j+1] = abs(np.sum(img[i:i+3, j:j+3] * p_suanziX))
            new_imageY[i+1, j+1] = abs(np.sum(img[i:i+3, j:j+3] * p_suanziY))
            new_image[i+1, j+1] = (new_imageX[i+1, j+1]*new_imageX[i+1,j+1] + new_imageY[i+1, j+1]*new_imageY[i+1,j+1])**0.5
    return np.uint8(new_imageX),np.uint8(new_imageY),np.uint8(new_image)


def mean_filter(img):
    r , c = img.shape
    new_image = np.zeros(img.shape)
    image = np.pad(img, ((1, 1), (1, 1)), 'constant', constant_values=(0, 0))
    for i in range(r):
        for j in range(c):
            new_image[i,j] = abs(np.sum(image[i:i+3,j:j+3])/(3*3))
    return new_image

def median_filter(img):
    r , c =img.shape
    image = np.pad(img, ((1, 1), (1, 1)), 'constant', constant_values=(0, 0))
    new_image = np.zeros(img.shape)
    for i in range(r):
        for j in range(c):
            new_image[i,j] = np.median(image[i:i+3,j:j+3])
    return new_image

def Gaussian_filter(img,kernel):
    r , c = img.shape
    image = np.pad(img, ((1, 1), (1, 1)), 'constant', constant_values=(0, 0))
    new_image = np.zeros(img.shape)
    sqrt_k = kernel**0.5
    suanzi = np.array([[1,sqrt_k,1],[sqrt_k,kernel,sqrt_k],[1,sqrt_k,1]])
    for i in range(r):
        for j in range(c):
            new_image[i,j] = abs(np.sum(image[i:i+3,j:j+3]*suanzi)/(kernel*kernel))
    return new_image
