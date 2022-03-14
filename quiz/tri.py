import numpy as np
import matplotlib.pyplot as plt

def scatter_plot():
    x = np.random.rand(100)
    y = np.random.rand(100)
    s = np.random.rand(100) * 800
    c = np.random.rand(100)

    plt.scatter(x, y, s=s, c=c, alpha=0.5, marker='^')
    plt.colorbar()
    plt.show()


scatter_plot()
