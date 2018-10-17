#from activity import Synthesize
    
#if __name__ == "__main__":
#    Synthesize().convert(input("Enter a series of number: "))
import numpy as np
import cv2

img = cv2.imread("Noysoft-logo.jpg", 0)
cv2.imshow('image', img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destrouAllWindows()
elif k == ord('s'):
    cv2.imwrite("noysoft.png",img)
    cv2.destroyAllWindows()
