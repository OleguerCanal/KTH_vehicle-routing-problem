import numpy as np
import itertools
import copy

class Person:
    def __init__(self, id, origin, destination):
        self.id = id
        self.origin = origin
        self.location = origin
        self.destination = destination

    def is_happy(self):
        return self.location == self.destination

    def __str__(self):
        s =  "Pers: " + str(self.id)
        s += ",  Ori: " + str(self.origin)
        s +=  ", Loc: " + str(self.location)
        s +=  ", Dest: " + str(self.destination)
        return s

    def __eq__(self, other):
        if not (hasattr(other, "id") and (self.id == other.id)):
            return False
        return (self.location == other.location) and (self.destination == other.destination)

    def __hash__(self):
        hash_val = hash(self.id)
        hash_val += hash(self.location)
        hash_val += hash(self.destination)
        return hash_val
        # return hash(repr(self))

class Plane:
    def __init__(self, id, origin):
        self.id = id
        self.origin = origin
        self.location = origin
        #TODO(oleguer): Add plane characteristics

    def get_flights(self, state):
        '''Return list of Possible flights
        '''

    def __str__(self):
        s =  "Plane: " + str(self.id)
        s +=  ", Loc: " + str(self.location)
        return s
    
    def __eq__(self, other):
        if not (hasattr(other, "id") and (self.id == other.id)):
            return False
        return other.location == self.location

    def __hash__(self):
        hash_val = hash(self.id)
        hash_val += hash(self.location)
        return hash_val
        # return hash(repr(self))

class Flight:
    def __init__(self, plane, origin, destination, passengers):
        self.plane = plane
        self.origin = origin
        self.destination = destination
        self.passengers = passengers
    
    def has_plane(self, plane):
        return self.plane.id == plane.id

    def has_passenger(self, person):
        for p in self.passengers:
            if p.id == person.id:
                return True
        return False

    def __str__(self):
        s =  "Plane " + str(self.plane.id) + ": " + str(self.origin) + "->" + str(self.destination) + ": Pass: "
        for person in self.passengers:
            s += str(person.id) + ", "
        return s

    def __eq__(self, other):
        # print("eq")
        # print(other.plane == self.plane)
        # print(other.origin == self.origin)
        # print(other.destination == self.destination)
        # print(other.passengers == self.passengers)
        # print("---")
        return (other.plane == self.plane) and (other.origin == self.origin) and\
                (other.destination == self.destination) and (other.passengers == self.passengers)

    def __hash__(self):
        hash_val = hash(self.plane)
        hash_val += 2*hash(self.origin)
        hash_val += 3*hash(self.destination)
        for person in self.passengers:
            hash_val += hash(person)
        return hash_val

class Action:
    def __init__(self, flights):
        self.flights = []
        self.add_flights(flights)

    def add_flights(self, flights):
        for flight in flights:
            self.flights.append(flight[0])

    def __str__(self):
        print("Action:")
        for flight in self.flights:
            print(flight)
        return ""
    
    def __eq__(self, other):
        return set(self.flights) == set(other.flights)

    def __hash__(self):
        hash_val = 0
        for flight in self.flights:
            hash_val += hash(flight)
        return hash_val

class State:
    def __init__(self, cities, people, planes):
        self.cities = cities
        self.planes = planes
        self.people = people

    def happy_people(self):
        happy_people = 0
        for person in self.people:
            if (person.is_happy()):
                happy_people += 1
        return happy_people

    def get_actions(self):
        if self.happy_people() == len(self.people):
            return []

        actions = []
        for city in self.cities:
            # Get people/planes in current city
            planes_in_city = self.__get_planes_in_city(city)
            if len(planes_in_city) == 0:
                continue
            # for plane_inc in planes_in_city:
            #     print(plane_inc)
            people_in_city = self.__people_in_city(city)
            # for pers in people_in_city:
            #     print(pers)
            planes_id = [plane.id for plane in planes_in_city]
            planes_id.append(-1)  # -1 meaning they dont get on any plane
            
            # Get all possible passengers combinations
            combinations = list(itertools.product(planes_id, repeat=len(people_in_city)))

            city_combinations = None
            for combination in combinations:
                combination_flights = []
                for plane in planes_in_city:
                    # Get all passengers that go to the plane
                    passengers = []
                    for passenger, plane_id in zip(people_in_city, combination):
                        if plane_id == plane.id:
                            passengers.append(passenger)
                    
                    # Get all possible destinations
                    plane_flights = []
                    for destination in self.cities:
                        plane_flights.append(Flight(plane, city, destination, passengers))
                    combination_flights.append(plane_flights)
                
                # Augment combinations
                combination_flights = list(itertools.product(*combination_flights))
                # for comb in combination_flights:
                #     for fli in comb:
                #         print(fli)
                
                if city_combinations is None:
                    city_combinations = np.array(combination_flights)
                else:
                    city_combinations = np.concatenate((city_combinations, np.array(combination_flights)))
                
            actions.append(city_combinations)
        actions = list(itertools.product(*actions))

        # Compute final array of possible actions
        final_actions = []
        for action in actions:
            final_actions.append(Action(action))
        return final_actions

    def apply_action(self, action):
        for flight in action.flights:
            for person in self.people:
                if flight.has_passenger(person):
                    person.location = flight.destination
            for plane in self.planes:
                if flight.has_plane(plane):
                    plane.location = flight.destination

    def __people_in_city(self, city):
        people = []
        for person in self.people:
            if person.location == city and not person.is_happy():
                people.append(person)
        return people

    def __get_planes_in_city(self, city):
        planes = []
        for plane in self.planes:
            if plane.location == city:
                planes.append(plane)
        return planes

    def __str__(self):
        print("------")
        print("State:")
        for city in self.cities:
            print("City " + str(city) + ":")
            for person in self.people:
                if person.location == city:
                    print(person)
            for plane in self.planes:
                if plane.location == city:
                    print(plane)
        return "------"

    def __eq__(self, other):
        if other.planes != self.planes:
            return False
        if other.people != self.people:
            return False
        return self.cities == other.cities

    def __hash__(self):
        hash_val = 0
        for plane in self.planes:
            hash_val += hash(plane)
        for person in self.people:
            hash_val += hash(person)
        return hash_val

# Given state and action applies step returns (next_state, reward, done)
def step(state, action):
    next_state = copy.deepcopy(state)
    next_state.apply_action(action)
    reward = 2*(next_state.happy_people() - state.happy_people())
    reward -= 1 # Penalize time
    # TODO(oleguer): Account for action cost (sum of flights cost)
    done = (next_state.happy_people() == len(next_state.people))
    if done:
        reward += 1000
    return next_state, reward, done