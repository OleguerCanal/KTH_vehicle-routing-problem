# Script to easily test different initial states
from airline_objects import Person, Plane, State
import itertools
import numpy as np


def get_initial_state_1():
    cities = ["A", "B", "C"]
    people = [Person(1, "A", "B"), Person(2, "A", "B")]
    planes = [Plane(1, "A"), Plane(2, "B")]
    return State(cities, people, planes)

if __name__ == "__main__":
    state = get_initial_state_1()
    print(state)

    actions = state.get_actions()
    print(len(actions))

    num = 15
    print(actions[num])
    state.apply_action(actions[num])
    print(state)