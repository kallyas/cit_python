import cv2

cap = cv2.VideoCapture(0)


def press_P_to_capture_pic_and_save():
    if cv2.waitKey(1) & 0xFF == ord('p'):
        cv2.imwrite('capture.jpg', frame)

def img_to_gray_scale():
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return gray




while True:
    ret, frame = cap.read()
    # img = img_to_gray_scale()
    cv2.imshow('Black and White', frame)
    press_P_to_capture_pic_and_save()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()