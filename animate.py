import matplotlib.pyplot as plt
from celluloid import Camera

fg = plt.figure()
camera = Camera(fg)
comparison = 0

# plot data set and variable to highlight
def Plot(highlight, data):
    x = list(range(len(data)))

    global comparison
    comparison += 1

    colors = list(len(data) * 'b')
    colors[highlight] = 'r'
    plt.bar(x, data, colors=colors)
    plt.title("Quick Sort Algorithm Visualization")
    plt.xlabel("Data size {} Comparison {}".format(len(data), comparison))
    plt.ylabel("Data")
    camera.snap()