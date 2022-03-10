"""
Homework assignment
1.Create a grid graph called Vaccine Data, and display 
in the graph of the data increasing then decreasing at the end.
2.Create a 4-D array and change it to a 1-D array.
3.Create 4 different Graphs in 1 figure.
4.Find out the standard Deviation for the Vaccine Data.

"""

def vaccine_data():
    """
    Create a grid graph called Vaccine Data, and display 
    in the graph of the data increasing then decreasing at the end.
    """
    import numpy as np
    import matplotlib.pyplot as plt
    # Create a grid graph called Vaccine Data
    data = np.random.randint(0, 100, (10, 10))
    # Display in the graph of the data increasing then decreasing at the end.
    plt.imshow(data, cmap='hot', interpolation='nearest')
    plt.title("Vaccine Data")
    plt.colorbar()
    plt.show()


def four_d_array():
    """
    Create a 4-D array and change it to a 1-D array.
    """
    import numpy as np
    # Create a 4-D array
    data = np.random.randint(0, 100, (10, 10, 10, 10))
    # Change it to a 1-D array
    data = data.flatten()
    print(data)


def four_graphs():
    """
    Create 4 different Graphs in 1 figure.
    """
    import numpy as np
    import matplotlib.pyplot as plt
    # Create 4 different Graphs in 1 figure.
    # graphs to be plotted: bar, line, scatter, pie

    data_x = np.random.randint(0, 100, (10, 10))
    data_y = np.random.randint(50, 100, (10, 10))
    data_fruits = ["apples", "oranges", "mangoes", "grapes"]
    data_fruits_sales = [200, 600, 400, 1000]

    # heatmap graph
    plt.subplot(221)
    plt.imshow(data_x, cmap='hot', interpolation='nearest')
    plt.title("Heatmap")
    plt.colorbar()


    # line graph
    plt.subplot(222)
    plt.plot(data_x, data_y)
    plt.title('Line Graph')
    plt.xlabel('X')
    plt.ylabel('Y')

    # scatter graph
    plt.subplot(223)
    plt.scatter(data_x, data_y)
    plt.title('Scatter Graph')
    plt.xlabel('X')

    # pie graph
    plt.subplot(224)
    plt.pie(data_fruits_sales, labels=data_fruits, autopct='%1.1f%%')
    plt.title('Pie Graph')
    plt.legend()

    plt.show()



def standard_deviation():
    """
    Find out the standard Deviation for the Vaccine Data.
    """
    import numpy as np
    # Find out the standard Deviation for the Vaccine Data.
    data = np.random.randint(0, 100, (10, 10))
    print(f"Standard Deviation: {np.std(data)}")


if __name__ == '__main__':
    vaccine_data()
    four_d_array()
    four_graphs()
    standard_deviation()