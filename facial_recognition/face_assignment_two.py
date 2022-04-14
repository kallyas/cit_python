import cv2
import matplotlib.pyplot as plt
import pandas as pd
import requests

"""
1. .Download a image and only detect the eyes in the image.
"""


def detect_only_eyes():
    img_url = 'many-faces.jpg'
    img = cv2.imread(img_url)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        eyes = eyes_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


detect_only_eyes()


"""
2. .Download the bitcoin csv and only print out the Opening and Closing price.
Then display it in a graph.
"""

def bitcoin_opening_closing():
    bitcoin_csv_close = 'https://api.coindesk.com/v1/bpi/historical/close.csv'
    bitcoin_csv_open = 'https://api.coindesk.com/v1/bpi/historical/open.csv'
    open_df = pd.read_csv(bitcoin_csv_open)
    close_df = pd.read_csv(bitcoin_csv_close)
    # remove last two rows from each dataframe
    open_df = open_df.iloc[:-2]
    close_df = close_df.iloc[:-2]
    print(open_df)
    print(close_df)
    open_df.plot(x='Date', y='Close')
    close_df.plot(x='Date', y='Close')
    plt.show()


bitcoin_opening_closing()