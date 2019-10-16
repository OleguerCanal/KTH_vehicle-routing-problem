from agent import RlAgent
from data import get_random_state
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import pickle
from data import *

if __name__ == "__main__":
    agent = RlAgent()

    # Fixed initialization
    initial_state, time_steps = problem_2_1() # From data file
    hp = []
    f = []
    probs = np.linspace(0,1,11)
    for prob in probs:
        stats, _, iterations = agent.train(initial_state, max_timesteps = time_steps,
                    num_episodes = 100, lr = 0.7, discount = 0.8, epsilon = 0.25,
                    miss_flight_prob = prob)  # 20% chance of missing flight (stochasticity)
        # plotting.plot_episode_stats(stats)
        score, happy_people, flights = agent.solve(initial_state, max_timesteps = time_steps)
        hp.append(happy_people)
        f.append(flights)
    
        np.save("hp.npy", hp)
        np.save("f.npy", f)


    hp = np.load("hp.npy")
    f = np.load("f.npy")

    fig = plt.figure()
    plt.plot( probs, hp, marker='', color='blue', linewidth=2,  label="People at destination")
    plt.plot( probs, f, marker='', color='red', linewidth=2, linestyle='dashed', label="Flight number")

    fig.suptitle('Stochastic effect')
    plt.legend()
    plt.xlabel('Missing flight probability')
    # plt.ylabel('number', fontsize=16)
    fig.savefig('test2.png')