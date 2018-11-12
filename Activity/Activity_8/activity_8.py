
import cv2
import numpy as np

class Activity8:

    def __init__(self):
        self.color = (255, 255, 255)
        self.green = (0, 255, 0)
        self.ey = 155
        self.ex = 145
        self.dy = 300
        self.dx = 0
        self.cx = 300
        self.cy = 0
        self.rad = 10
        self.screen = np.zeros((300, 300, 3), dtype="uint8")
        #self.multiLine()
        #self.multiCircle()
        #self.multiRect()
        #self.xo()
        self.weirdLines()

    def multiLine(self):
        while self.dx < 300:
            cv2.line(self.screen, (self.dx, 0), (300, self.dy), self.color, 3)
            self.dx += 10
            self.dy -= 10
        while self.cy < 300:
            cv2.line(self.screen, (0, self.cy), (self.cx, 300), self.color, 3)
            self.cy += 10
            self.cx -= 10
        cv2.imshow('Lines', self.screen)
        cv2.waitKey(0)

    def multiCircle(self):
        while self.rad < 150:
            cv2.circle(self.screen, (150, 150), self.rad, self.color, 5)
            self.rad += 10
        cv2.imshow('Circles', self.screen)
        cv2.waitKey(0)

    def multiRect(self):
        while self.ex > 0:
            cv2.rectangle(self.screen, (self.ex, self.ex), (self.ey, self.ey), self.color, 3)
            self.ex -= 10
            self.ey += 10
        cv2.imshow('Rectangles', self.screen)
        cv2.waitKey(0)

    def xo(self):
        cv2.line(self.screen, (100, 0), (100, 300), self.color, 3)
        cv2.line(self.screen, (200, 0), (200, 300), self.color, 3)
        cv2.line(self.screen, (0, 100), (300, 100), self.color, 3)
        cv2.line(self.screen, (0, 200), (300, 200), self.color, 3)
        cv2.circle(self.screen, (50, 50), 45, self.color, 3)
        cv2.line(self.screen, (110, 10), (190, 90), self.color, 3)
        cv2.line(self.screen, (190, 10), (110, 90), self.color, 3)
        cv2.circle(self.screen, (250, 50), 45, self.color, 3)
        cv2.line(self.screen, (10, 110), (90, 190), self.color, 3)
        cv2.line(self.screen, (90, 110), (10, 190), self.color, 3)
        cv2.circle(self.screen, (150, 150), 45, self.color, 3)
        cv2.line(self.screen, (210, 110), (290, 190), self.color, 3)
        cv2.line(self.screen, (290, 110), (210, 190), self.color, 3)
        cv2.circle(self.screen, (50, 250), 45, self.color, 3)
        cv2.line(self.screen, (110, 210), (190, 290), self.color, 3)
        cv2.line(self.screen, (190, 210), (110, 290), self.color, 3)
        cv2.circle(self.screen, (250, 250), 45, self.color, 3)
        cv2.imshow('XO', self.screen)
        cv2.waitKey(0)

    def weirdLines(self):
        x = 0
        y = 0
        dx = 300
        dy = 300
        while x < 300:
            cv2.line(self.screen, (x, y), (dx, dy), self.green, 1)
            cv2.line(self.screen, (dx, y), (x, dy), self.green, 1)
            cv2.line(self.screen, (y, dx), (dy, x), self.green, 1)
            cv2.line(self.screen, (y, x), (dy, dx), self.green, 1)
            y += 10
            dy -= 10
            x += 10
        while dx > 0:
            cv2.line(self.screen, (x, y), (dx, dy), self.green, 1)
            cv2.line(self.screen, (dx, y), (x, dy), self.green, 1)
            cv2.line(self.screen, (y, dx), (dy, x), self.green, 1)
            cv2.line(self.screen, (y, x), (dy, dx), self.green, 1)
            dx -= 10
            dy -= 10
            x += 10

        cv2.imshow('Weird Lines', self.screen)
        cv2.waitKey(0)
