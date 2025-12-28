import cv2
import numpy as np



cap = cv2.VideoCapture(1)
cap.set(3,1280)
cap.set(4,720)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:

    success,frame = cap.read()
    if not success:
        print("Kamera tidak terbuka")
        exit()

    frame = cv2.flip(frame,1)

    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(imgGray, 1.1, 5,minSize=(30,30))

    for (x, y, w, h) in faces:
        # cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
        # cv2.putText(frame, "Wajah Blur", (x, y - 10), 
        #             cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        
        face_roi = frame[y:y+h, x:x+w]

        face_roi = cv2.GaussianBlur(face_roi, (99,99),0)

        frame[y:y+h, x:x+w] = face_roi
        

    cv2.imshow("Result", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == ord('Q') or key == 27:
        break

cap.release()
cv2.destroyAllWindows()

