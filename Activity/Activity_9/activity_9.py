import numpy as np
import cv2

class Activity9:

    def __init__(self):
        self.red = (0, 0, 255)
        self.green = (0, 255, 0)
        self.blue = (255, 0, 0)
        self.white = (255, 255, 255)
        self.color = (255, 255, 255)
        self.bg = (50, 50, 50)
        self.screen = np.zeros((500, 500, 3), dtype="uint8")
        #self.actitvit9_1()
        self.activity_9_2()

    def actitvit9_1(self):
        #cv2.rectangle(self.screen, (0, 0), (500, 500), self.bg, -1)
        #top-left circles
        cv2.circle(self.screen, (0, 0), 70, self.blue, -1)
        cv2.circle(self.screen, (0, 0), 50, self.green, -1)
        cv2.circle(self.screen, (0, 0), 30, self.red, -1)

        #top-right circles
        cv2.circle(self.screen, (500, 0), 70, self.blue, -1)
        cv2.circle(self.screen, (500, 0), 50, self.green, -1)
        cv2.circle(self.screen, (500, 0), 30, self.red, -1)

        #bottom-left circles
        cv2.circle(self.screen, (0, 500), 70, self.blue, -1)
        cv2.circle(self.screen, (0, 500), 50, self.green, -1)
        cv2.circle(self.screen, (0, 500), 30, self.red, -1)

        #bottom-right circles
        cv2.circle(self.screen, (500, 500), 70, self.blue, -1)
        cv2.circle(self.screen, (500, 500), 50, self.green, -1)
        cv2.circle(self.screen, (500, 500), 30, self.red, -1)

        #python
        cv2.line(self.screen, (50, 100), (50, 190), self.color, 3)
        cv2.rectangle(self.screen, (50, 100), (100, 150), self.color, 3)
        cv2.line(self.screen, (110, 100), (140, 140), self.color, 3)
        cv2.line(self.screen, (140, 140), (170, 100), self.color, 3)
        cv2.line(self.screen, (140, 140), (140, 190), self.color, 3)
        cv2.line(self.screen, (180, 100), (240, 100), self.color, 3)
        cv2.line(self.screen, (210, 100), (210, 190), self.color, 3)
        cv2.line(self.screen, (250, 100), (250, 190), self.color, 3)
        cv2.line(self.screen, (300, 100), (300, 190), self.color, 3)
        cv2.line(self.screen, (250, 140), (300, 140), self.color, 3)
        cv2.circle(self.screen, (350, 140), 40, self.color, 3)
        cv2.line(self.screen, (400, 100), (400, 190), self.color, 3)
        cv2.line(self.screen, (450, 100), (450, 190), self.color, 3)
        cv2.line(self.screen, (400, 100), (450, 190), self.color, 3)

        #red rectangle
        cv2.rectangle(self.screen, (100, 300), (150, 350), self.red, -1)

        #green rectangle
        cv2.rectangle(self.screen, (220, 300), (270, 350), self.green, -1)

        #blue rectangle
        cv2.rectangle(self.screen, (350, 300), (400, 350), self.blue, -1)

        cv2.imshow('Activity 9', self.screen)
        cv2.waitKey(0)

    def activity_9_2(self):
        #left eye
        cv2.circle(self.screen, (150, 200), 100, self.white, -1)
        cv2.circle(self.screen, (160, 200), 80, self.red, -1)
        cv2.circle(self.screen, (170, 200), 60, self.blue, -1)
        cv2.circle(self.screen, (180, 200), 40, self.white, -1)

        #right eye
        cv2.circle(self.screen, (350, 200), 100, self.white, -1)
        cv2.circle(self.screen, (340, 200), 80, self.red, -1)
        cv2.circle(self.screen, (330, 200), 60, self.blue, -1)
        cv2.circle(self.screen, (320, 200), 40, self.white, -1)

        #nose
        cv2.circle(self.screen, (250, 290), 20, self.green, -1)

        #mouth
        cv2.rectangle(self.screen, (150, 330), (350, 380), self.red, -1)

        #teeth
        cv2.rectangle(self.screen, (200, 330), (230, 360), self.white, -1)
        cv2.rectangle(self.screen, (270, 330), (300, 360), self.white, -1)

        cv2.imshow('Activity 9', self.screen)
        cv2.waitKey()
