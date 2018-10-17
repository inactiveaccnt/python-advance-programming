import cv2
import numpy as np
from Image import asset_collector
from matplotlib import pyplot as plt

class ImageProcess:

    def __init__(self):
        #self.testingClass()
        #self.thresholding()
        #self.morphologicalTransform()
        #self.imageGradients()
        self.cannyEdgeDetection()

    def testingClass(self):
        img = cv2.imread(asset_collector.IMG['four'], 0)
        cv2.imshow('Pixel Manipulation', img)
        #cv2.imwrite('Image/image_2.png', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def writeImage(self, file, image):
        cv2.imwrite(file, image);

    def thresholding(self):
        img = cv2.imread(asset_collector.IMG['four'], 0)
        ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        blur = cv2.GaussianBlur(img, (5, 5), 0)
        ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        images = [img, 0, th1,
                  img, 0, th2,
                  blur, 0, th3]
        titles = ['Original Noisy Image', 'Histogram', 'Global Thresholding (v=127)',
                    'Original Noisy Image', 'Histogram', 'Otsu\'s Thresholding',
                    'Gaussian Filtered Image', 'Histogram', 'Otsu\'s Thresholding']
        plt.imshow(images[6],'gray')
        plt.title(titles[6]), plt.xticks([]), plt.yticks([])
        plt.show()

    def morphologicalTransform(self):
        img = cv2.imread(asset_collector.IMG['three'], 0)
        kernel = np.ones((2, 2), np.uint8)
        erosion = cv2.erode(img, kernel, iterations = 1)
        dilation = cv2.dilate(img, kernel, iterations = 1)
        opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
        closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
        gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
        tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
        blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
        cv2.imshow('Morphological Transform', blackhat)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def imageGradients(self):
        img = cv2.imread(asset_collector.IMG['six'], 0)
        laplacian = cv2.Laplacian(img, cv2.CV_64F)
        sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize = 5)
        sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize = 5)

        sobelx8u = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize = 5)
        sobelx64f = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize = 5)
        abs_sobel64f = np.absolute(sobelx64f)
        sobel_8u = np.uint8(abs_sobel64f)

        cv2.imshow('Morphological Transform', sobel_8u)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def cannyEdgeDetection(self):
        img = cv2.imread(asset_collector.IMG['four'], 0)
        edges = cv2.Canny(img, 100, 200)
        cv2.imshow('Morphological Transform', edges)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
