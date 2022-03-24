import cv2
import numpy as np
import pandas as pd

"""
1. Download a picture image and make that image smaller 
than the original size.
The image also have to be grey scale.
"""

def download_and_resize_image(image_path, width, height):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (width, height))
    # change the color to grey scale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img


"""
2. Create a data frame by downloading a csv file and add a new column to your dataFrame.
"""

def create_data_frame(csv_path):
    df = pd.read_csv(csv_path)
    # add a new column to your dataFrame
    df = df.assign(half_sepal_length=lambda x: x['sepal_length']/2)
    return df

"""
3. In your dataframe i want to know the total average of 3 columns.
"""

def get_average_of_columns(df, columns):
    return df[columns].mean()


"""
4. The picture image you downloaded i want you to slice through the second column.
"""

def slice_image(img, column):
    return img[:, column]


def main():
    # 1. Download a picture image and make that image smaller
    image_path = "kallyas.jpg"
    img = download_and_resize_image(image_path, 250, 250)
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 2. Create a data frame by downloading a csv file and add a new column to your dataFrame
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    df = create_data_frame(csv_path=url)
    print(df.head())

    # 3. In your dataframe i want to know the total average of 3 columns.
    columns = ['sepal_length', 'sepal_width', 'petal_length']
    print(get_average_of_columns(df, columns))

    # 4. The picture image you downloaded i want you to slice through the second column.
    sliced_img = slice_image(img, 1)
    cv2.imshow("sliced image", sliced_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
