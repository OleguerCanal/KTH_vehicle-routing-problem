# Script to easily test different initial states
from airline_objects import Person, Plane, State, Flight, Action
import itertools
import numpy as np
import copy

time_steps = 5

def get_initial_state():
    cities = ["A", "B", "C", "D"]
    people =   [Person("A", "B"),\
                Person("A", "B"),\
                Person("A", "B"),\
                Person("A", "D"),\
                Person("B", "C")]
    planes = [Plane("A", 2), Plane("B", 3)]
    return State(cities, people, planes, city_distances), time_steps

def problem_0_1():
    cities = ["1", "2", "3", "4"]
    people =   [Person("1", "2"),\
                Person("2", "3"),\
                Person("2", "3"),\
                Person("3", "1"),\
                Person("3", "2")]
    planes = [Plane("2", 10)]
    time_steps = 4
    return State(cities, people, planes), time_steps

def problem_0_2():
    cities = ["1", "2", "3", "4"]
    city_distances =   [[0, 1, 1, 1],
                        [1, 0, 1, 1],
                        [1, 1, 0, 1],
                        [1, 1, 1, 0]]
    people =   [Person("1", "2"),\
                Person("2", "4"),\
                Person("2", "3"),\
                Person("3", "1"),\
                Person("3", "2")]
    planes = [Plane("3", 10)]
    time_steps = 4
    return State(cities, people, planes, city_distances), time_steps

def problem_0_3():
    cities = ["1", "2", "3", "4"]
    city_distances =   [[0, 1, 1, 1],
                        [1, 0, 1, 1],
                        [1, 1, 0, 1],
                        [1, 1, 1, 0]]
    people =   [Person("1", "2"),\
                Person("1", "2"),\
                Person("1", "2")]
    planes = [Plane("2", 10)]
    time_steps = 4
    return State(cities, people, planes, city_distances), time_steps

def problem_0_4():
    cities = ["1", "2", "3", "4", "5", "6"]
    people =   [Person("2", "6"),\
                Person("4", "1"),\
                Person("4", "2"),\
                Person("4", "2"),\
                Person("4", "5"),\
                Person("5", "2"),\
                Person("5", "6")]
    planes = [Plane("2", 10)]
    time_steps = 5
    return State(cities, people, planes), time_steps

def problem_1_1():
    cities = ["1", "2", "3", "4", "5", "6"]
    people =   [Person("2", "1"),\
                Person("5", "6"),\
                Person("5", "6")]
    planes = [Plane("3", 1), Plane("4", 2)]
    time_steps = 2
    return State(cities, people, planes), time_steps

def problem_1_2():
    cities = ["1", "2", "3", "4", "5"]
    people =   [Person("3", "1"),\
                Person("3", "1"),\
                Person("3", "1"),\
                Person("3", "2"),\
                Person("4", "2"),\
                Person("4", "2"),\
                Person("4", "2"),\
                Person("5", "4")]
    planes = [Plane("1", 3), Plane("5", 4)]
    time_steps = 4
    return State(cities, people, planes), time_steps

def problem_1_3():
    cities = ["1", "2", "3", "4", "5"]
    distances = [[0, 2, 2, 3, 4],
                [2, 0, 1, 3, 3],
                [2, 1, 0, 2, 2],
                [3, 3, 2, 0, 2],
                [4, 3, 2, 2, 0]]
    people =   [Person("2", "1"),\
                Person("2", "5"),\
                Person("2", "5"),\
                Person("4", "1"),\
                Person("4", "1"),\
                Person("4", "5"),\
                Person("5", "1"),\
                Person("5", "1")]
    planes = [Plane("2", 5), Plane("4", 3)]
    time_steps = 6
    return State(cities, people, planes, distances), time_steps
    # return State(cities, people, planes), time_steps

def problem_1_4():
    cities = ["1", "2", "3", "4", "5"]
    distances = [[0, 2, 2, 3, 4],
                [2, 0, 1, 3, 3],
                [2, 1, 0, 2, 2],
                [3, 3, 2, 0, 2],
                [4, 3, 2, 2, 0]]
    people =   [Person("1", "2"),\
                Person("1", "4"),\
                Person("1", "5"),\
                Person("3", "1"),\
                Person("3", "4"),\
                Person("3", "5")]
    planes = [Plane("1", 3), Plane("3", 5)]
    time_steps = 5
    # return State(cities, people, planes, distances), time_steps
    return State(cities, people, planes), time_steps

def problem_2_1():
    cities = ["1", "2", "3", "4"]
    city_distances =   [[0, 1, 1, 1],
                        [1, 0, 1, 1],
                        [1, 1, 0, 1],
                        [1, 1, 1, 0]]
    people =   [Person("1", "2"),\
                Person("1", "3"),\
                Person("1", "4"),\
                Person("1", "3"),\
                Person("2", "1"),\
                Person("2", "4"),\
                Person("2", "3"),\
                Person("3", "1"),\
                Person("3", "1"),\
                Person("3", "4"),\
                Person("4", "3"),\
                Person("4", "3"),\
                Person("4", "1")]
    planes = [Plane("1", 1), Plane("2", 2)]
    time_steps = 5
    return State(cities, people, planes, city_distances), time_steps

def get_random_state(city_number, people_number, planes_number):
    random_cities = range(city_number)
    # city_distances = np.ones((city_number, city_number)) - np.eye(city_number)
    # print(city_distances)
    people = []
    for i in range(people_number):
        people.append(Person(np.random.choice(random_cities), np.random.choice(random_cities)))
    
    planes = []
    for i in range(planes_number):
        planes.append(Plane(np.random.choice(random_cities), 2))

    return State(random_cities, people, planes), time_steps
    

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
