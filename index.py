import cv2

# In here we are going to use the Haar Cascade Classifier to detect faces in an image.

m = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# v = cv2.VideoCapture("video.mp4")
v = cv2.VideoCapture("video.mp4")

while True:
    b,i1 = v.read()

    if b:
      
     i2 = cv2.cvtColor(i1,cv2.COLOR_BGR2GRAY)
 
    faces = m.detectMultiScale(i2,scaleFactor=1.2,minNeighbors=5)

    for(x,y,w,h) in faces:
     cv2.rectangle(i1,(x,y),(x+w,y+h),(0,0,255),2)


    cv2.imshow('Hello',i1)

    cv2.waitKey(1)
