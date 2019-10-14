from agent import RlAgent
from data import get_random_state
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

def get_branch_factor(cities, people, planes, reps = 5):
    branch_factor = 0
    for _ in range(reps):
        initial_state, time_steps = get_random_state(cities, people, planes)
        stats, branch_fact = agent.train(initial_state, max_timesteps = time_steps,
                    num_episodes = 50, lr = 0.7, discount = 0.7, epsilon = 0.2)
        branch_factor += branch_fact
    branch_factor = branch_factor/reps
    return branch_factor

if __name__ == "__main__":
    agent = RlAgent()

    # Random initialization
    max_cities = 5
    min_people = 2
    max_people = 9

    min_planes = 1
    max_planes = 5

    # for city in cities:
    cities = max_cities
    X = np.arange(min_people, max_people, 2)
    Y = np.arange(min_planes, max_planes, 1)
    X, Y = np.meshgrid(X, Y)
    Z = np.zeros(X.shape)
    # a = raw_input()
    for i, people in enumerate(range(min_people, max_people, 2)):
        for j, planes in enumerate(range(min_planes, max_planes, 1)):
            Z[j][i] = get_branch_factor(cities, people, planes)

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                        linewidth=0, antialiased=False)

    # Customize the z axis.
    ax.set_zlim(0, np.max(Z))
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()