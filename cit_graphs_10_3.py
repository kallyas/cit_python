import random
import numpy as np
import matplotlib.pyplot as plt



"""
1.Create a plot graph that have 2 lines intersecting 
and add a point to the plot.
"""

def plot_graph():
    line_one = np.arange(0, 10, 4)
    line_two = np.arange(10, 0, -4)
    x_axis = np.arange(0, 10, 4)
    plt.style.use('seaborn-whitegrid')
    plt.plot(line_one, x_axis, 'r', marker='o')
    plt.plot(line_two, x_axis, 'b', marker='o')
    # set max width of the plot
    plt.xlim(0, 10)

"""
2.Create a bar graph displaying a label 
for the y axis and x axis. Inside a grid.
"""

def sports_bar_graph():
    sports = ['Tennis', 'Cricket', 'Football', 'Basketball', 'Golf', 'Rugby', 'Hockey']
    times = [10, 20, 30, 40, 50, 60, 70]
    random.shuffle(times)
    colors = ['r', 'b', 'g', 'y', 'c', 'm', 'k']
    random.shuffle(colors)
    plt.style.use('seaborn-whitegrid')
    plt.bar(sports, times, color=colors)
    plt.title('Sports Data')
    plt.xlabel('Sports')
    plt.ylabel('Times')


"""
Top 5 students pass the exam,create a pie graph of
the students scores from highest to lowest,
then find the total average of the students.
"""

def top_five_students():
    scores = [80, 90, 70, 60, 100]
    explode = [0, 0, 0, 0, 0.1]
    labels = ['Student 1', 'Student 2', 'Student 3', 'Student 4', 'Student 5']
    plt.pie(scores, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title('Top 5 Students')
    print(f"The total average of the students is {sum(scores)/len(scores)}")


"""
4.Create a scatter plot displaying any color you desire 
but in different sizes and the plot have to be in stars.
(add a color bar).
"""

def scatter_plot():
    x = np.random.rand(100)
    y = np.random.rand(100)
    plt.style.use('dark_background')
    plt.scatter(x, y, c='r', marker='*')
    plt.title('Scatter Plot')
    plt.colorbar()


"""
5.Put question 1,2,3,and 4 graphs in one figure.
"""

def combine_graphs():
    plt.subplot(2,2,4)
    plot_graph()
    plt.subplot(2,2,1)
    sports_bar_graph()
    plt.subplot(2,2,2)
    top_five_students()
    plt.subplot(2,2,3)
    scatter_plot()
    plt.show()


if __name__ == '__main__':
    combine_graphs()