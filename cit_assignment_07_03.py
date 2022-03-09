"""
1. create a 2-D array and grab 3 numbers in the second column
"""

from timeit import repeat
import numpy as np

def grab_three_numbers(array, col):
    """
    Grab three numbers from the second column of a 2-D array
    """
    return array[:, col]

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(grab_three_numbers(array, 1))

"""
2. create a list called company_data, using a function, a company needs to
know the total average, the variance and how spread out the data is
"""
company_data = np.array([45, 52, 67, 90, 23, 45, 67, 89, 90, 45])

def total_average(array):
    """
    Calculate the total average of a list
    """
    return np.mean(array)

def variance(array):
    """
    Calculate the variance of a list
    """
    return np.var(array)

def spread(array):
    """
    Calculate the spread of a list
    """
    return np.std(array)


print(f"The total average is: {total_average(company_data)}")
print(f"The variance is: {variance(company_data)}")
print(f"The spread is: {spread(company_data)}")

"""
3. create 2 arrays showing the x axis from 20 to 100 and the y axis from 120 to 200
(use matplotlib to visualize arrays x and y)
"""
import matplotlib.pyplot as plt

x = np.linspace(20, 100, num=10)
y = np.linspace(120, 200, num=10)

def visualize_arrays(x, y):
    """
    Visualize two arrays
    """
    plt.bar(x, y, align="edge")
    # show x and y legends
    plt.xlabel("X Array")
    plt.ylabel("Y Array")
    # show the plot
    plt.show()



visualize_arrays(x, y)

"""
4. Create a 2-d array and multiple both columns.
"""

two_d_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

def multiply_both_columns(array):
    """
    Multiply both columns of a 2-D array
    """
    return array[:, 0] * array[:, 1]


print(multiply_both_columns(two_d_array))

"""
5.Create any  sorting algorithm and show us the animation using matplotlib.
"""
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import axes3d
import matplotlib as mp
import numpy as np
import random

# quicksort function
def quicksort(array, start, end):
	if start >= end:
		return
	x = array[start]
	j = start
	for i in range(start + 1, end + 1):
		if array[i] <= x:
			j += 1
			array[j], array[i] = array[i], array[j]
		yield array
	array[start], array[j]= array[j], array[start]
	yield array

	# yield from statement used to yield
	# the array after dividing
	yield from quicksort(array, start, j-1)
	yield from quicksort(array, j + 1, end)

# function to plot bars
def visualize_quick_sort():

	# for random unique values
	n = int(input("enter array size\n"))
	array = [i for i in range(1, n + 1)]
	random.shuffle(array)
	datasetName ='Random'

	# generator object returned by the function
	generator = quicksort(array, 0, n-1)
	algoName = 'Quick Sort'

	# style of the chart
	plt.style.use('fivethirtyeight')

	# set colors of the bars
	data_normalizer = mp.colors.Normalize()
	color_map = mp.colors.LinearSegmentedColormap(
		"my_map",
		{
			"red": [(0, 1.0, 1.0),
					(1.0, .5, .5)],
			"green": [(0, 0.5, 0.5),
					(1.0, 0, 0)],
			"blue": [(0, 0.50, 0.5),
					(1.0, 0, 0)]
		}
	)

	fig, ax = plt.subplots()

	# bar container
	bar_rects = ax.bar(range(len(array)), array, align ="edge",
					color = color_map(data_normalizer(range(n))))

	# setting the limits of x and y axes
	ax.set_xlim(0, len(array))
	ax.set_ylim(0, int(1.1 * len(array)))
	ax.set_title("ALGORITHM : "+ algoName + "\n" + "DATA SET : " +
			datasetName, fontdict = {'fontsize': 13, 'fontweight':
									'medium', 'color' : '#E4365D'})

	# the text to be shown on the upper left indicating the number of iterations
	# transform indicates the position with relevance to the axes coordinates.
	text = ax.text(0.01, 0.95, "", transform = ax.transAxes, color = "#E4365D")
	iteration = [0]

	def animate(A, rects, iteration):
		for rect, val in zip(rects, A):

			# setting the size of each bar equal to the value of the elements
			rect.set_height(val)
		iteration[0] += 1
		text.set_text("iterations : {}".format(iteration[0]))

	# call animate function repeatedly
	anim = FuncAnimation(fig, func = animate,
		fargs = (bar_rects, iteration), frames = generator, interval = 50,
		repeat = False)
	plt.show()

visualize_quick_sort()








