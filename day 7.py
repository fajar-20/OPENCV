import cv2
import numpy as np

img = cv2.imread("Latihan day 1 - day 30/Resources/foto2.jpg")
if img is None:
    print("Error: Gambar tidak ditemukan")
    exit()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 1)

# Bisa pakai Threshold
th = cv2.adaptiveThreshold(
    blur, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY_INV,
    11, 2
)

# Atau Canny
# edges = cv2.Canny(blur, 100, 200)

contours, hierarchy = cv2.findContours(
    th,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

cv2.drawContours(img, contours, -1, (0,255,0), 2)

cv2.imshow("Threshold", th)
cv2.imshow("Contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
