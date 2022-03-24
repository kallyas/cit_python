# 1. What is the correct way to start your pandas series?
# pd.Series()

"""
2. Whats the output of this code? 
car_sales = { "Bmw":[20000,30000,40000,50000], "Lambo":[100000,200000,300000,400000], "Nissan":[9000,11000,17000,19000] } 
data = pd.DataFrame(car_sales) 
print(car_sales)
"""
# None of the above

"""
Whats the output of this code? 
car_sales = { "Bmw":[20000,30000,40000,50000], "Lambo":[100000,200000,300000,400000], "Nissan":[9000,11000,17000,19000] } 
print(data.columns[1:])
"""
# None of the above

"""
4. True or False? iloc is label-based, which means that we have to specify the name of the rows and columns that we need to filter out.
"""
# True

"""
5. What is the correct way to read a csv file in your script?
"""
# pd.read_csv('data.csv')

"""
6. You are given a dictionary that contains names and numbers of people.
You need to create a DataFrame from the dictionary and add an index to it, 
which should be the name values.Then take a name from user input and output the row in the DataFrame, 
which corresponds to that row.
"""

names_and_numbers = {}

def add_names_and_numbers(name, number):
    names_and_numbers[name] = [number]


def create_dataframe(names_and_numbers, index_name, pd):
    df = pd.DataFrame(names_and_numbers)
    return df[ index_name ]

"""
7. "Seats in a Theater." You are given an array that represents the occupancy of seats in a movie theater. 
A seat marked with 1 is occupied, while one marked 0 means the seat is free.However, the array is flat and 1-dimensional. 
Transform it into a 2-dimensional array, representing the rows of the seats.Each row in the theater has 5 seats and there are a total of 30 seats.
Reshape the array into the corresponding shape and output the row at the given index, which is taken from user input.
"""

def reshape_seats_and_output_row(seats, index):
    return seats.reshape(5,6)[index]


"""
8. Given a list of numbers and the number of rows (r), 
reshape the list into a 2-dimensional array. 
Note that r divides the length of the list evenly. 
First line: an integer (r) indicating the number of rows of the 2-dimensional array
Next line: numbers separated by the space. An numpy 2d array of values rounded to the second decimal.
"""

def reshape_list_into_array(list, r, np):
    return np.array(list).reshape(r, -1)


"""
9. Create housing prices, you need to calculate and output the number of houses that have a price that is above the average. 
To calculate the average price of the houses, you need to divide the sum of all prices by the number of houses.
"""

def calculate_average_price(prices):
    return sum(prices) / len(prices)

def calculate_number_of_houses_above_average(prices, average_price):
    return len([price for price in prices if price > average_price])


"""
10. Download any csv file and plot out the that data in 3 different graphs in 1 figure.
"""

def plot_csv_data(filename, plt, pd):
    df = pd.read_csv(filename, nrows=100)
    
    fg, ax = plt.subplots(3, 1, sharex=True)
    artists = df['artist']
    weeks_on_board = df['weeks-on-board']

    df.plot(kind="line", ax=ax[0])
    # pie chart for artists/weeks_on_board
    ax[1].pie(weeks_on_board, labels=artists, autopct='%1.1f%%')

    # bar chart for artists/weeks_on_board
    ax[2].bar(artists, weeks_on_board)

    plt.show()


def main():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import json

    # add names and numbers to names_and_numbers dictionary
    names = ["Divina","Jozlyn","Kassie","Rayven","Arin","Ivan","Sidney","Ellanor","Catherine","Maja"]
    phones = [123456789,234567890,345678901,456789012,567890123,678901234,789012345,890123456,901234567,123456780]
    for name, phone in zip(names, phones):
        add_names_and_numbers(name, phone)
        
    # create dataframe
    df = create_dataframe(
        names_and_numbers, 
        input("Enter any name from the list {}: ".format(names)), 
        pd)
    print(df)
    # print(row)

    # reshape seats
    # creat seats list of random 0 and 1 length 30
    seats = np.random.randint(0, 2, 30)
    print("ndim: {}".format(seats.ndim))
    seat_row = reshape_seats_and_output_row(seats, index=2)
    print(seat_row)

    # reshape list into array
    # my_list is a 4D list with length 16
    my_list = [[[[ x for x in range(4)] for x in range(4)] for x in range(4)] for x in range(4)]
    print(my_list)
    reshaped = reshape_list_into_array(my_list, 4, np)
    print(reshaped)

    # housing prices
    housing_prices = [100000,200000,300000,400000,500000,600000,700000,800000,900000,1000000]
    average_price = calculate_average_price(housing_prices)
    print(average_price)
    number_of_houses_above_average = calculate_number_of_houses_above_average(housing_prices, average_price)
    print(number_of_houses_above_average)

    # plot csv data
    filename = 'charts.csv'
    plot_csv_data(filename=filename, plt=plt, pd=pd)



if __name__ == '__main__':
    main()

