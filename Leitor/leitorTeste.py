import cv2

video = cv2.VideoCapture()
ip = 'https://192.168.1.7:8080/video'

video.open(ip)

while True:
    check, img = video.read()
    print(type(img))
    cv2.imshow('img', img)
    cv2.waitKey(1)
    