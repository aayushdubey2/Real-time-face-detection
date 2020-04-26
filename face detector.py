import cv2
face=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
video=cv2.VideoCapture(0)

while True:
    
    check,frame=video.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=face.detectMultiScale(gray,scaleFactor=1.05, minNeighbors=5)
    for x,y,w,h in faces:
        gray=cv2.rectangle(gray,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow("frame",gray)
    key=cv2.waitKey(1)
    if key==ord('a'):
        break

video.release()
cv2.destroyAllWindows()
