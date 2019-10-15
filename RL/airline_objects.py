import numpy as np
import itertools
import copy

# Global constants
PLANE_FLYING = "PLANE_FLYING"

class Person:
    class_counter = 0
    def __init__(self, origin, destination):
        self.id = Person.class_counter
        Person.class_counter += 1
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
    class_counter = 0
    def __init__(self, origin, seats):
        self.id = Plane.class_counter
        Plane.class_counter += 1
        self.origin = origin
        self.location = origin
        self.seats = seats

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
    def __init__(self, plane, origin, destination, passengers, state):
        self.plane = plane
        self.origin = origin
        self.destination = destination
        self.passengers = passengers
        self.original_distance = state.city_distance(origin, destination)
        self.remaining_distance = self.original_distance
    
    def has_plane(self, plane):
        return self.plane.id == plane.id

    def has_passenger(self, person):
        for p in self.passengers:
            if p.id == person.id:
                return True
        return False

    def get_cost(self):
        return self.original_distance # TODO(oleguer): Return distance between cities

    def __str__(self):
        s =  "Plane " + str(self.plane.id) + ": " + str(self.origin) + "->" + str(self.destination) + " Pass: "
        for person in self.passengers:
            s += str(person.id) + ", "
        s += "Timesteps To Dest: " + str(self.remaining_distance)
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
            # print(flight)
            for f in flight:
                self.flights.append(f)

    def get_cost(self):
        cost = 0
        for flight in self.flights:
            cost += flight.get_cost()
        return cost

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
    def __init__(self, cities, people, planes, distances=None):
        self.cities = cities
        self.planes = planes
        self.people = people
        self.ongoing_flights = []

        if distances == None:
            self.city_distances = np.ones((len(cities), len(cities))) -\
                                    np.eye((len(cities), len(cities)))
        else:
            self.city_distances = distances

    def city_distance(self, a, b):
        return self.city_distances[self.cities.index(a)][self.cities.index(b)]

    def happy_people(self):
        happy_people = 0
        for person in self.people:
            if (person.is_happy()):
                happy_people += 1
        return happy_people

    # Return True if combination of passengers is valid, False otherwise
    def __valid_combination(self, combination, planes_in_city):
        for plane in planes_in_city:
            if combination.count(plane.id) > plane.seats:
                return False
        return True

    # Retuns an array a such that a[i] = number of people in plane p
    def __group_passengers(self, people_in_city, combination, plane_ids):
        n_cities = len(self.cities)
        groupings = {}

        if sum(1 for i in combination if i != -1) == 0:
            return ""

        for plane_idx in plane_ids:
            if plane_idx != -1:
                groupings[plane_idx] = np.zeros(n_cities)

        for passenger_idx, plane_idx in enumerate(combination):
            if plane_idx != -1:
                destIdx = self.cities.index(people_in_city[passenger_idx].destination)
                groupings[plane_idx][destIdx] += 1

        res_str = ""
        for plane_idx in sorted(groupings):
            if plane_idx != -1:
                res_str += str(int(plane_idx))
                for n in groupings[plane_idx]:
                    res_str += str(int(n))
        return res_str

        

    def get_actions(self):
        if self.happy_people() == len(self.people):
            return []

        actions = []
        for city in self.cities:
            # Get people/planes in current city
            planes_in_city = self.__get_planes_in_city(city)
            if len(planes_in_city) == 0:
                continue

            people_in_city = self.__people_in_city(city)
            planes_id = [plane.id for plane in planes_in_city]
            planes_id.append(-1)  # -1 meaning they dont get on any plane
            
            # Get all possible passengers combinations
            combinations = list(itertools.product(planes_id, repeat=len(people_in_city)))
            seen_groupings = set()
            city_combinations = None
            for combination in combinations:
                if not self.__valid_combination(combination, planes_in_city):
                    continue

                grouping = self.__group_passengers(people_in_city, combination, planes_id)
                print("##############")
                for passenger in people_in_city:
                    print(passenger.destination)
                print(combination)
                print(grouping)
                print("##############")
                
                if grouping in seen_groupings:
                    continue
                else:
                   seen_groupings.add(grouping)
                
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
                        if (destination != city) or ((destination == city) and len(passengers) == 0):
                            plane_flights.append(Flight(plane, city, destination, passengers, self))
                    combination_flights.append(plane_flights)

                # Augment combinations
                combination_flights = list(itertools.product(*combination_flights))
                
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

    def apply_action(self, action, missed_plane_prob = 0.0):
        for flight in self.ongoing_flights:  # First check ongoing flights
            flight.remaining_distance -= 1
            if flight.remaining_distance <= 0:  # If plane has arrived
                self.ongoing_flights.remove(flight)  # Remove it from ongoing flights list
                for person in self.people:
                    if flight.has_passenger(person):
                        if np.random.uniform() >= missed_plane_prob:
                            person.location = flight.destination
                for plane in self.planes:
                    if flight.has_plane(plane):
                        plane.location = flight.destination

        for flight in action.flights:  # Then check new action flights
            flight.remaining_distance -=1
            if flight.remaining_distance <= 0:                      # Plane has arrived
                for person in self.people:
                    if flight.has_passenger(person):
                        if np.random.uniform() >= missed_plane_prob:
                            person.location = flight.destination
                for plane in self.planes:
                    if flight.has_plane(plane):
                        plane.location = flight.destination
            else:                                                   # Plane still flying
                for person in self.people:
                    if flight.has_passenger(person):
                        person.location = PLANE_FLYING
                for plane in self.planes:
                    if flight.has_plane(plane):
                        plane.location = PLANE_FLYING
                self.ongoing_flights.append(flight) # Save flight as ongoing

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
def step(state, action, missed_plane_prob = 0):
    # Compute next state
    next_state = copy.deepcopy(state)
    next_state.apply_action(action, missed_plane_prob)

    # Compute reward of this action
    reward = 2*(next_state.happy_people() - state.happy_people())   # Add happy people increment
    reward -= 2                                                     # Penalize time
    reward -= action.get_cost()                                     # Substract flights cost

    done = (next_state.happy_people() == len(next_state.people))
    if done:
        reward += 2*next_state.happy_people()
    return next_state, reward, done
