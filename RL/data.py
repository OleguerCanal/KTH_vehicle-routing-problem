# Script to easily test different initial states
from airline_objects import Person, Plane, State, Flight, Action
import itertools
import numpy as np
import copy

cities = ["A", "B", "C", "D"]
city_distances =   [[0, 1, 1, 1],
                    [1, 0, 1, 1],
                    [1, 1, 0, 1],
                    [1, 1, 1, 0]]
time_steps = 5


def get_initial_state():
    people =   [Person("A", "B"),\
                Person("A", "B"),\
                Person("A", "D"),\
                Person("B", "C")]
    planes = [Plane("A", 3), Plane("B", 3)]
    return State(cities, people, planes, city_distances), time_steps

def get_random_state(city_number, people_number, planes_number):
    random_cities = range(city_number)
    people = []
    for i in range(people_number):
        people.append(Person(np.random.choice(random_cities), np.random.choice(random_cities)))
    
    planes = []
    for i in range(planes_number):
        planes.append(Plane(np.random.choice(random_cities), 2))

    return State(random_cities, people, planes, city_distances), time_steps
    

if __name__ == "__main__":
    state, steps = get_initial_state()
    print(state)
    actions = state.get_actions()
    print(actions[4])
    state.apply_action(actions[4])
    print(state)
    # state.get_actions()
    for action in state.get_actions():
        print(action)
    # action = state.get_actions()[0]
    # print(action)
    # state.apply_action(action)
    # print(state)
