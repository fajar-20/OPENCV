

import cv2
import numpy as np

import cv2
import numpy as np

def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list) or isinstance(imgArray[0], tuple)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]

    if rowsAvailable:
        for x in range(rows):
            for y in range(cols):
                img = imgArray[x][y]
                if img is None:
                    img = np.zeros((height, width, 3), np.uint8)
                if img.shape[:2] == (height, width):
                    imgArray[x][y] = cv2.resize(img, (0, 0), fx=scale, fy=scale)
                else:
                    resized = cv2.resize(img, (width, height))
                    imgArray[x][y] = cv2.resize(resized, (0, 0), fx=scale, fy=scale)
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)

        hor = []
        for x in range(rows):
            hor.append(np.hstack(imgArray[x]))
        ver = np.vstack(hor)
    else:
        for x in range(rows):
            img = imgArray[x]
            if img is None:
                img = np.zeros((height, width, 3), np.uint8)
            if img.shape[:2] == (height, width):
                imgArray[x] = cv2.resize(img, (0, 0), fx=scale, fy=scale)
            else:
                resized = cv2.resize(img, (width, height))
                imgArray[x] = cv2.resize(resized, (0, 0), fx=scale, fy=scale)
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor

    return ver

img = cv2.imread("Latihan day 1 - day 30/Resources/SHAPES.jpg")
if img is None:
    print("Error: Gambar tidak ditemukan")
    exit()

imgResize = cv2.resize(img, (650, 500))
imgContour = imgResize.copy()
gray = cv2.cvtColor(imgResize, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 1)

# th = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

canny = cv2.Canny(blur, 50,100)

kernel = np.ones((2,2), np.uint8)
dilation = cv2.dilate(canny, kernel, iterations=2)
eroded = cv2.erode(dilation,kernel,iterations=1)

def getContours(img, imgContour, minArea=500):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > minArea:
            cv2.drawContours(imgContour, cnt, -1, (255,0,0),2)

        
            peri = cv2.arcLength(cnt, True) # digunakan untuk menghitung keliling
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True) # digunkan untuk menyederhanakan contour
            objCor = len(approx) # hitung sudut pada objek
            x,y,w,h = cv2.boundingRect(cnt)

            shape = "None"
            if objCor == 3:
                shape = "Triangle"
            elif objCor == 4:
                aspRatio = w / float(h)
                shape = "Square" if 0.95 < aspRatio < 1.05 else "Rectangle"
            elif objCor == 5:
                shape = "Pentagon"
            elif objCor == 10:
                shape = "Stars"
            else:
                shape = "Circle"

            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgContour, shape, (x+20, y+50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        (255,0,0), 2)
            cv2.putText(imgContour, f"{int(area)}", (x, y + h + 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
            

getContours(eroded, imgContour)

imgBlank = np.zeros_like(img)
imgStack = stackImages(0.8,([imgResize,dilation,imgContour],[blur,gray,imgBlank]))


cv2.imshow("Result", imgStack)

cv2.waitKey(0)