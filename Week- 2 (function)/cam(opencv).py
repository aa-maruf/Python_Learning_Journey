import cv2
cam = cv2.VideoCapture(1)

while True:
    _, frame = cam.read()   # first parameter is not used therefore _ is used.
    cv2.imshow('my cam', frame)
    cv2.waitkey(1)