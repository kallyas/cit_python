import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
import imutils
from datetime import datetime

"""
1. .Download the csv file for the current price for etheruem and etheruem classic.
Display the data in 2 different graphs in 1 figure.hint(subplot)
"""

def scrap_data_etherium():
    api_url = 'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=1027&convertId=2781&timeStart=1644710400&timeEnd=1649808000'
    headers = {
        'Accepts': 'application/json',
        'authority': 'api.coinmarketcap.com',
        'accept-language': 'en-US,en;q=0.9',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'origin': 'https://coinmarketcap.com',
        'plataform': 'web',
        'if-modified-since': 'Wed, 13 Apr 2022 13:56:09 GMT',
        'referer': 'https://coinmarketcap.com',
        'sec-ch-ua': """"Not A;Brand";v="99", "Chromium";v="100", "Mircosoft Edge";v="100""",
        'x-request-id': 'a2589056-a96c-419c-bfaa-27a6adffe354',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-site': 'same-site',
        'sec-ua-platform': 'Windows',
    }
    response = requests.get(api_url, headers=headers)
    data = response.json()
    return data

def srcape_data_etherium_classic():
    api_url = 'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=1321&convertId=2781&timeStart=1644710400&timeEnd=1649808000'
    headers = {
        'Accepts': 'application/json',
        'authority': 'api.coinmarketcap.com',
        'accept-language': 'en-US,en;q=0.9',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'origin': 'https://coinmarketcap.com',
        'plataform': 'web',
        'if-modified-since': 'Wed, 13 Apr 2022 13:56:09 GMT',
        'referer': 'https://coinmarketcap.com',
        'sec-ch-ua': """"Not A;Brand";v="99", "Chromium";v="100", "Mircosoft Edge";v="100""",
        'x-request-id': 'a2589056-a96c-419c-bfaa-27a6adffe354',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-site': 'same-site',
        'sec-ua-platform': 'Windows',
    }
    response = requests.get(api_url, headers=headers)
    data = response.json()
    return data




def plot_graph():
    etherium = scrap_data_etherium()['data']['quotes']
    print(etherium)
    eth_close = [et['quote']['close'] for et in etherium]
    eth_open = [et['quote']['open'] for et in etherium]
    eth_high = [et['quote']['high'] for et in etherium]
    eth_low = [et['quote']['low'] for et in etherium]
    # convert the timestamp to date 
    eth_date = [et['quote']['timestamp'] for et in etherium]
    etherium_classic = srcape_data_etherium_classic()['data']['quotes']
    eth_close_classic = [et['quote']['close'] for et in etherium_classic]
    eth_open_classic = [et['quote']['open'] for et in etherium_classic]
    eth_high_classic = [et['quote']['high'] for et in etherium_classic]
    eth_low_classic = [et['quote']['low'] for et in etherium_classic]
    # format the date to D-M-Y. date is not timestamp
    eth_date_classic = [et['quote']['timestamp'] for et in etherium_classic]


    df_etherium = pd.DataFrame({
        'close': eth_close,
        'open': eth_open,
        'high': eth_high,
        'low': eth_low,
        'date': eth_date
    })
    df_etherium_classic = pd.DataFrame({
        'close': eth_close_classic,
        'open': eth_open_classic,
        'high': eth_high_classic,
        'low': eth_low_classic,
        'date': eth_date_classic
    })
    print(df_etherium_classic)
    fig, ax = plt.subplots(2, 1)
    # plot everything in the dataframe
    df_etherium.plot(ax=ax[0], x='date')
    df_etherium_classic.plot(ax=ax[1], x='date')
    ax[0].set_title('Etherium')
    ax[1].set_title('Etherium Classic')
    plt.show()

plot_graph()


"""
2. Create a face recognition, detecting faces in an image.
"""

def detect_many_faces():
    image_with_many_faces_url = 'business-people.jpg'
    image_with_many_faces = cv2.imread(image_with_many_faces_url)
    gray = cv2.cvtColor(image_with_many_faces, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(image_with_many_faces, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow('image_with_many_faces', image_with_many_faces)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


detect_many_faces()


"""
3. .Create a body recognition, detecting body in an image.hint(haarcascade_body_default.xml')
"""

def body_recognition():
    img_url = 'many-people.jpg'
    img = cv2.imread(img_url)
    image = imutils.resize(img, width=min(400, img.shape[1]))
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)
    for (x, y, w, h) in rects:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.imshow("Detecting people", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

body_recognition()