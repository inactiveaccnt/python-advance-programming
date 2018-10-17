from Image import asset_collector
from matplotlib import pyplot
import numpy as np
import cv2

class ImageCV:
    def __init__(self):
        #self.openImage()
        #self.plotImage()
        #self.drawShape()
        self.drawing = False
        self.mode = True
        self.ix, self.iy = -1, -1
        self.paintShape()

    def openImage(self):
        img = cv2.imread(asset_collector.IMG['two'],0)
        cv2.imshow('Test Tutorial', img)
        cv2.imwrite('Image/grayimage.png', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def plotImage(self):
        img = cv2.imread(asset_collector.IMG['two'], 0)
        pyplot.imshow(img,'gray')
        pyplot.xticks([]), pyplot.yticks([])
        pyplot.show()

    def drawShape(self):
        img = np.zeros((512, 512, 3), np.uint8)
        img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
        img = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
        img = cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)
        img = cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)
        pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
        pts = pts.reshape(-1, 1, 2)
        img = cv2.polylines(img, [pts], True, (255, 255, 255))
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('Drawing Image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def drawCircle(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.drawing = True
            self.ix, self.iy = x, y
        elif event == cv2.EVENT_MOUSEMOVE:
            if self.drawing == True:
                if self.mode == True:
                    cv2.rectangle(self.img, (self.ix, self.iy), (x, y), (0, 255, 0), -1)
                else:
                    cv2.circle(self.img, (x, y), 5, (0, 0, 255), -1)
        elif event == cv2.EVENT_LBUTTONUP:
            self.drawing = False
            if self.mode == True:
                cv2.rectangle(self.img, (self.ix, self.iy), (x, y), (0, 255, 0), -1)
            else:
                cv2.circle(self.img, (x, y), 5, (0, 0, 255), -1)

    def paintShape(self):
        self.img = np.zeros((512, 512, 3), np.uint8)
        cv2.namedWindow('image')
        cv2.setMouseCallback('image', self.drawCircle)
        while(1):
            cv2.imshow('image', self.img)
            k = cv2.waitKey(1) & 0xFF
            if k == ord('m'):
                self.mode = False
            elif k == 27:
                break
        cv2.destroyAllWindows()
