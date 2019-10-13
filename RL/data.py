# Script to easily test different initial states
from airline_objects import Person, Plane, State, Flight, Action
import itertools
import numpy as np
import copy


def get_initial_state_1():
    cities = ["A", "B", "C"]
    people = [Person(1, "A", "B"), Person(2, "A", "B")]
    planes = [Plane(1, "A"), Plane(2, "B")]
    time_steps = 5
    return State(cities, people, planes), time_steps

if __name__ == "__main__":
    pass
    # state, time_steps = get_initial_state_1()
    # print(state)

    # actions = state.get_actions()
    # print(len(actions))

    # num = 15
    # print(actions[num])
    # state.apply_action(actions[num])
    # print(state)
    # pers1 = Person(1, "A", "B")
    # pers2 = Person(2, "A", "B")
    # pers3 = Person(3, "A", "B")
    # pers4 = Person(4, "A", "B")
    # plane_1 = Plane(1, "A")
    # plane_2 = Plane(2, "C")
    # plane_3 = Plane(3, "A")
    # plane_4 = Plane(4, "B")
    # fligth1 = Flight(plane_1, "A", "B", [pers1, pers2])
    # fligth2 = Flight(plane_2, "A", "B", [pers1])
    # fligth3 = Flight(plane_3, "A", "B", [pers1, pers3])
    # fligth4 = Flight(plane_4, "B", "C", [pers1, pers4])

    # # print(fligth1 == fligth2)
    # # print(fligth1 == fligth3)

    # print(set([fligth1, fligth2]) == set([fligth1, fligth2]))
    # print(set([fligth2, fligth1]) == set([fligth1, fligth2]))
    # print(set([fligth2, fligth1]) == set([fligth3, fligth2]))

    # action1 = Action([[fligth1], [fligth2]])
    # action2 = Action([[fligth2], [fligth1]])
    # action3 = Action([[fligth1], [fligth3]])
    # print(action1 == action2)
    # print(action1 == action3)

    # print(action1)


    # # planes_1 = [Plane(1, "A"), Plane(2, "B")]
    # # planes_2 = [Plane(1, "A"), Plane(2, "B")]
    # # equal = (planes_1 == planes_2)
    # # equal2 = (Plane(1, "A") == Plane(1, "A"))
    # # print(equal)
    # # print(equal2)

    # # print(hash(Plane(1, "A")))
    # # print(hash(Plane(1, "A")))
    # # print(hash(copy.deepcopy(Plane(1, "A"))))

    # Dict = { } 
    # print("Initial nested dictionary:-") 
    # print(Dict) 
    
    # Dict['Dict1'] = {} 
    
    # # Adding elements one at a time  
    # Dict['Dict1']['name'] = 'Bob'
    # Dict['Dict1']['age'] = 21
    # print("\nAfter adding dictionary Dict1") 
    # print(Dict) 
    
    # # Adding whole dictionary 
    # Dict['Dict2'] = {'name': 'Cara', 'age': 25} 
    # print("\nAfter adding dictionary Dict1") 
    # print(Dict) 
