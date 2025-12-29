import cv2
import numpy as np

img = cv2.imread("Latihan day 1 - day 30/Resources/SHAPES.jpg")
if img is None:
    print("Error: Gambar tidak ditemukan")
    exit()

imgContour = img.copy()    
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 1)

th = cv2.adaptiveThreshold(
blur, 255,
cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
cv2.THRESH_BINARY_INV,
11, 2
)

kernel = np.ones((2, 2), np.uint8)
imgDial = cv2.dilate(th, kernel, iterations=1)


def getContours(img, imgContour, minArea=40):

    contours, hierarchy = cv2.findContours(
        img,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_NONE
    )
     

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > minArea:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 2)


getContours(imgDial, imgContour)


# cv2.imshow("Threshold", )
cv2.imshow("Original", img)
cv2.imshow("Result", imgContour)
cv2.imshow("thresh", imgDial)

cv2.waitKey(0)
cv2.destroyAllWindows()
