import numpy as np
import itertools

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


# Given state and action applies step returns (next_state, reward, done)
def step(state, action):
    next_state = copy.deepcopy(state)
    next_state.apply_action(actoion)
    reward = next_state.happy_people() - state.happy_people()
    reward -= 1 # Penalize time
    # TODO(oleguer): Account for action cost (sum of flights cost)
    done = (next_state.happy_people == len(next_state.people))
    return next_state, reward