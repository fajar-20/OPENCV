import cv2
import numpy as np

cap = cv2.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    imgContour = frame.copy()

    # Preprocessing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7,7), 1)
    edges = cv2.Canny(blur, 50, 150)

    # Contour
    contours, _ = cv2.findContours(
        edges,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # Counter
    triangle = square = rectangle = circle = 0

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 1000:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            objCor = len(approx)

            x, y, w, h = cv2.boundingRect(approx)

            if objCor == 3:
                shape = "Triangle"
                color = (0,255,0)
                triangle += 1

            elif objCor == 4:
                aspRatio = w / float(h)
                if 0.95 < aspRatio < 1.05:
                    shape = "Square"
                    color = (255,0,0)
                    square += 1
                else:
                    shape = "Rectangle"
                    color = (0,255,255)
                    rectangle += 1

            else:
                shape = "Circle"
                color = (0,0,255)
                circle += 1

            cv2.drawContours(imgContour, [approx], -1, color, 2)
            # cv2.rectangle(imgContour, (x,y), (x+w,y+h), color, 2)
            cv2.putText(imgContour, shape, (x+5, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    # Display count
    cv2.putText(imgContour, f"Triangle: {triangle}", (10,30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
    cv2.putText(imgContour, f"Square: {square}", (10,60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)
    cv2.putText(imgContour, f"Rectangle: {rectangle}", (10,90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255), 2)
    cv2.putText(imgContour, f"Circle: {circle}", (10,120),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

    cv2.imshow("Day 8 - Shape Detection Webcam", imgContour)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
