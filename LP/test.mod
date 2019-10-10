# OBJECTS ------------------------------------------
set CITIES;
set PLANES;
set PEOPLE;

param PLANE_ORIGIN {p in PLANES} in CITIES;
param PERSON_ORIGIN {p in PEOPLE} in CITIES;
param PERSON_DEST {p in PEOPLE} in CITIES;

var PLANE_POS {p in PLANES} in CITIES; # Traks where each person is
var PERSON_POS {p in PEOPLE} in CITIES; # Traks where each person is


# OPTIMIZATION ------------------------------------------
# Computes the distance from a person to their goal
# IDEA: PENALIZE A LOT IF DISTANCE != 0 TO ENCOURAGE PEOPLE GETTING TO THEIR GOALS
var PERSON_DISTANCE {p in PEOPLE} = if PERSON_POS[p] - PERSON_DEST[p] > 0 then PERSON_POS[p] - PERSON_DEST[p] else PERSON_DEST[p] - PERSON_POS[p]; 
# Minimizes total distances
minimize PEOPLE_DIST:
	sum {p in PEOPLE} PERSON_DISTANCE[p];
	

# CONSTRAINS ------------------------------------------
