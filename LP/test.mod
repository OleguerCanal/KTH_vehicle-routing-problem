# OBJECTS ------------------------------------------
param TIMESTEPS;

set CITIES;
set PLANES;
set PEOPLE;
set TIME = 0 .. TIMESTEPS;
set POSITIVE_TIME = 1 .. TIMESTEPS;

param PLANE_ORIGIN {p in PLANES} in CITIES;
param PERSON_ORIGIN {p in PEOPLE} in CITIES;
param PERSON_DEST {p in PEOPLE} in CITIES;

var PLANE_POS {p in PLANES, t in TIME} in CITIES; # Traks where each person is
var PERSON_POS {p in PEOPLE, t in TIME} in CITIES; # Traks where each person is

var PERSON_GETS_PLANE {p in PEOPLE, pl in PLANES, t in TIME} binary;


# OPTIMIZATION ------------------------------------------
# Computes the distance from a person to their goal
# IDEA: PENALIZE A LOT IF DISTANCE != 0 TO ENCOURAGE PEOPLE GETTING TO THEIR GOALS
var PERSON_DISTANCE {p in PEOPLE} =
	if PERSON_POS[p, TIMESTEPS] - PERSON_DEST[p] > 0
	then PERSON_POS[p, TIMESTEPS] - PERSON_DEST[p] else PERSON_DEST[p] - PERSON_POS[p, TIMESTEPS]; 
# Minimizes total distances
minimize PEOPLE_DIST:
	sum {p in PEOPLE} PERSON_DISTANCE[p];
	

# CONSTRAINS ------------------------------------------
# Person position stays the same unless takes plane
s.t. STATIONARY {p in PEOPLE, pl in PLANES, t in POSITIVE_TIME}:
	if not PERSON_GETS_PLANE[p, pl, t]
	then PERSON_POS[p, t] = PERSON_POS[p, t-1];