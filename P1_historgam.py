import numpy as np
import cv2

def otsu_threshold(im):
    width, height = im.shape
    pixel_counts = np.zeros(256)
    for x in range(width):
        for y in range(height):
            pixel = im[x,y]
            pixel_counts[pixel] = pixel_counts[pixel] + 1
    # 得到图片的以0-255索引的像素值个数列表
    s_max = [0, 0]
    for threshold in range(256):
        # 遍历所有阈值，根据公式挑选出最好的
        # 更新
        w_0 = sum(pixel_counts[:threshold])  # 得到阈值以下像素个数
        w_1 = sum(pixel_counts[threshold:])  # 得到阈值以上像素个数

        # 得到阈值下所有像素的平均灰度
        u_0 = sum([i * pixel_counts[i] for i in range(0, threshold)]) / w_0 if w_0 > 0 else 0

        # 得到阈值上所有像素的平均灰度
        u_1 = sum([i * pixel_counts[i] for i in range(threshold, 256)]) / w_1 if w_1 > 0 else 0

        # 总平均灰度
        u = w_0 * u_0 + w_1 * u_1

        # 类间方差
        g = w_0 * (u_0 - u) * (u_0 - u) + w_1 * (u_1 - u) * (u_1 - u)

        # 类间方差等价公式
        # g = w_0 * w_1 * (u_0 * u_1) * (u_0 * u_1)

        # 取最大的
        if g > s_max[1]:
            s_max = [threshold, g]
    return s_max[0]

def segment(img):
    """
    最大熵分割
    :param img:
    :return:
    """
    def calculate_current_entropy(hist, threshold):
        data_hist = hist.copy()
        background_sum = 0.
        target_sum = 0.
        for i in range(256):
            if i < threshold:  # 累积背景
                background_sum += data_hist[i]
            else:  # 累积目标
                target_sum += data_hist[i]
        background_ent = 0.
        target_ent = 0.
        for i in range(256):
            if i < threshold:  # 计算背景熵
                if data_hist[i] == 0:
                    continue
                ratio1 = data_hist[i] / background_sum
                background_ent -= ratio1 * np.log2(ratio1)
            else:
                if data_hist[i] == 0:
                    continue
                ratio2 = data_hist[i] / target_sum
                target_ent -= ratio2 * np.log2(ratio2)
        return target_ent + background_ent

    def max_entropy_segmentation(img):
        channels = [0]
        hist_size = [256]
        prange = [0, 256]
        hist = cv2.calcHist(img, channels, None, hist_size, prange)  #画出直方图
        hist = np.reshape(hist, [-1])
        max_ent = 0.
        max_index = 0
        for i in range(256):
            cur_ent = calculate_current_entropy(hist, i)
            if cur_ent > max_ent:
                max_ent = cur_ent
                max_index = i
        ret, th = cv2.threshold(img, max_index, 255, cv2.THRESH_BINARY)
        return ret
    thesold= max_entropy_segmentation(img)
    return thesold