"""
1. Create a dictionary called test scores, 
the keys is the name and values is there grades for 3
classes. Turn that dictionary to a pandas Series.
"""

def create_dictionary(keys, values):
    """
    Create a dictionary with keys and values.
    """
    return dict(zip(keys, values))

def dict_to_panda_series(dictionary, pd):
    """
    Convert a dictionary to a pandas Series.
    """
    return pd.Series(dictionary)

"""
2. Download any data online and transform that csv file from rows to columnns.
"""

def download_and_transform_csv(url, pd):
    """
    Download any data online and transform that csv file from rows to columnns.
    """
    df = pd.read_csv(url)
    return df.transpose()


"""
3. Download a picture and find out the shape of that picture.
"""

def download_and_find_shape(url, cv):
    """
    Download a picture and find out the shape of that picture.
    """
    img = cv.imread(url)
    return img.shape



def main():
    import pandas as pd
    import cv2

    # 1. Create a dictionary called test scores,
    # the keys is the name and values is there grades for 3
    # classes. Turn that dictionary to a pandas Series.
    keys = ['Math', 'English', 'Science']
    values = [90, 80, 70], [80, 70, 60], [70, 60, 50]
    test_scores = create_dictionary(keys, values)
    test_scores_series = dict_to_panda_series(test_scores, pd)
    print(test_scores_series)

    # 2. Download any data online and transform that csv file from rows to columnns.
    url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
    df = download_and_transform_csv(url, pd)
    print(df)

    # 3. Download a picture and find out the shape of that picture.
    img_url = 'kallyas.jpg'
    img_shape = download_and_find_shape(img_url, cv2)
    print(img_shape)


if __name__ == '__main__':
    main()