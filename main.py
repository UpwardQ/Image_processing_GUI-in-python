#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os, sys
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
from tkinter.messagebox import *
#from markbookmain import *
from PIL import Image, ImageTk
# import tkinter.filedialog as tkFileDialog
# import tkinter.simpledialog as tkSimpleDialog    #askstring()
from P1_historgam import *
from P2_convolution import *
from P3_morphology1 import *
from P4_morphology2 import *
from P5_GrayMorphology1 import *
from P6_GrayMorphology2 import *
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import cv2 as cv
from PIL import Image, ImageTk
from matplotlib import pyplot as plt





class Application_ui(Frame):
    # 这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('Form1')
        self.master.geometry("775x575+300+30")
        self.createWidgets()
        self.path = 'E:\pictures'
        self.pack()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.TabStrip1 = Notebook(self.top)
        self.TabStrip1.place(relx=0.035, rely=0.035, relwidth=0.92, relheight=0.92)

        self.TabStrip1__Tab1 = Frame(self.TabStrip1)

        f1 = Frame(self.TabStrip1__Tab1, width=100, height=480, bg="white")
        f1.place(x=10, y=20)
        global f2
        f2 = Frame(self.TabStrip1__Tab1, width=570, height=480, bg="white")
        f2.place(x=130, y=20)
        self.btn01 = Button(f1, text="showpicture",
                            width=10, height=1, anchor=E, command=self.showpicture)  # login是自己定义的，anchor可以控制位置
        self.btn01.place(relx=0.1, rely=0.1)
        self.btn02 = Button(f1, text="historgam",
                            width=10, height=1, anchor=E, command=self.historgam)  # login是自己定义的，anchor可以控制位置
        self.btn02.place(relx=0.1, rely=0.3)
        self.btn03 = Button(f1, text="OTSU",
                            width=10, height=1, anchor=E, command=self.OTSU)  # login是自己定义的，anchor可以控制位置
        self.btn03.place(relx=0.1, rely=0.5)
        self.btn04 = Button(f1, text="Entropy",
                            width=10, height=1, anchor=E, command=self.Entropy)  # login是自己定义的，anchor可以控制位置
        self.btn04.place(relx=0.1, rely=0.7)
        self.sc = Scale(f2, from_=0, to=255, length=200, tickinterval=50, orient=HORIZONTAL, command=self.Scale1)
        self.sc.place(relx=0.6, rely=0.85)
        self.TabStrip1.add(self.TabStrip1__Tab1, text='P1-Binary_Historgam')

        # 第二个界面
        self.TabStrip1__Tab2 = Frame(self.TabStrip1)
        f3 = Frame(self.TabStrip1__Tab2, width=100, height=480, bg="white")
        f3.place(x=10, y=20)
        global f4
        f4 = Frame(self.TabStrip1__Tab2, width=570, height=480, bg="white")
        f4.place(x=130, y=20)
        f3.btn01 = Button(f3, text="showpicture",
                          width=10, height=1, anchor=E, command=self.showpicture2)  # login是自己定义的，anchor可以控制位置
        f3.btn01.place(relx=0.1, rely=0.1)
        f3.btn02 = Button(f3, text="roberts",
                          width=10, height=1, anchor=E, command=self.roberts)  # login是自己定义的，anchor可以控制位置
        f3.btn02.place(relx=0.1, rely=0.2)
        f3.btn03 = Button(f3, text="Sobel",
                          width=10, height=1, anchor=E, command=self.sobel)  # login是自己定义的，anchor可以控制位置
        f3.btn03.place(relx=0.1, rely=0.3)
        f3.btn04 = Button(f3, text="Prewitt",
                          width=10, height=1, anchor=E, command=self.prewitt)  # login是自己定义的，anchor可以控制位置
        f3.btn04.place(relx=0.1, rely=0.4)
        f3.btn05 = Button(f3, text="Mean",
                          width=10, height=1, anchor=E, command=self.Mean)  # login是自己定义的，anchor可以控制位置
        f3.btn05.place(relx=0.1, rely=0.5)
        f3.btn06 = Button(f3, text="Median",
                          width=10, height=1, anchor=E, command=self.Median)  # login是自己定义的，anchor可以控制位置
        f3.btn06.place(relx=0.1, rely=0.6)
        f3.btn07 = Button(f3, text="Gaussian",
                          width=10, height=1, anchor=E, command=self.Gaussian)  # login是自己定义的，anchor可以控制位置
        f3.btn07.place(relx=0.1, rely=0.7)

        self.TabStrip1.add(self.TabStrip1__Tab2, text='P2-Convolution')

        # 第三个界面
        self.TabStrip1__Tab3 = Frame(self.TabStrip1)
        f5 = Frame(self.TabStrip1__Tab3, width=100, height=480, bg="white")
        f5.place(x=10, y=20)
        global f6
        f6 = Frame(self.TabStrip1__Tab3, width=570, height=480, bg="white")
        f6.place(x=130, y=20)
        f5.btn01 = Button(f5, text="showpicture",
                          width=10, height=1, anchor=E, command=self.showpicture3)  # login是自己定义的，anchor可以控制位置
        f5.btn01.place(relx=0.1, rely=0.1)
        f5.btn02 = Button(f5, text="erosion",
                          width=10, height=1, anchor=E, command=self.Erosion)  # login是自己定义的，anchor可以控制位置
        f5.btn02.place(relx=0.1, rely=0.2)
        f5.btn03 = Button(f5, text="dilation",
                          width=10, height=1, anchor=E, command=self.Dilation)  # login是自己定义的，anchor可以控制位置
        f5.btn03.place(relx=0.1, rely=0.3)
        f5.btn04 = Button(f5, text="open",
                          width=10, height=1, anchor=E, command=self.Open)  # login是自己定义的，anchor可以控制位置
        f5.btn04.place(relx=0.1, rely=0.4)
        f5.btn05 = Button(f5, text="close",
                          width=10, height=1, anchor=E, command=self.Close)  # login是自己定义的，anchor可以控制位置
        f5.btn05.place(relx=0.1, rely=0.5)

        self.TabStrip1.add(self.TabStrip1__Tab3, text='P3-Morphology1')

        # 第四个界面
        self.TabStrip1__Tab4 = Frame(self.TabStrip1)
        f7 = Frame(self.TabStrip1__Tab4, width=100, height=480, bg="white")
        f7.place(x=10, y=20)
        global f8
        f8 = Frame(self.TabStrip1__Tab4, width=570, height=480, bg="white")
        f8.place(x=130, y=20)
        f7.btn01 = Button(f7, text="showpicture",
                          width=10, height=1, anchor=E, command=self.showpicture4)  # login是自己定义的，anchor可以控制位置
        f7.btn01.place(relx=0.1, rely=0.1)
        f7.btn02 = Button(f7, text="Distrans",
                          width=10, height=1, anchor=E, command=self.Distrans)  # login是自己定义的，anchor可以控制位置
        f7.btn02.place(relx=0.1, rely=0.2)
        f7.btn03 = Button(f7, text="Skeleton",
                          width=10, height=1, anchor=E, command=self.Skeleton)  # login是自己定义的，anchor可以控制位置
        f7.btn03.place(relx=0.1, rely=0.3)
        f7.btn04 = Button(f7, text="Recontrus",
                          width=10, height=1, anchor=E, command=self.Recontrustion)  # login是自己定义的，anchor可以控制位置
        f7.btn04.place(relx=0.1, rely=0.4)
        f7.btn05 = Button(f7, text="Ext_Edge",
                          width=10, height=1, anchor=E, command=self.Ext_Edge)  # login是自己定义的，anchor可以控制位置
        f7.btn05.place(relx=0.1, rely=0.5)
        f7.btn06 = Button(f7, text="int_Edge",
                          width=10, height=1, anchor=E, command=self.Int_Edge)  # login是自己定义的，anchor可以控制位置
        f7.btn06.place(relx=0.1, rely=0.6)
        f7.btn07 = Button(f7, text="Stad_Edge",
                          width=10, height=1, anchor=E, command=self.Stad_Edge)  # login是自己定义的，anchor可以控制位置
        f7.btn07.place(relx=0.1, rely=0.7)
        f7.btn08 = Button(f7, text="CondDilated",
                          width=10, height=1, anchor=E, command=self.CondDilated)  # login是自己定义的，anchor可以控制位置
        f7.btn08.place(relx=0.1, rely=0.8)

        self.TabStrip1.add(self.TabStrip1__Tab4, text='P4-Morphology2')

        # 第五个界面
        self.TabStrip1__Tab5 = Frame(self.TabStrip1)
        f9 = Frame(self.TabStrip1__Tab5, width=100, height=480, bg="white")
        f9.place(x=10, y=20)
        global f10
        f10 = Frame(self.TabStrip1__Tab5, width=570, height=480, bg="white")
        f10.place(x=130, y=20)
        f9.btn01 = Button(f9, text="showpicture",
                          width=10, height=1, anchor=E, command=self.showpicture5)  # login是自己定义的，anchor可以控制位置
        f9.btn01.place(relx=0.1, rely=0.1)
        f9.btn02 = Button(f9, text="GErosion",
                          width=10, height=1, anchor=E, command=self.GErosion)  # login是自己定义的，anchor可以控制位置
        f9.btn02.place(relx=0.1, rely=0.2)
        f9.btn03 = Button(f9, text="GDilation",
                          width=10, height=1, anchor=E, command=self.GDilation)  # login是自己定义的，anchor可以控制位置
        f9.btn03.place(relx=0.1, rely=0.3)
        f9.btn04 = Button(f9, text="GOpening",
                          width=10, height=1, anchor=E, command=self.GOpening)  # login是自己定义的，anchor可以控制位置
        f9.btn04.place(relx=0.1, rely=0.4)
        f9.btn05 = Button(f9, text="GClosing",
                          width=10, height=1, anchor=E, command=self.GClosing)  # login是自己定义的，anchor可以控制位置
        f9.btn05.place(relx=0.1, rely=0.5)

        self.TabStrip1.add(self.TabStrip1__Tab5, text='P5-Morphology_gray1')

        # 第六个界面
        self.TabStrip1__Tab6 = Frame(self.TabStrip1)
        f11 = Frame(self.TabStrip1__Tab6, width=100, height=480, bg="white")
        f11.place(x=10, y=20)
        global f12
        f12 = Frame(self.TabStrip1__Tab6, width=570, height=480, bg="white")
        f12.place(x=130, y=20)
        f11.btn01 = Button(f11, text="showpicture",
                           width=10, height=1, anchor=E, command=self.showpicture6)  # login是自己定义的，anchor可以控制位置
        f11.btn01.place(relx=0.1, rely=0.1)
        f11.btn02 = Button(f11, text="GExt_Edge",
                           width=10, height=1, anchor=E, command=self.GExt_Edge)  # login是自己定义的，anchor可以控制位置
        f11.btn02.place(relx=0.1, rely=0.2)
        f11.btn03 = Button(f11, text="GInt_Edge",
                           width=10, height=1, anchor=E, command=self.GInt_Edge)  # login是自己定义的，anchor可以控制位置
        f11.btn03.place(relx=0.1, rely=0.3)
        f11.btn04 = Button(f11, text="GStad_Edge",
                           width=10, height=1, anchor=E, command=self.GStad_Edge)  # login是自己定义的，anchor可以控制位置
        f11.btn04.place(relx=0.1, rely=0.4)
        f11.btn05 = Button(f11, text="GOBR",
                           width=10, height=1, anchor=E, command=self.GOBR)  # login是自己定义的，anchor可以控制位置
        f11.btn05.place(relx=0.1, rely=0.5)
        f11.btn06 = Button(f11, text="GCBR",
                           width=10, height=1, anchor=E, command=self.GCBR)  # login是自己定义的，anchor可以控制位置
        f11.btn06.place(relx=0.1, rely=0.6)

        self.TabStrip1.add(self.TabStrip1__Tab6, text='P6-Morphology_gray2')


class Application(Application_ui):
    # 这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)
        self.path = 'E:\pictures'

    def showpicture(self):
        global img_png
        self.file_path = filedialog.askopenfilename()
        img_open = Image.open(self.file_path)
        dst = img_open.resize((200, 200))
        img_png = ImageTk.PhotoImage(dst)
        label_img = Label(f2, image=img_png, width=200, height=200)
        label_img.place(relx=0.06, rely=0.055)
        label01 = Label(f2, text="original", width=10, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.15, rely=0.01)

    def historgam(self):
        global img_png_h
        image = cv.imread(self.file_path)
        image1 = plt.hist(image.ravel(), 256, [0, 256])  # 统计称256个bin
        plt.savefig('images/test1.jpg')
        img_open = Image.open('images/test1.jpg')
        dst = img_open.resize((200, 200))
        img_png_h = ImageTk.PhotoImage(dst)
        label_img = Label(f2, image=img_png_h, width=200, height=200)
        label_img.place(relx=0.06, rely=0.53)
        label01 = Label(f2, text="historgam", width=10, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.15, rely=0.48)

    def OTSU(self):
        global img_png_b
        image = cv.imread(self.file_path, cv.IMREAD_GRAYSCALE)
        thresold = otsu_threshold(image)
        # print(thresold)
        ret, binary = cv.threshold(image, thresold, 255, cv.THRESH_BINARY)
        cv.imwrite("images/binary_pollen.jpg", binary)
        image1 = Image.open("images/binary_pollen.jpg")
        dst = image1.resize((200, 200))
        img_png_b = ImageTk.PhotoImage(dst)
        label_img = Label(f2, image=img_png_b, width=200, height=200)
        label_img.place(relx=0.5, rely=0.055)
        self.label01 = Label(f2, text="thresold:%s" % thresold, width=12, height=1,
                             bg="white", fg="black")
        self.label01.place(relx=0.82, rely=0.3)
        label01 = Label(f2, text="OTSU", width=10, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.6, rely=0.01)

    def Entropy(self):
        global img_png_b
        image = cv.imread(self.file_path, cv.IMREAD_GRAYSCALE)
        thresold = segment(image)
        # print(thresold)
        ret, binary = cv.threshold(image, thresold, 255, cv.THRESH_BINARY)
        cv.imwrite("images/binary_pollen.jpg", binary)
        image1 = Image.open("images/binary_pollen.jpg")
        dst = image1.resize((200, 200))
        img_png_b = ImageTk.PhotoImage(dst)
        label_img = Label(f2, image=img_png_b, width=200, height=200)
        label_img.place(relx=0.5, rely=0.055)
        self.label02 = Label(f2, text="thresold:%s" % thresold, width=12, height=1,
                             bg="white", fg="black")
        self.label02.place(relx=0.82, rely=0.3)
        label01 = Label(f2, text="Entropy", width=10, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.6, rely=0.01)

    def Scale1(self, value):
        global img_png_v
        image = cv.imread(self.file_path, cv.IMREAD_GRAYSCALE)
        # thresold = segment(image)
        # print(thresold)
        a = int(value)
        ret, binary = cv.threshold(image, a, 255, cv.THRESH_BINARY)
        cv.imwrite("images/binary_pollen.jpg", binary)
        image1 = Image.open("images/binary_pollen.jpg")
        dst = image1.resize((150, 150))
        img_png_v = ImageTk.PhotoImage(dst)
        label_img = Label(f2, image=img_png_v, width=150, height=150)
        label_img.place(relx=0.5, rely=0.53)
        label01 = Label(f2, text="change_thresold", width=15, height=1,
                        bg="white", fg="black")

        label01.place(relx=0.6, rely=0.48)
        pass

    def showpicture2(self):
        global img_png_2
        self.file_path = filedialog.askopenfilename()
        img_open = Image.open(self.file_path)
        dst = img_open.resize((200, 200))
        img_png_2 = ImageTk.PhotoImage(dst)
        label_img = Label(f4, image=img_png_2, width=200, height=200)
        label_img.place(relx=0.06, rely=0.055)
        label01 = Label(f4, text="original", width=10, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.15, rely=0.01)

    def roberts(self):
        global img_png_rx, img_png_ry, img_png_r
        image = cv.imread(self.file_path, cv.IMREAD_GRAYSCALE)
        robert = Roberts(image)[2]
        name = 'images\Robert.jpg';
        cv.imwrite(name, robert)

        '''
        #X方向
        robertX = roberts(image)[0]
        nameX = 'images\X.jpg' ; cv.imwrite(nameX,robertX)
        img_robertX = Image.open(nameX)
        dst= img_robertX.resize((150, 150))
        img_png_rx = ImageTk.PhotoImage(dst)
        label_imgx = Label(f4, image=img_png_rx,width=150,height=150)
        label_imgx.place(relx=0.5,rely=0.1)

        #Y方向
        robertY = roberts(image)[1]
        nameY = 'images\Y.jpg' ; cv.imwrite(nameY,robertY)
        img_robertY = Image.open(nameY)
        dst= img_robertY.resize((150, 150))
        img_png_ry = ImageTk.PhotoImage(dst)
        label_imgy = Label(f4, image=img_png_ry,width=150,height=150)
        label_imgy.place(relx=0.1,rely=0.55)
        '''
        # 综合
        img_robert = Image.open(name)
        dst = img_robert.resize((200, 200))
        img_png_r = ImageTk.PhotoImage(dst)
        label_img = Label(f4, image=img_png_r, width=200, height=200)
        label_img.place(relx=0.5, rely=0.055)
        label01 = Label(f4, text="Robert", width=10, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.6, rely=0.01)

    def sobel(self):
        global img_S
        image = cv.imread(self.file_path, cv.IMREAD_GRAYSCALE)
        sobel = Sobel(image)[2]
        name = 'images\Sobel.jpg';
        cv.imwrite(name, sobel)
        # 综合
        img_robert = Image.open(name)
        dst = img_robert.resize((200, 200))
        img_S = ImageTk.PhotoImage(dst)
        label_img = Label(f4, image=img_S, width=200, height=200)
        label_img.place(relx=0.06, rely=0.53)
        label01 = Label(f4, text="Sobel", width=10, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.15, rely=0.48)

    def prewitt(self):
        global img_p
        image = cv.imread(self.file_path, cv.IMREAD_GRAYSCALE)
        prewitt = Prewitt(image)[2]
        name = 'images\Prewitt.jpg';
        cv.imwrite(name, prewitt)
        # 综合
        img_robert = Image.open(name)
        dst = img_robert.resize((200, 200))
        img_p = ImageTk.PhotoImage(dst)
        label_img = Label(f4, image=img_p, width=200, height=200)
        label_img.place(relx=0.5, rely=0.53)
        label01 = Label(f4, text="prewitt", width=10, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.6, rely=0.48)

    def Mean(self):
        global img_m
        image = cv.imread(self.file_path, cv.IMREAD_GRAYSCALE)
        mean = mean_filter(image)
        name = 'images\mean.jpg';
        cv.imwrite(name, mean)
        # 综合
        img_robert = Image.open(name)
        dst = img_robert.resize((200, 200))
        img_m = ImageTk.PhotoImage(dst)
        label_img = Label(f4, image=img_m, width=200, height=200)
        label_img.place(relx=0.5, rely=0.055)
        label01 = Label(f4, text="Mean_filter", width=10, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.6, rely=0.01)

    def Median(self):
        global img_mid
        image = cv.imread(self.file_path, cv.IMREAD_GRAYSCALE)
        median = median_filter(image)
        name = 'images\median.jpg';
        cv.imwrite(name, median)
        # 综合
        img_robert = Image.open(name)
        dst = img_robert.resize((200, 200))
        img_mid = ImageTk.PhotoImage(dst)
        label_img = Label(f4, image=img_mid, width=200, height=200)
        label_img.place(relx=0.06, rely=0.53)
        label01 = Label(f4, text="Median", width=10, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.15, rely=0.48)

    def Gaussian(self):
        global img_gu
        image = cv.imread(self.file_path, cv.IMREAD_GRAYSCALE)
        guassian = Gaussian_filter(image, 3)
        name = 'images\gaussian.jpg';
        cv.imwrite(name, guassian)
        # 综合
        img_robert = Image.open(name)
        dst = img_robert.resize((200, 200))
        img_gu = ImageTk.PhotoImage(dst)
        label_img = Label(f4, image=img_gu, width=200, height=200)
        label_img.place(relx=0.5, rely=0.53)
        label01 = Label(f4, text="Gaussian", width=10, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.6, rely=0.48)

    def showpicture3(self):
        global img_png_3
        self.file_path = filedialog.askopenfilename()
        img_open = Image.open(self.file_path)
        dst = img_open.resize((200, 200))
        img_png_3 = ImageTk.PhotoImage(dst)
        label_img = Label(f6, image=img_png_3, width=200, height=200)
        label_img.place(relx=0.06, rely=0.055)
        label01 = Label(f6, text="original", width=10, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.15, rely=0.01)

    def Erosion(self):
        global img_E
        kernel = np.array([[1, 0], [1, 1]])
        image = cv.imread(self.file_path, cv.IMREAD_GRAYSCALE)
        ret, image_bin = cv.threshold(image, 0, 1, cv.THRESH_BINARY | cv.THRESH_OTSU)
        erode = erosion(image_bin, kernel)
        name = 'images\deoc_erode.jpg';
        cv.imwrite(name, erode * 255)
        # 综合
        img_robert = Image.open(name)
        dst = img_robert.resize((200, 200))
        img_E = ImageTk.PhotoImage(dst)
        label_img = Label(f6, image=img_E, width=200, height=200)
        label_img.place(relx=0.5, rely=0.055)
        label01 = Label(f6, text="Erosion", width=10, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.6, rely=0.01)

    def Dilation(self):
        global img_D
        kernel = np.array([[1, 0], [1, 1]])
        image = cv.imread(self.file_path, cv.IMREAD_GRAYSCALE)
        ret, image_bin = cv.threshold(image, 0, 1, cv.THRESH_BINARY | cv.THRESH_OTSU)
        dilate = dilation(image_bin, kernel)
        name = 'images\deoc_dilate.jpg';
        cv.imwrite(name, dilate * 255)
        # 综合
        img_robert = Image.open(name)
        dst = img_robert.resize((200, 200))
        img_D = ImageTk.PhotoImage(dst)
        label_img = Label(f6, image=img_D, width=200, height=200)
        label_img.place(relx=0.06, rely=0.53)
        label01 = Label(f6, text="Dilation", width=10, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.15, rely=0.48)

    def Open(self):
        global img_O
        kernel = np.array([[1, 0], [1, 1]])
        image = cv.imread(self.file_path, cv.IMREAD_GRAYSCALE)
        ret, image_bin = cv.threshold(image, 0, 1, cv.THRESH_BINARY | cv.THRESH_OTSU)
        Opening = opening(image_bin, kernel)
        name = 'images\deoc_open.jpg';
        cv.imwrite(name, Opening * 255)
        # 综合
        img_robert = Image.open(name)
        dst = img_robert.resize((200, 200))
        img_O = ImageTk.PhotoImage(dst)
        label_img = Label(f6, image=img_O, width=200, height=200)
        label_img.place(relx=0.5, rely=0.53)
        label01 = Label(f6, text="Opening", width=10, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.6, rely=0.48)

    def Close(self):
        global img_C
        kernel = np.array([[1, 0], [1, 1]])
        image = cv.imread(self.file_path, cv.IMREAD_GRAYSCALE)
        ret, image_bin = cv.threshold(image, 0, 1, cv.THRESH_BINARY | cv.THRESH_OTSU)
        Closing = closing(image_bin, kernel)
        name = 'images\deoc_close.jpg';
        cv.imwrite(name, Closing * 255)
        # 综合
        img_robert = Image.open(name)
        dst = img_robert.resize((200, 200))
        img_C = ImageTk.PhotoImage(dst)
        label_img = Label(f6, image=img_C, width=200, height=200)
        label_img.place(relx=0.5, rely=0.53)
        label01 = Label(f6, text="Closing", width=10, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.6, rely=0.48)

    def showpicture4(self):
        global img_png_4
        self.file_path = filedialog.askopenfilename()
        img_open = Image.open(self.file_path)
        dst = img_open.resize((200, 200))
        img_png_4 = ImageTk.PhotoImage(dst)
        label_img = Label(f8, image=img_png_4, width=200, height=200)
        label_img.place(relx=0.06, rely=0.055)
        label01 = Label(f8, text="original", width=10, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.15, rely=0.01)

    def Distrans(self):
        global img_Dis
        kernel = np.ones((3, 3))
        image = cv.imread(self.file_path, cv.IMREAD_GRAYSCALE)
        ret, image_bin = cv.threshold(image, 0, 1, cv.THRESH_BINARY | cv.THRESH_OTSU)
        dis = DistTans(image_bin, kernel)
        name = 'images\deoc_distrans.jpg';
        cv.imwrite(name, dis * 5)
        # 综合
        img_robert = Image.open(name)
        dst = img_robert.resize((200, 200))
        img_Dis = ImageTk.PhotoImage(dst)
        label_img = Label(f8, image=img_Dis, width=200, height=200)
        label_img.place(relx=0.5, rely=0.055)
        label01 = Label(f8, text="distrans", width=10, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.6, rely=0.01)

    def Skeleton(self):
        global img_SK
        image = cv.imread(self.file_path, cv.IMREAD_GRAYSCALE)
        ret, image_bin = cv.threshold(image, 0, 1, cv.THRESH_BINARY | cv.THRESH_OTSU)
        dilate, c = Ske(image_bin)
        name = 'images\sketelon.jpg';
        cv.imwrite(name, dilate * 255)
        # 综合
        img_robert = Image.open(name)
        dst = img_robert.resize((200, 200))
        img_SK = ImageTk.PhotoImage(dst)
        label_img = Label(f8, image=img_SK, width=200, height=200)
        label_img.place(relx=0.06, rely=0.53)
        label01 = Label(f8, text="Skeleton", width=10, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.15, rely=0.48)

    def Recontrustion(self):
        global img_re
        image = cv.imread(self.file_path, cv.IMREAD_GRAYSCALE)
        dilate, a = Ske(image)
        recons1 = recons(image,a)
        name = 'images\krecon.jpg';
        cv.imwrite(name, recons1)
        # 综合
        img_robert = Image.open(name)
        dst = img_robert.resize((200, 200))
        img_re = ImageTk.PhotoImage(dst)
        label_img = Label(f8, image=img_re, width=200, height=200)
        label_img.place(relx=0.5, rely=0.53)
        label01 = Label(f8, text="Reconstruction", width=15, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.6, rely=0.48)

    def Ext_Edge(self):
        global img_Ex
        kernel = np.ones((3, 3))
        image = cv.imread(self.file_path, cv.IMREAD_GRAYSCALE)
        ret, image_bin = cv.threshold(image, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
        image_ext = ext_edg(image_bin, kernel)
        name = 'images\ext_edge.jpg';
        cv.imwrite(name, image_ext * 255)
        # 综合
        img_robert = Image.open(name)
        dst = img_robert.resize((200, 200))
        img_Ex = ImageTk.PhotoImage(dst)
        label_img = Label(f8, image=img_Ex, width=200, height=200)
        label_img.place(relx=0.5, rely=0.055)
        label01 = Label(f8, text="Ext_Edge", width=10, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.6, rely=0.01)

    def Int_Edge(self):
        global img_In
        kernel = np.ones((3, 3))
        image = cv.imread(self.file_path, cv.IMREAD_GRAYSCALE)
        ret, image_bin = cv.threshold(image, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
        image_In = ext_edg(image_bin, kernel)
        name = 'images\int_edge.jpg';
        cv.imwrite(name, image_In * 255)
        # 综合
        img_robert = Image.open(name)
        dst = img_robert.resize((200, 200))
        img_In = ImageTk.PhotoImage(dst)
        label_img = Label(f8, image=img_In, width=200, height=200)
        label_img.place(relx=0.06, rely=0.53)
        label01 = Label(f8, text="Dilation", width=10, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.15, rely=0.48)

    def Stad_Edge(self):
        global img_st
        kernel = np.ones((3, 3))
        image = cv.imread(self.file_path, cv.IMREAD_GRAYSCALE)
        ret, image_bin = cv.threshold(image, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
        image_st = Stad_edg(image_bin, kernel)
        name = 'images\int_edge.jpg';
        cv.imwrite(name, image_st * 255)
        # 综合
        img_robert = Image.open(name)
        dst = img_robert.resize((200, 200))
        img_st = ImageTk.PhotoImage(dst)
        label_img = Label(f8, image=img_st, width=200, height=200)
        label_img.place(relx=0.5, rely=0.53)
        label01 = Label(f8, text="Closing", width=10, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.6, rely=0.48)

    def CondDilated(self):
        global img_l, img_condD
        kernel = np.ones((3, 3))
        image = cv.imread(self.file_path, cv.IMREAD_GRAYSCALE)
        ret, image_bin = cv.threshold(image, 0, 1, cv.THRESH_BINARY | cv.THRESH_OTSU)
        img_condDi, image_line = condtionalDilate(image_bin, kernel)
        name_img = 'images\img_conditioanD.jpg';
        cv.imwrite(name_img, img_condDi * 255)
        name = 'images\img_line.jpg';
        cv.imwrite(name, image_line * 255)
        # 综合
        img_robert = Image.open(name)
        dst1 = img_robert.resize((200, 200))
        img_l = ImageTk.PhotoImage(dst1)
        label_img = Label(f8, image=img_l, width=200, height=200)
        label_img.place(relx=0.06, rely=0.53)
        label01 = Label(f8, text="line", width=10, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.15, rely=0.48)

        img_robert = Image.open(name_img)
        dst = img_robert.resize((200, 200))
        img_condD = ImageTk.PhotoImage(dst)
        label_img = Label(f8, image=img_condD, width=200, height=200)
        label_img.place(relx=0.5, rely=0.53)
        label01 = Label(f8, text="conditional_dilation", width=10, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.6, rely=0.48)

    def showpicture5(self):
        global img_png_5
        self.file_path = filedialog.askopenfilename()
        img_open = Image.open(self.file_path)
        dst = img_open.resize((200, 200))
        img_png_5 = ImageTk.PhotoImage(dst)
        label_img = Label(f10, image=img_png_5, width=200, height=200)
        label_img.place(relx=0.06, rely=0.055)
        label01 = Label(f10, text="original", width=10, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.15, rely=0.01)

    def GErosion(self):
        global img_GE
        kernel = np.ones([5, 5], dtype='int')
        image = cv.imread(self.file_path, cv.IMREAD_GRAYSCALE)
        erode = GErosion(image, kernel)
        name = 'images\ori_erode.jpg'
        cv.imwrite(name, erode)
        # 综合
        img_robert = Image.open(name)
        dst = img_robert.resize((200, 200))
        img_GE = ImageTk.PhotoImage(dst)
        label_img = Label(f10, image=img_GE, width=200, height=200)
        label_img.place(relx=0.5, rely=0.055)
        label01 = Label(f10, text="GErosion", width=10, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.6, rely=0.01)

    def GDilation(self):
        global img_GD
        kernel = np.ones([5, 5], dtype='int')
        image = cv.imread(self.file_path, cv.IMREAD_GRAYSCALE)
        dilate = GDilation(image, kernel)
        name = 'images\ori_dilate.jpg';
        cv.imwrite(name, dilate)
        # 综合
        img_robert = Image.open(name)
        dst = img_robert.resize((200, 200))
        img_GD = ImageTk.PhotoImage(dst)
        label_img = Label(f10, image=img_GD, width=200, height=200)
        label_img.place(relx=0.06, rely=0.53)
        label01 = Label(f10, text="GDilation", width=10, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.15, rely=0.48)

    def GOpening(self):
        global img_GO
        kernel = np.ones([5, 5], dtype='int')

        image = cv.imread(self.file_path, cv.IMREAD_GRAYSCALE)
        Opening = GOpen(image, kernel)
        name = 'images\ori_open.jpg'
        cv.imwrite(name, Opening)
        # 综合
        img_robert = Image.open(name)
        dst = img_robert.resize((200, 200))
        img_GO = ImageTk.PhotoImage(dst)
        label_img = Label(f10, image=img_GO, width=200, height=200)
        label_img.place(relx=0.5, rely=0.53)
        label01 = Label(f10, text="Opening", width=10, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.6, rely=0.48)

    def GClosing(self):
        global img_GC
        kernel = np.ones([5, 5], dtype='int')
        image = cv.imread(self.file_path, cv.IMREAD_GRAYSCALE)
        Closing = GClose(image, kernel)
        name = 'images\ori_close.jpg'
        cv.imwrite(name, Closing)
        # 综合
        img_robert = Image.open(name)
        dst = img_robert.resize((200, 200))
        img_GC = ImageTk.PhotoImage(dst)
        label_img = Label(f10, image=img_GC, width=200, height=200)
        label_img.place(relx=0.5, rely=0.53)
        label01 = Label(f10, text="GClosing", width=10, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.6, rely=0.48)

    def showpicture6(self):
        global img_png_6
        self.file_path = filedialog.askopenfilename()
        img_open = Image.open(self.file_path)
        dst = img_open.resize((200, 200))
        img_png_6 = ImageTk.PhotoImage(dst)
        label_img = Label(f12, image=img_png_6, width=200, height=200)
        label_img.place(relx=0.06, rely=0.055)
        label01 = Label(f12, text="original", width=10, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.15, rely=0.01)

    def GExt_Edge(self):
        global img_GEx
        kernel = np.ones([5, 5], dtype='int')
        image = cv.imread(self.file_path, cv.IMREAD_GRAYSCALE)
        image_ext = ext_Gradient(image, kernel)
        name = 'images\Gext_edge.jpg';
        cv.imwrite(name, image_ext)
        # 综合
        img_robert = Image.open(name)
        dst = img_robert.resize((200, 200))
        img_GEx = ImageTk.PhotoImage(dst)
        label_img = Label(f12, image=img_GEx, width=200, height=200)
        label_img.place(relx=0.5, rely=0.055)
        label01 = Label(f12, text="GExt_Edge", width=10, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.6, rely=0.01)

    def GInt_Edge(self):
        global img_GIn
        kernel = np.ones([5, 5], dtype='int')
        image = cv.imread(self.file_path, cv.IMREAD_GRAYSCALE)
        image_In = int_Gradient(image, kernel)
        name = 'images\Gint_edge.jpg'
        cv.imwrite(name, image_In)
        # 综合
        img_robert = Image.open(name)
        dst = img_robert.resize((200, 200))
        img_GIn = ImageTk.PhotoImage(dst)
        label_img = Label(f12, image=img_GIn, width=200, height=200)
        label_img.place(relx=0.06, rely=0.53)
        label01 = Label(f12, text="Gint_edge", width=10, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.15, rely=0.48)

    def GStad_Edge(self):
        global img_Gst
        kernel = np.ones([5, 5], dtype='int')
        image = cv.imread(self.file_path, cv.IMREAD_GRAYSCALE)
        image_st = stad_Gradient(image, kernel)
        name = 'images\int_edge.jpg'
        cv.imwrite(name, image_st)
        # 综合
        img_robert = Image.open(name)
        dst = img_robert.resize((200, 200))
        img_Gst = ImageTk.PhotoImage(dst)
        label_img = Label(f12, image=img_Gst, width=200, height=200)
        label_img.place(relx=0.5, rely=0.53)
        label01 = Label(f12, text="Gstad_edge", width=10, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.6, rely=0.48)

    def GOBR(self):
        global img_GOBR
        kernel = np.ones([5, 5], dtype='int')
        image = cv.imread(self.file_path, cv.IMREAD_GRAYSCALE)
        erode = OBR(image)
        name = 'images\ori_obr.jpg'
        cv.imwrite(name, erode)
        # 综合
        img_robert = Image.open(name)
        dst = img_robert.resize((200, 200))
        img_GOBR = ImageTk.PhotoImage(dst)
        label_img = Label(f12, image=img_GOBR, width=200, height=200)
        label_img.place(relx=0.5, rely=0.055)
        label01 = Label(f12, text="GOBR", width=10, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.6, rely=0.01)

    def GCBR(self):
        global img_GCBR
        kernel = np.ones([5, 5], dtype='int')
        image = cv.imread(self.file_path, cv.IMREAD_GRAYSCALE)
        image_In = CBR(image)
        name = 'images\Gint_edge.jpg'
        cv.imwrite(name, image_In)
        # 综合
        img_robert = Image.open(name)
        dst = img_robert.resize((200, 200))
        img_GCBR = ImageTk.PhotoImage(dst)
        label_img = Label(f12, image=img_GCBR, width=200, height=200)
        label_img.place(relx=0.06, rely=0.53)
        label01 = Label(f12, text="GCBR", width=10, height=1,
                        bg="white", fg="black")
        label01.place(relx=0.15, rely=0.48)


if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()