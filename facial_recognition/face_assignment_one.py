import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
import imutils
from typing import Any, Dict, List
from datetime import datetime

"""
1. Download the CSV file for the current price for Ethereum and Ethereum Classic.
Display the data in 2 different graphs in 1 figure (hint: use subplot).
"""


def scrap_data_ethereum() -> Dict[str, Any]:
    """
    Scrapes historical data for Ethereum from CoinMarketCap API.

    Returns:
        dict: JSON data containing historical prices for Ethereum.
    """
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


def scrape_data_ethereum_classic() -> Dict[str, Any]:
    """
    Scrapes historical data for Ethereum Classic from CoinMarketCap API.

    Returns:
        dict: JSON data containing historical prices for Ethereum Classic.
    """
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


def plot_graph() -> None:
    """
    Plots the historical prices for Ethereum and Ethereum Classic in subplots.
    """
    ethereum_data = scrap_data_ethereum()['data']['quotes']
    ethereum_classic_data = scrape_data_ethereum_classic()['data']['quotes']
    
    eth_close = [et['quote']['close'] for et in ethereum_data]
    eth_open = [et['quote']['open'] for et in ethereum_data]
    eth_high = [et['quote']['high'] for et in ethereum_data]
    eth_low = [et['quote']['low'] for et in ethereum_data]
    eth_date = [et['quote']['timestamp'] for et in ethereum_data]

    eth_close_classic = [et['quote']['close'] for et in ethereum_classic_data]
    eth_open_classic = [et['quote']['open'] for et in ethereum_classic_data]
    eth_high_classic = [et['quote']['high'] for et in ethereum_classic_data]
    eth_low_classic = [et['quote']['low'] for et in ethereum_classic_data]
    eth_date_classic = [et['quote']['timestamp'] for et in ethereum_classic_data]

    df_ethereum = pd.DataFrame({
        'close': eth_close,
        'open': eth_open,
        'high': eth_high,
        'low': eth_low,
        'date': eth_date
    })
    df_ethereum_classic = pd.DataFrame({
        'close': eth_close_classic,
        'open': eth_open_classic,
        'high': eth_high_classic,
        'low': eth_low_classic,
        'date': eth_date_classic
    })

    fig, ax = plt.subplots(2, 1, figsize=(12, 8))
    df_ethereum.plot(ax=ax[0], x='date', title='Ethereum')
    df_ethereum_classic.plot(ax=ax[1], x='date', title='Ethereum Classic')
    plt.tight_layout()
    plt.show()


plot_graph()


"""
2. Create a face recognition, detecting faces in an image.
"""


def detect_many_faces(image_path: str = 'business-people.jpg') -> None:
    """
    Detects faces in the given image and displays the result.

    Args:
        image_path (str): The path to the image file.
    """
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found at {image_path}")
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    if face_cascade.empty():
        raise RuntimeError("Error loading face cascade")
    
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    cv2.imshow('Detected Faces', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


detect_many_faces()


"""
3. Create a body recognition, detecting body in an image (hint: use haarcascade_body_default.xml).
"""


def body_recognition(image_path: str = 'many-people.jpg') -> None:
    """
    Detects bodies in the given image and displays the result.

    Args:
        image_path (str): The path to the image file.
    """
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found at {image_path}")
    
    resized_image = imutils.resize(image, width=min(400, image.shape[1]))
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    (rects, weights) = hog.detectMultiScale(resized_image, winStride=(4, 4), padding=(8, 8), scale=1.05)
    
    for (x, y, w, h) in rects:
        cv2.rectangle(resized_image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    
    cv2.imshow("Detecting People", resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


body_recognition()
