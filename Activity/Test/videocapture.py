import cv2
import numpy as np

class VideoCap:

    def __init__(self):
        #self.cap = cv2.VideoCapture(0)
        #self.cap = cv2.VideoCapture('Video/output.avi')
        #self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        #self.out = cv2.VideoWriter('Video/output.avi', self.fourcc, 20.0, (640, 480))
        #self.frameMaskRes()
        #self.captureVideo()
        #self.playVideo()
        pass

    def frameMaskRes(self):
        while(1):
            ret, frame = self.cap.read()
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            lower_blue = np.array([100, 50, 50])
            upper_blue = np.array([130, 255, 255])
            mask = cv2.inRange(hsv, lower_blue, upper_blue)
            res = cv2.bitwise_and(frame, frame, mask=mask)
            cv2.imshow('frame', frame)
            cv2.imshow('mask', mask)
            cv2.imshow('res', res)
            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                break
        cv2.destroyAllWindows()

    def captureVideo(self):
        while(self.cap.isOpened()):
            ret, frame = self.cap.read()
            if ret == True:
                frame = cv2.flip(frame, 0)
                self.out.write(frame)
                cv2.imshow('frame', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
        self.cap.release()
        self.out.release()
        cv2.destroyAllWindows()

    def playVideo(self):
        while(self.cap.isOpened()):
            ret, frame = self.cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame', gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.cap.release()
        cv2.destroyAllWindows()
