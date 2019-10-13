# RL Q-Learning implementation of airline variation of VRP
# Inspiration from https://www.geeksforgeeks.org/q-learning-in-python/
from collections import defaultdict
import copy
import numpy as np
import matplotlib
import matplotlib.style
import itertools
# import pandas as pd
import sys
from tqdm import tqdm
from utils import plotting 
matplotlib.style.use('ggplot')

from airline_objects import State, Action, step
from data import get_initial_state

class Quality():
    def __init__(self):
        self.Q = {}

    def update(self, state, action, value):
        if state not in self.Q:
            self.Q[state] = {}
        self.Q[state][action] = value

    def get(self, state, action):
        if state not in self.Q:
            return 0
        if action not in self.Q[state]:
            return 0
        return self.Q[state][action]
    
    def get_best_action_val(self, state):
        if state not in self.Q:
            return 0
        return np.argmax(self.Q[state])

    def select_best_action_indx(self, state, actions):
        best_action_indx = 0
        best_action_val = -np.inf
        for idx, action in enumerate(actions):
            val = self.get(state, action)
            if val > best_action_val:
                best_action_val = val
                best_action_indx = idx
        return best_action_indx

    def best_action(self, state):
        if state not in self.Q:
            return 0
        return max(self.Q[state], key=self.Q[state].get)

class RlAgent:
    def __init__(self):
        self.Q = Quality()

    def __epsilon_greedy(self, state, epsilon, actions):
        probs = np.ones(len(actions), dtype = float)*epsilon/len(actions)
        best_action_indx = self.Q.select_best_action_indx(state, actions)  
        probs[best_action_indx] += (1.0 - epsilon)
        action_idx = np.random.choice(np.arange(len(probs)), p = probs)
        return actions[action_idx]

    def train(self, initial_state, max_timesteps, num_episodes, lr, discount, epsilon):
        stats = plotting.EpisodeStats(
            episode_lengths = np.zeros(num_episodes),
            episode_rewards = np.zeros(num_episodes))
       
        for ith_episode in tqdm(range(num_episodes)):
            state = copy.deepcopy(initial_state)
            step_count = 0
            
            for t in itertools.count(): # Repeat until convergence
                actions = state.get_actions()  # Get all possible actions
                action = self.__epsilon_greedy(state, epsilon, actions)  # Choose one following epsilon-greedy
                next_state, reward, done = step(state, action)  # Take action
    
                # Update statistics 
                stats.episode_rewards[ith_episode] += reward
                stats.episode_lengths[ith_episode] = t
                
                # TD Update
                td_target = reward + discount*self.Q.get_best_action_val(next_state)
                old_val = self.Q.get(state, action)
                new_val = old_val + lr*(td_target - old_val)
                self.Q.update(state, action, new_val)
    
                if done or step_count >= max_timesteps:  # Limit search
                    break
                state = next_state
                step_count += 1
        return stats 

    def solve(self, state, max_timesteps):
        done = False
        steps = 0
        while not done and steps < max_timesteps:
            print("\nTIMESTEP: " + str(steps))
            best_action = self.Q.best_action(state)
            state, reward, done = step(state, best_action)
            print(best_action)
            print("Reward:", reward)
            # print(state)
            steps += 1


if __name__ == "__main__":
    initial_state, time_steps = get_initial_state() # From data file

    agent = RlAgent()
    stats = agent.train(initial_state, max_timesteps = time_steps,
                num_episodes = 200, lr = 0.7, discount = 0.7, epsilon = 0.2)

    plotting.plot_episode_stats(stats)
    agent.solve(initial_state, max_timesteps = 10)