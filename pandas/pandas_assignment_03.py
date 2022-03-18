from calendar import c
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


"""
1. Download any data csv and find out the total average for 3 columns.
"""

def read_csv_file(file_name):
    """
    Read csv file.
    """
    # Read csv file, limit to first 1000 rows.
    data = pd.read_csv(file_name, nrows=1000)
    return data

def total_average(data, columns):
    """
    Calculate the total average for 3 columns.
    """
    total_average = data[columns].mean()
    return total_average


"""
2.  Inside your new csv you downloaded, remove 1 column out of your 
data frame.
"""

def remove_column(data, column):
    """
    Remove column from data frame.
    """
    data = data.drop(column, axis=1)
    return data


"""
3. Use a scatter plot with different colors to display your data.
"""

def scatter_plot(data, x_axis, y_axis):
    """
    Scatter plot.
    """
    colors = np.random.rand(len(data))
    data.plot.scatter(x=x_axis, y=y_axis, s=len(data)*0.05, c=colors, alpha=0.5)
    # plt.colorbar()
    plt.show()


def main():
    """
    Main function.
    """
    file_name = 'charts.csv'
    data = read_csv_file(file_name)
    columns = ['last-week', 'peak-rank', 'weeks-on-board']
    total_avg = total_average(data, columns)
    print(total_avg)
    remove_column(data, 'rank')
    scatter_plot(data, 'last-week', 'peak-rank')


if __name__ == '__main__':
    main()
