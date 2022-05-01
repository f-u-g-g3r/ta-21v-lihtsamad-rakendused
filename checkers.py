import cv2
import numpy
import mediapipe

colorBlack = (0, 0, 0)
colorWhite = (255, 255, 255)
colorLightBrown = (140, 140, 140)
colorDarkBrown = (200, 200, 200)
thickness = 1
img = numpy.zeros((512, 512))
posZeroZero = (0, 0)

while True:
    cv2.imshow('Checkers', img)
    cv2.rectangle(img, (0, 0), (52, 52), colorLightBrown, thickness)
    cv2.rectangle(img, (52, 0), (104, 52), colorLightBrown, thickness)
    if cv2.waitKey(1) == ord('q'):
        break