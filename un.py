import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
import time
import mediapipe as mp
#keypoint using MP Hoslistic
cap =cv2.VideoCapture(0)
while cap.isOpened():
    ret,frame=cap.read()
    cv2.imshow('OpenCV',frame)
    if cv2.waitkey(10)&0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllwindows()