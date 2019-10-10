from __future__ import print_function
from ortools.sat.python import cp_model
from ortools.linear_solver import pywraplp

# class Optimizer(cp_model.CpSolverSolutionCallback):
#     """Print intermediate solutions."""

#     def __init__(self, flights, timeslots, origin, destination, seats, time, sols):
#         cp_model.CpSolverSolutionCallback.__init__(self)
#         self._flights = flights
#         self._timeslots = timeslots
#         self._origin = origin
#         self._destination = destination
#         self._seats = seats
#         self._time = time
#         self._solutions = set(sols)
#         self._solution_count = 0

#     def on_solution_callback(self):
#         if self._solution_count in self._solutions:
#             print('Solution %i' % self._solution_count)
#             for i in range(self._origin):
#                 print('Origin %i' % i)
#                 for j in range(self._destination):
#                     is_Route = False
#                     for t in range(self._timeslots):
#                         if self.Value(self._flights[(i, j, t)]):
#                             is_Route = True
#                             print('  Plane goes from %i to %i at time %i' % (i, j, t))
#                     #if not is_Route:
#                         #print('  Nurse {} does not work'.format(n))
#             print()
#         self._solution_count += 1

#     def solution_count(self):
#         return self._solution_count

def main():

    # TODO: Define problem as GLOP or Constraints Satisfiability

    # Create the linear solver with the GLOP backend.
    solver = pywraplp.Solver('simple_lp_program', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

    # -------------- DATA -------------- #

    #Parameters
    timeslots = 3
    origin = 3
    destination = origin
    #planes = 3 --> first start with one plane
    seats = 15
    time = 24

    passengers = [[0, 12, 15],
                [13, 0, 15],
                [14, 16, 0]]

    distances = [[0, 2, 5],
                [2, 0, 5],
                [5, 5, 0]]            

    #Sets
    all_timeslots = range(timeslots)
    all_origin = range(origin)
    all_destination = range(destination)
    #all_planes = range(planes)

    model = cp_model.CpModel();

    # -------------- VARIABLES -------------- #

    flights = {}

    # Creates flight variables
    # flights[(i,j,t)]: flight goes from 'i' to 'j' at time 't'
    for i in all_origin:
        for j in all_destination:
            for t in all_timeslots:
                flights[(i,j,t)] = model.NewBoolVar('flight_i%ij%it%i' % (i,j,t))

    # -------------- CONSTRAINTS -------------- #

    #TODO: Define constrains properly according to selected model

    # Each flight is assigned to only one origin-destination combination per timeslot
    for t in all_timeslots:
        model.Add(sum(sum(flights[(i,j,t)] for j in all_destination) for i in all_origin) == 1)

    # Number of flights must not be greater that maximum of timeslots
    model.Add(sum(sum(sum(flights[(i,j,t)] for t in all_timeslots) for j in all_destination) for i in all_origin) <= timeslots)

    # Time employed in flights must not be greater than maximum time
    model.Add(sum(sum(sum(flights[(i,j,t)] * distances[i][j] for t in all_timeslots) for j in all_destination) for i in all_origin) <= time)

    # Plane must depart at t+1 from same location it arrived at t
    for j in all_destination:
        for t in range(0, len(all_timeslots)-1):
            model.Add(sum(flights[(i,j,t)] for i in all_origin) - sum(flights[(j,k,t+1)] for k in destination) == 0)

    # Maximum of 1 flight per timeslot
    for t in all_timeslots:
        model.Add(sum(sum(flights[i,j,t] for j in all_destination) for i in all_origin) <= 1)

    # Plane cannot repeat location twice
    for i in all_origin:
        for j in all_destination:
            model.Add(sum(flights[i,j,t] for t in all_timeslots) <= 1)

    # -------------- OBJECTIVE FUNCTION -------------- #

    #TODO: define properly objective function

    objective = solver.Objective()
    objective.SetCoefficient()

    objective = sum(sum(sum(flights[(i,j,t)] * distances[i][j] * passengers[i][j] for t in all_timeslots) for j in all_destination) for i in all_origin)

    # # Creates the solver and solve.
    # solver = cp_model.CpSolver()
    # solver.parameters.linearization_level = 0
    # # Display the first five solutions.
    # a_few_solutions = range(5)

    # solution_printer = Optimizer(flights, timeslots, origin, destination, seats, time, a_few_solutions)
    # solver.SearchForAllSolutions(model, solution_printer)

    # # Statistics.
    # print()
    # print('Statistics')
    # print('  - conflicts       : %i' % solver.NumConflicts())
    # print('  - branches        : %i' % solver.NumBranches())
    # print('  - wall time       : %f s' % solver.WallTime())
    # print('  - solutions found : %i' % solution_printer.solution_count())


if __name__ == '__main__':
    main()