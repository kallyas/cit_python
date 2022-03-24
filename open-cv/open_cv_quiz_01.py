import numpy as np
import pandas as pd
import random
import yfinance as yf
import matplotlib.pyplot as plt

"""
1. Create a list called basketball players. 
You need to calculate and output how many 
players are in the range of one standard 
deviation from the mean.
"""

def basketball_players():
    players = [random.randint(1, 100) for _ in range(100)]
    mean = np.mean(players)
    std = np.std(players)
    print(f"The mean is {mean} and the standard deviation is {std}")
    print(f"There are {len([x for x in players if x > mean - std and x < mean + std])} players in the range of one standard deviation from the mean.")


"""
2. You are given a task to find all 
of the whole numbers below 100 that 
are multiples of borh 3 and 5. 
Create an array of numbers below 100 
that are multiples of both 3 and 5, and out put it.
"""

def find_multiples():
    return [x for x in range(1, 100) if x % 3 == 0 and x % 5 == 0]


"""
3. Create a 2 -D Array and slice out 3 numbers out the second column.
"""

def slice_2d_array():
    arr = np.arange(0, 100).reshape(10, 10)
    return arr[:, 2]


"""
4. Wallstreet wants to know the open and close price for amazon. 
Download the amazon csv or yfinance and print out only 
the open and close price for the amazon stock.
"""

def yfinance_amazon():
    amazon = yf.Ticker('AMZN')
    data = amazon.history(period='1d', interval='1m')
    # return open and close price for the amazon stock
    return data['Open'], data['Close']


"""
5. Download and csv file and put it in your dataframe. 
Your task is to rename a column inside your dataframe.
"""

def rename_column():
    df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv')
    df.rename(columns={'Date': 'Changed Date'}, inplace=True)
    return df


"""
6. Create "2" 1-D array and divide both of the array's
"""

def divide_array():
    arr1 = np.arange(1, 100)
    arr2 = np.arange(1, 100)
    random.shuffle(arr1)
    random.shuffle(arr2)
    
    result = arr1 / arr2
    # use lambda to round off each element in the array to 2 decimal places
    result = np.array(list(map(lambda x: round(x, 2), result)))
    return result


"""
7. Create a scatter plot that print out stars 
instead of circles inside your graph.
"""

def scatter_plot():
    x = np.arange(0, 100)
    y = np.arange(0, 100)
    random.shuffle(x)
    random.shuffle(y)
    size = np.arange(0, 100)
    colors = np.arange(0, 100)
    return plt.scatter(x, y, s=size, c=colors, marker='*')



def main():
    # 1. Create a list called basketball players.
    print("---- basketball ---")
    basketball_players()

    # 2. You are given a task to find all of the whole numbers below 100 that are multiples of borh 3 and 5. Create an array of numbers below 100 that are multiples of both 3 and 5, and out put it.
    print("---- find_multiples ---")
    print(find_multiples())

    # 3. Create a 2 -D Array and slice out 3 numbers out the second column.
    print("---- slice_2d_array ---")
    print(slice_2d_array())

    # 4. Wallstreet wants to know the open and close price for amazon. Download the amazon csv or yfinance and print out only the open and close price for the amazon stock.
    print("---- yfinance_amazon ---")
    open, close = yfinance_amazon()
    print(open)
    print(close)

    # 5. Download and csv file and put it in your dataframe. Your task is to rename a column inside your dataframe.
    print("---- rename_column ---")
    print(rename_column())

    # 6. Create "2" 1-D array and divide both of the array's
    print("---- divide_array ---")
    print(divide_array())

    # 7. Create a scatter plot that print out stars instead of circles inside your graph.
    print("---- scatter_plot ---")
    scatter_plot()
    plt.title('Scatter Plot')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.colorbar()
    plt.show()


if __name__ == '__main__':
    main()
