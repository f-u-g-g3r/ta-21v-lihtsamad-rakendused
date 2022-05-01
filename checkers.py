import cv2
import numpy
import mediapipe

colorBlack = (0, 0, 0)
colorWhite = (255, 255, 255)
colorLightBrown = (134, 175, 206)
colorDarkBrown = (33, 104, 159)
thickness = -1
img = numpy.zeros((420, 420, 3), numpy.uint8)

def drawGame():

    pos1 = [50, 0]
    pos2 = [0, 50]
    n = 0

    while n != 4:
        cv2.rectangle(img, pos1, pos2, colorLightBrown, thickness)
        pos1[0] = pos1[0] + 102
        pos2[0] = pos2[0] + 102
        n += 1

    pos1 = [50, 100]
    pos2 = [100, 50]
    n = 0
    
    while n != 4:
        cv2.rectangle(img, pos1, pos2, colorLightBrown, thickness)
        pos1[0] = pos1[0] + 102
        pos2[0] = pos2[0] + 102
        n += 1

    pos1 = [50, 150]
    pos2 = [0, 100]
    n = 0
    
    while n != 4:
        cv2.rectangle(img, pos1, pos2, colorLightBrown, thickness)
        pos1[0] = pos1[0] + 102
        pos2[0] = pos2[0] + 102
        n += 1
    
    pos1 = [50, 200]
    pos2 = [100, 150]
    n = 0
    
    while n != 4:
        cv2.rectangle(img, pos1, pos2, colorLightBrown, thickness)
        pos1[0] = pos1[0] + 102
        pos2[0] = pos2[0] + 102
        n += 1
    
    pos1 = [50, 250]
    pos2 = [0, 200]
    n = 0
    
    while n != 4:
        cv2.rectangle(img, pos1, pos2, colorLightBrown, thickness)
        pos1[0] = pos1[0] + 102
        pos2[0] = pos2[0] + 102
        n += 1

    pos1 = [50, 300]
    pos2 = [100, 250]
    n = 0
    
    while n != 4:
        cv2.rectangle(img, pos1, pos2, colorLightBrown, thickness)
        pos1[0] = pos1[0] + 102
        pos2[0] = pos2[0] + 102
        n += 1

    pos1 = [50, 350]
    pos2 = [0, 300]
    n = 0
    
    while n != 4:
        cv2.rectangle(img, pos1, pos2, colorLightBrown, thickness)
        pos1[0] = pos1[0] + 102
        pos2[0] = pos2[0] + 102
        n += 1

    pos1 = [50, 400]
    pos2 = [100, 350]
    n = 0
    
    while n != 4:
        cv2.rectangle(img, pos1, pos2, colorLightBrown, thickness)
        pos1[0] = pos1[0] + 102
        pos2[0] = pos2[0] + 102
        n += 1

    pos1 = [50, 450]
    pos2 = [0, 400]
    n = 0
    

    

def drawFigures():
    pos1 = []
    pos2 = []
    cv2.circle(img, pos1, pos2, colorBlack, thickness) 
#def play():


while True:
    drawGame()
    cv2.imshow('Checkers', img)
    int(input("123:"))
    if cv2.waitKey(1) == ord('q'):
        break