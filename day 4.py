import cv2
import numpy as np

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

img = cv2.imread("Latihan day 1 - day 30/Resources/foto3.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv  = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Tentukan skala yang sama dengan yang ada di stackImages
        scale = 0.8
        
        # 1. Kembalikan koordinat ke ukuran asli
        real_y = int(y / scale)
        real_x_full = int(x / scale)
        
        # 2. Karena gambar disusun menyamping (horizontal), 
        # kita ambil sisa bagi dengan lebar gambar asli agar koordinat x tetap sinkron
        width_original = img.shape[1]
        local_x = real_x_full % width_original
        
        # Pastikan tidak error jika klik melebihi batas gambar
        if real_y < img.shape[0]:
            print(f"Koordinat Asli: x={local_x}, y={real_y}")
            print("BGR :", img[real_y, local_x])
            print("HSV :", hsv[real_y, local_x])
            print("GRAY:", gray[real_y, local_x])
            print("-" * 30)

imgStack = stackImages(0.8,([img,gray,hsv])) 
cv2.imshow("Stacked Images", imgStack)

cv2.setMouseCallback("Stacked Images", mouse_event)

cv2.waitKey(0)
cv2.destroyAllWindows()