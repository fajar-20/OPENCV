import cv2
import numpy as np

# =============================
# CAMERA
# =============================
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# =============================
# HSV COLOR RANGE
# =============================

# RED (2 range karena HSV muter)
lower_red1 = np.array([0,120,70])
upper_red1 = np.array([10,255,255])
lower_red2 = np.array([170,120,70])
upper_red2 = np.array([180,255,255])

# YELLOW
lower_yellow = np.array([15,100,100])
upper_yellow = np.array([35,255,255])

# GREEN
lower_green = np.array([36,50,70])
upper_green = np.array([89,255,255])

# =============================
# FUNCTION DETECT COLOR
# =============================
def detect_color(mask, label, draw_color, frame):
    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 800:  # filter noise
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x+w, y+h), draw_color, 2)
            return label, draw_color

    return None, None

# =============================
# MAIN LOOP
# =============================
while True:
    success, frame = cap.read()
    if not success:
        print("Kamera tidak terbaca")
        break

    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # =============================
    # MASKING
    # =============================
    mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask_red = cv2.bitwise_or(mask_red1, mask_red2)

    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
    mask_green  = cv2.inRange(hsv, lower_green, upper_green)

    # =============================
    # MORPHOLOGY (NOISE CLEAN)
    # =============================
    kernel = np.ones((5,5), np.uint8)
    mask_red = cv2.morphologyEx(mask_red, cv2.MORPH_OPEN, kernel)
    mask_yellow = cv2.morphologyEx(mask_yellow, cv2.MORPH_OPEN, kernel)
    mask_green = cv2.morphologyEx(mask_green, cv2.MORPH_OPEN, kernel)

    status = "NONE"
    color = (255,255,255)

    # =============================
    # DETECTION PRIORITY
    # =============================
    for result in [
        detect_color(mask_red, "STOP", (0,0,255), frame),
        detect_color(mask_yellow, "READY", (0,255,255), frame),
        detect_color(mask_green, "GO", (0,255,0), frame)
    ]:
        if result[0] is not None:
            status, color = result
            break

    # =============================
    # DISPLAY TEXT
    # =============================
    cv2.putText(
        frame,
        f"STATUS: {status}",
        (30, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.2,
        color,
        3
    )

    cv2.imshow("Day 9 - Traffic Light Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
