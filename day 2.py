
import cv2
import numpy as np

# Inisialisasi variabel global
x1, y1 = -1, -1
drawing = False

path = "Latihan day 1 - day 30/Resources/cctv1.jpg"
img = cv2.imread(path)

if img is None:
    print("Gambar tidak ditemukan!")
    exit()

def mouse_event(event, x, y, flags, param):
    global x1, y1, drawing, img
    
    # 1. Selalu buat copy dari gambar asli untuk tampilan sementara (hover effect)
    temp = img.copy()
    
    # Munculkan koordinat di pojok kiri atas saat mouse bergerak
    cv2.putText(temp, f"X= {x}, Y= {y}", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        x1, y1 = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            # Menggambar kotak persegi saat sedang drag (visualisasi area crop)
            cv2.rectangle(temp, (x1, y1), (x, y), (255, 0, 0), 2)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        # Hitung koordinat crop yang benar (menghindari nilai negatif)
        x_start, x_end = sorted([x1, x])
        y_start, y_end = sorted([y1, y])
        
        # Eksekusi Crop jika area valid
        if x_end - x_start > 0 and y_end - y_start > 0:
            roi = img[y_start:y_end, x_start:x_end]
            roi_resized = cv2.resize(roi,(640,520))
            cv2.imshow("Crop", roi_resized)
            # cv2.imshow("Crop", roi)
            
            print(f"\nCROP AREA SELESAI")
            print(f"Ukuran Asli: {roi.shape[1]}x{roi.shape[0]}")
            print(f"Ukuran Resize: 640x520")
            print("-" * 30)

    # Tampilkan 'temp' yang sudah berisi teks/kotak dinamis
    cv2.imshow("Result", temp)

cv2.imshow("Result", img)
cv2.setMouseCallback("Result", mouse_event)
cv2.waitKey(0)
cv2.destroyAllWindows()

