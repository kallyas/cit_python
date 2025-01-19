import cv2
import matplotlib.pyplot as plt
import pandas as pd
from typing import Tuple

"""
1. Download an image and only detect the eyes in the image.
"""


def detect_only_eyes(img_path: str = 'many-faces.jpg') -> None:
    """
    Detects faces and eyes in the given image and displays the result.

    Args:
        img_path (str): The path to the image file.
    """
    img = cv2.imread(img_path)
    if img is None:
        raise FileNotFoundError(f"Image not found at {img_path}")
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eyes_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    
    if face_cascade.empty() or eyes_cascade.empty():
        raise RuntimeError("Error loading Haar cascades")

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eyes_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow('Eye Detection', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


detect_only_eyes()

"""
2. Download the bitcoin csv and only print out the Opening and Closing price.
Then display it in a graph.
"""


def bitcoin_opening_closing() -> None:
    """
    Downloads Bitcoin historical data and plots the opening and closing prices.
    """
    bitcoin_csv_close = 'https://api.coindesk.com/v1/bpi/historical/close.csv'
    bitcoin_csv_open = 'https://api.coindesk.com/v1/bpi/historical/open.csv'
    
    open_df = pd.read_csv(bitcoin_csv_open)
    close_df = pd.read_csv(bitcoin_csv_close)
    
    if open_df.empty or close_df.empty:
        raise ValueError("Error loading Bitcoin CSV data")

    # Print the data frames
    print("Opening Prices:")
    print(open_df)
    print("\nClosing Prices:")
    print(close_df)
    
    # Plot the data
    plt.figure()
    open_df.plot(x='Date', y='Open', label='Opening Price')
    close_df.plot(x='Date', y='Close', label='Closing Price')
    plt.title('Bitcoin Opening and Closing Prices')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()


bitcoin_opening_closing()
