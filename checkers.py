import cv2
import numpy
import mediapipe

colorBlack = (0, 0, 0)
colorWhite = (255, 255, 255)
colorLightBrown = (140, 140, 140)
colorDarkBrown = (200, 200, 200)
thickness = 1
img = numpy.zeros((512, 512))
pos52_0 = [52, 0]
pos52_52 = [52, 52]

def DrawPlace():
    for i in range(0, 512, 52):
        cv2.rectangle(img, pos52_0, pos52_52, colorLightBrown, thickness)
        pos52_52[0] = pos52_52[0] + 52
DrawPlace()
while True:
    cv2.imshow('Checkers', img)
    DrawPlace()
    # cv2.rectangle(img, (0, 0), (52, 52), colorLightBrown, thickness)
    # cv2.rectangle(img, (52, 0), (104, 52), colorLightBrown, thickness)
    # cv2.rectangle(img, (52, 0), (156, 52), colorLightBrown, thickness)
    # cv2.rectangle(img, (52, 0), (156, 52), colorLightBrown, thickness)
    # cv2.rectangle(img, (52, 0), (208, 52), colorLightBrown, thickness)
    if cv2.waitKey(1) == ord('q'):
        break