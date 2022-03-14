# 1. Which is the correct way to change the graph background in Matplotlib?
#  plt.style.use()

# 2. Which is the correct way to find the variance in a array?
#  np.var()

# 3. Which is the correct way to flatten a array?
#  np.ravel()

# 4. True or False? linspace is an in-built function in Python's NumPy library. It is used to create an evenly spaced sequence in a specified interval.​
#  True

"""
5. Roc nation record label has 4 artist that had their album come out last friday. 
In the first week,Rihanna sold 100,000,Kanye sold 95,000,J.cole sold 70,000,and Wale sold 35,000 in the first week. 
Display each sales in the first week using any graph in Matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt

def plot_artist_sales():
    artists = ['Rihanna', 'Kanye', 'J.cole', 'Wale']
    sales = [100000, 95000, 70000, 35000]
    colors = ['red', 'blue', 'green', 'yellow']
    plt.bar(artists, sales, color=colors)
    plt.title('Artist Sales in First Week')
    plt.show()



"""
6. Roc nation record label wants to also analyze 
the album sales for those 4 artist in 6 different graphs in 1 figure.
"""

def visualize_artist_sales():
    artists = ['Rihanna', 'Kanye', 'J.cole', 'Wale']
    sales = [100000, 95000, 70000, 35000]
    colors = ['red', 'blue', 'green', 'yellow']

    fig, ax = plt.subplots(nrows=2, ncols=3)

    # figure Title
    fig.suptitle('Artist Sales in First Week by Different charts')
    
    # 1st graph - bar chart
    ax[0, 0].bar(artists, sales, color=colors)
    ax[0, 0].set_title('Artist Sales in First Week - Bar Chart')
    ax[0, 0].set_xlabel('Artists')
    ax[0, 0].set_ylabel('Sales')

    # 2nd graph - pie chart
    explode = (0.1, 0.2, 0.2, 0.1)
    ax[0, 1].pie(sales, explode=explode, labels=artists, autopct='%1.1f%%', shadow=True, startangle=90)
    ax[0, 1].axis('equal')
    ax[0, 1].set_title('Artist Sales in First Week by Pie Chart')

    # 3rd graph - line chart
    ax[0,2].plot(artists, sales)
    ax[0,2].set_title('Artist Sales in First Week - Line Chart')


    # 4th graph - scatter plot
    # sizes = each artist's sales / 100
    sizes = [sales[i] / 100 for i in range(len(sales))]
    ax[1,0].scatter(artists, sales, color=colors, s=sizes, alpha=0.5, marker='o', edgecolors='black', cmap=plt.cm.Blues)
    ax[1,0].set_xlabel('Artists')
    ax[1,0].set_ylabel('Sales')
    ax[1,0].set_title('Artist Sales in First Week - Scatter Plot')


    # 5th graph - histogram
    ax[1,1].hist(sales, bins=10, color='b', edgecolor='black', linewidth=1.5)
    ax[1,1].set_xlabel('Sales')
    ax[1,1].set_ylabel('Frequency')
    ax[1,1].set_title('Artist Sales in First Week - Histogram')


    # 6th graph - density plot
    ax[1,2].plot(artists, sales, 'o')
    ax[1,2].set_xlabel('Sales')
    ax[1,2].set_ylabel('Frequency')
    ax[1,2].set_title('Artist Sales in First Week - Density Plot')

    plt.show()



"""
7. Create a 2-D array and print only 1 column in that 2-D array.
"""

def print_column():
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(arr[:, 1])


"""
8. Create a plot graph that have the x axis going up 
then down and then up, and the y axis going down up and down.
 (Use different colors for the lines for axis x and y.
"""

def plot_graph():
    x = np.arange(0, 10, 0.1)
    y = np.sin(x)
    plt.plot(x, y, 'r')
    plt.plot(x, -y, 'b')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


"""
9. Create a scatter plot that has a color bar with different sizes and 
the the plot have to be a triangle instead of a circle.
"""

def scatter_plot():
    x = np.random.rand(100)
    y = np.random.rand(100)
    s = np.random.rand(100) * 100
    c = np.random.rand(100)
    plt.scatter(x, y, s=s, c=c, alpha=0.5, marker='^')
    plt.colorbar()
    plt.show()


"""
10. Create a list called rocnation sales, 
using the album sales that was displayed for Rihanna,Kanye,J.cole,and Wale. 
Find the total average,median,variance,and standard deviation of all 4 of those artist sales.
"""

def rocnation_sales():
    sales = [100000, 95000, 70000, 35000]
    print(f"Total average: {np.mean(sales)}")
    print(f"Total median: {np.median(sales)}")
    print(f"Total variance: {np.var(sales)}")
    print(f"Total standard deviation: {np.std(sales)}")



def main():
    plot_artist_sales()
    visualize_artist_sales()
    print_column()
    plot_graph()
    scatter_plot()
    rocnation_sales()


if __name__ == "__main__":
    main()