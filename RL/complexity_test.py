from agent import RlAgent
from data import get_random_state
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import pickle


def get_branch_factor(cities, people, planes, reps = 10):
    branch_factor = 0
    for _ in range(reps):
        initial_state, time_steps = get_random_state(cities, people, planes)
        branch_factor += len(initial_state.get_actions())
    branch_factor = branch_factor/reps
    return branch_factor

def plot(X, Y, Z):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    # Plot the surface.
    Z = Z/1e6
    surf = ax.plot_surface(X[0:, 0:-1], Y[0:, 0:-1], Z[0:, 0:-1], cmap=cm.coolwarm,
                        linewidth=0, antialiased=False)

    # Customize the z axis.
    ax.set_zlim(0, np.max(Z))
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.1f'))

    ax.set_xlabel('People')
    ax.set_ylabel('Planes')
    ax.set_zlabel('branching_factor / 1e6')

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()


if __name__ == "__main__":
    # agent = RlAgent()

    # # Random initialization
    # max_cities = 5
    
    # min_people = 2
    # max_people = 13

    # min_planes = 1
    # max_planes = 7

    # # for city in cities:
    # cities = max_cities
    # X = np.arange(min_people, max_people, 2)
    # Y = np.arange(min_planes, max_planes, 1)
    # X, Y = np.meshgrid(X, Y)
    # Z = np.zeros(X.shape)
    # # a = raw_input()
    # for i, people in enumerate(range(min_people, max_people, 2)):
    #     for j, planes in enumerate(range(min_planes, max_planes, 1)):
    #         Z[j][i] = get_branch_factor(cities, people, planes)
    #         A = np.array([X, Y, Z])
    #         np.save("branching.npy", A)

    # plot(X, Y, Z)

    loaded = np.load("branching.npy")
    plot(loaded[0,:, :], loaded[1, :, :], loaded[2, :, :])

    

    
