def visualize_artist_sales():
    import matplotlib.pyplot as plt

    artists = ['Rihana', 'Kanye', 'J.Cole', 'Wale']
    sales = [100000, 95000, 70000, 35000]
    colors = ['red', 'blue', 'green', 'yellow']

    fig, ax = plt.subplots(nrows=2,ncols=3)

    # figure title
    fig.suptitle('Artists sales by Different charts for Roc Nation')

    # Bar Graph
    ax[0, 0].bar(artists, sales, color=colors)
    ax[0, 0].set_title('Bar Graph')
    ax[0, 0].set_xlabel('Artists')
    ax[0, 0].set_ylabel('Sales')

    # pie chart
    explode = (0.1, 0.1, 0.1, 0.1)
    ax[0, 1].pie(sales, explode=explode, labels=artists, autopct='%1.1f%%',
                 shadow=True, startangle=90)
    ax[0, 1].set_title('Pie chart')

    # line graph
    ax[1, 1].plot(artists, sales)
    ax[1, 1].set_title('Line Graph')

    # scatter graph
    sizes = [sales[i]/100 for i in range(len(sales))]
    ax[1, 0].scatter(artists, sales, color=colors, s=sizes, alpha=0.5,
                     marker='o', edgecolors='black')
    ax[1, 0].set_xlabel('Artists')
    ax[1, 0].set_ylabel('Sales')
    ax[1, 0].set_title('Scatter graph')

    # histogram
    ax[0, 2].hist(sales, color='b', edgecolor='black', linewidth=1.5)
    ax[0, 2].set_xlabel('Artists')
    ax[1, 0].set_ylabel('Sales')
    ax[1, 0].set_title('Histogram graph')

    # density graph
    ax[1, 2].plot(artists, sales, 'o')
    ax[1, 2].set_xlabel('Sales')
    ax[1, 2].set_ylabel('Artists')
    ax[1, 2].set_title('Density plot')

    plt.show()



# visualize_artist_sales()

import numpy as np
import matplotlib.pyplot as plt

def plot_graph():
    x = np.arange(0, 10, 0.1)
    y = np.sin(x)
    plt.plot(x, y, 'r')
    plt.plot(x, -y, 'b')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


plot_graph()