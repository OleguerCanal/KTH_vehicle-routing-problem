# Creddit to: https://github.com/naifmeh/
# Code from: https://github.com/naifmeh/smartbot/blob/master/utils/plotting.py
import matplotlib
import numpy as np
from collections import namedtuple
from matplotlib import pyplot as plt
import pandas as pd

EpisodeStats = namedtuple("Stats", ["episode_lengths", "episode_rewards"])
BotStats = namedtuple("Bot", ["blocked", "not_blocked"])


def plot_episode_stats(stats, smoothing_window=10, noshow=False, title="None"):

    # Plot the episode reward over time
    fig = plt.figure(figsize=(10, 5))
    rewards_smoothed = pd.Series(stats.episode_rewards).rolling(smoothing_window, min_periods=smoothing_window).mean()
    plt.plot(rewards_smoothed)
    plt.xlabel("Episode")
    plt.ylabel("Episode Reward (Smoothed)")
    if title != "None":
        plt.title(title)
    else:
        plt.title("Episode Reward over Time (Smoothed over window size {})".format(smoothing_window))
    if noshow:
        plt.close(fig)
    else:
        plt.show(fig)

    return fig