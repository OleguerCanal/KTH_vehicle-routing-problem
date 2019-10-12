# RL Q-Learning implementation of airline variation of VRP
from collections import defaultdict
import numpy as np
import matplotlib 
import matplotlib.style 
import pandas as pd 
import sys 
import plotting 
matplotlib.style.use('ggplot')

from airline_objects import State, Action, step
from data import *
class RlAgent:
    def __init__(self):
        Q = defaultdict(lambda: np.zeros(1))

    def epsilon_greedy(self, state, epsilon, actions):
        probs = np.ones(num_actions, dtype = float)*epsilon/num_actions
        # best_action = np.argmax(Q[state]) # TODO(oleguer): Try this, should be faster
        best_action_indx = 0
        best_action_val = -np.inf
        for idx, action in enumerate(actions):
            if Q[state][action] > best_action_val:
                best_action_val = Q[state][action]
                best_action_indx = idx
        probs[best_action_indx] += (1.0 - epsilon)
        action_idx = np.random.choice(np.arange(len(probs)), p = probs)
        return actions[action_idx]

    def train(self, initial_state, num_episodes, alpha, discount, epsilon):
        stats = plotting.EpisodeStats( 
            episode_lengths = np.zeros(num_episodes), 
            episode_rewards = np.zeros(num_episodes))     
       
        # Create an epsilon greedy policy function 
        # appropriately for environment action space 
        policy = createEpsilonGreedyPolicy(Q, epsilon, env.action_space.n) 
        for ith_episode in range(num_episodes): 
            state = copy.deepcopy(initial_state)    
            
            for t in itertools.count(): # Repeat until convergence
                actions = state.get_actions()  # Get all possible actions
                action = epsilon_greedy(state, epsilon, actions)  # Choose one following epsilon-greedy
                next_state, reward, done = step(state, action)  # Take action
    
                # Update statistics 
                stats.episode_rewards[ith_episode] += reward
                stats.episode_lengths[ith_episode] = t
                
                # TD Update 
                best_next_action = np.argmax(Q[next_state])     
                td_target = reward + discount*Q[next_state][best_next_action] 
                td_delta = td_target - Q[state][action] 
                Q[state][action] += alpha*td_delta 
    
                # done is True if episode terminated    
                if done: 
                    break
                state = next_state 
        return Q, stats 

    def solve():
        pass




if __name__ == "__init__":
    agent = RlAgent()
    initial_state = get_initial_state_1() # From data file

