"""
1. Download the covid csv file and find out the shape 
and the number of dimension of that file.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def find_shape_and_dimension(filename):
    df = pd.read_csv(filepath_or_buffer=filename, sep=',', skiprows=2)
    print(df.shape)
    print(df.ndim)


"""
2. The previous covid csv you downloaded, print the output
for the amount of new cases for each month
"""

def print_new_cases_by_month(filename):
    df = pd.read_csv(filepath_or_buffer=filename, sep=',', skiprows=2)
    # group by first three characters of date
    df.groupby(df['Date'].str[:3]).sum()['New Cases']
"""
3. Plot that data in a pie graph showing the Percentages.
"""

def plot_pie_chart(filename):
    df = pd.read_csv(filepath_or_buffer=filename, sep=',', skiprows=2)
    # Mar 3 2020
    df.groupby(df['Date'].str[:3]).sum()['New Cases'].plot(kind='pie', autopct='%1.1f%%')
    plt.show()

"""
4.  Find the percentile for all the new cases.
"""

def find_percentile(filename):
    df = pd.read_csv(filepath_or_buffer=filename, sep=',', skiprows=2)
    pc = df.groupby(df['Date'].str[:3]).sum()['New Cases'].describe()['50%']
    print(pc)

def main():
    filename = 'covid_data_us.csv'
    find_shape_and_dimension(filename)
    print_new_cases_by_month(filename)
    plot_pie_chart(filename)
    find_percentile(filename)


if __name__ == '__main__':
    main()
