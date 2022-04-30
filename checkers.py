import cv2
import numpy as np
import mediapipe

colorBlack = (0, 0, 0)
colorWhite = (255, 255, 255)

img = np.zeros((512,512,3), np.uint8)
