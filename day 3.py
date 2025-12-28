

# import cv2
# import numpy as np

# path = "Latihan day 1 - day 30/Resources/foto3.jpg"
# img = cv2.imread(path)

# if img is None:
#     print("Gambar tidak ditemukan di path:", {path})
#     exit()

# # 1. Deteksi Wajah
# faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# faces = faceCascade.detectMultiScale(imgGray,1.1,4)

# for (x,y,w,h) in faces:
#     cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2)

# cv2.imshow("Face Detection", img)

# # menggambar garis dan bentuk di gambar
# h, w = img.shape[:2]
# cx,cy = w//2, h//2

# # garis tengah horizontal dan vertikal
# cv2.line(img,(0,cy),(w,cy),(255,0,0),2)
# cv2.line(img,(cx,0),(cx,h),(255,0,0), 2)

# # Menggambar banyak lingkaran dengan loop
# for r in range(20,90,10):
#     cv2.circle(img,(cx,cy),r,(0,255,0),2)


# # Titik pusat lingkaran

# cv2.circle(img,(cx,cy), 10,(0,0,255),cv2.FILLED)

# # kotak di tengah
# cv2.rectangle(img,(cx-100,cy-100),(cx+100,cy+100),(0,0,255),3)

# # tulisan
# cv2.putText(img,("Day 3 - Draw"),(20,50),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,255),2)

# # fungsi mouse event
# def mouse_event(event, x,y,flags, param):
#     if event == cv2.EVENT_MOUSEMOVE:
#         temp = img.copy()
#         cv2.putText(temp, f"X= {x}, Y= {y}", (x-10, y-10), cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,255),1)
#         cv2.imshow("Result", temp)


# cv2.imshow("Result", img)

# cv2.setMouseCallback("Result", mouse_event)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2
import numpy as np

path = "Latihan day 1 - day 30/Resources/foto3.jpg"
img = cv2.imread(path)

if img is None:
    print("Gambar tidak ada di path", {path})
    exit()

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
# cv2.imshow("Face detection", img)

h,w = img.shape[:2]
cx,cy = w//2, h//2

cv2.line(img, (0,cy), (w,cy), (0,0,255),2)
cv2.line(img, (cx,0), (cx,h), (0,0,255),2)

for r in range(20,100,10):
    cv2.circle(img, (cx,cy),r, (0,255,0),3)

cv2.circle(img, (cx,cy), 10, (0,0,255),cv2.FILLED)

cv2.rectangle(img, (cx-100, cy-100), (cx+100, cy+100), (0,255,255),4)

cv2.putText(img, "Draw_day 3", (10,30), cv2.FONT_HERSHEY_SIMPLEX,0.8, (255,0,255),2)

def mouse_event (event,x,y,flags,param):
    if event == cv2.EVENT_MOUSEMOVE:
        temp = img.copy()
        cv2.putText(temp, f"X= {x}, Y= {y}", (x-10,y-10), cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,255),2)
        cv2.imshow("Result", temp)


cv2.imshow("Result", img)
cv2.setMouseCallback("Result", mouse_event)
cv2.waitKey(0)
cv2.destroyAllWindows()