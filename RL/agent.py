# RL Q-Learning implementation of airline variation of VRP
from collections import defaultdict
import copy
import numpy as np
import matplotlib
import matplotlib.style
import itertools
import sys
from tqdm import tqdm
from utils import plotting 
matplotlib.style.use('ggplot')
import random

from airline_objects import State, Action, step
from data import get_initial_state, get_random_state

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
            print("State never seen, taking random action")
            return np.random.choice(state.get_actions())
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

    def train(self, initial_state, max_timesteps, num_episodes, lr, discount, epsilon, miss_flight_prob = 0):
        stats = plotting.EpisodeStats(
            episode_lengths = np.zeros(num_episodes),
            episode_rewards = np.zeros(num_episodes))
        
        total_actions_num = 0
        total_actions_num_size = 0
        
        print("Training...")
        for ith_episode in tqdm(range(num_episodes)):
            state = copy.deepcopy(initial_state)
            step_count = 0
            
            
            for t in itertools.count(): # Repeat until convergence
                actions = state.get_actions()  # Get all possible actions
                if len(actions) == 0:
                    break
                total_actions_num += len(actions)
                total_actions_num_size += 1
                action = self.__epsilon_greedy(state, epsilon, actions)  # Choose one following epsilon-greedy
                next_state, reward, done = step(state, action, miss_flight_prob)  # Take action
    
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
        # To compute branching factor stats
        branching_factor = 0
        if total_actions_num_size != 0:
            branching_factor = total_actions_num/total_actions_num_size
        return stats, branching_factor

    def solve(self, state, max_timesteps):
        done = False
        steps = 0
        while not done and steps < max_timesteps:
            print("\nSTEP: " + str(steps))
            best_action = self.Q.best_action(state)
            state, reward, done = step(state, best_action)
            print(best_action)
            steps += 1


if __name__ == "__main__":
    agent = RlAgent()

    # Fixed initialization
    initial_state, time_steps = get_initial_state() # From data file
    stats, _ = agent.train(initial_state, max_timesteps = time_steps,
                num_episodes = 1000, lr = 0.7, discount = 0.7, epsilon = 0.2,
                miss_flight_prob = 0.)  # 20% chance of missing flight (stochasticity)
    # plotting.plot_episode_stats(stats)
    agent.solve(initial_state, max_timesteps = time_steps)