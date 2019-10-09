/* Definition of sets */

set TIMESLOTS;
set TIMESLOTS1;
set ORIGIN;
set DESTINATION;
set K;
set PLANES;

/* Definition of parameters */

param SEATS; #number of seats
param AIRTIME {i in ORIGIN, j in DESTINATION};
param TIME; #sum {j in FLIGHTS} AIRTIME[j]; #total time elapsed = sum of airtimes
param PASSENGERS {i in ORIGIN, j in DESTINATION};

/* Definition of variables */

var x {i in ORIGIN, j in DESTINATION, p in PLANES, t in TIMESLOTS} binary; #x[p,i,j,t]=1 if plane p travels from i to j at timeslot t
var m {i in ORIGIN, j in DESTINATION, p in PLANES, t in TIMESLOTS};

/* Definition of Objective Function */

maximize profit: #number of filled seats*flytime*if flight occured
	sum {i in ORIGIN, j in DESTINATION, p in PLANES, t in TIMESLOTS} AIRTIME[i,j]*(m[i,j,p,t]+x[i,j,p,t]);

/* Definition of Constraints */

s.t. maxflights{p in PLANES}: #cannot take more flights than timeslots
    sum {i in ORIGIN, j in DESTINATION, t in TIMESLOTS} x[i,j,p,t] <= 3;

s.t. time{p in PLANES}: #cannot exceed deadline
	sum {i in ORIGIN, j in DESTINATION, t in TIMESLOTS} x[i,j,p,t]*AIRTIME[i,j] <= TIME;

s.t. origin {p in PLANES, j in DESTINATION, t in TIMESLOTS1}: #next flight must leave from previous destinations
	sum {i in ORIGIN} x[i,j,p,t] - sum {k in DESTINATION} x[j,k,p,t+1] = 0;

s.t. oneflight {p in PLANES, t in TIMESLOTS}:
	sum {i in ORIGIN, j in DESTINATION} x[i,j,p,t] <= 1;

s.t. norepeats {i in ORIGIN, j in DESTINATION, p in PLANES}:
	sum {t in TIMESLOTS} x[i,j,p,t] <= 1;

s.t. differentflights {i in ORIGIN, j in DESTINATION}:
	sum {p in PLANES, t in TIMESLOTS} x[i,j,p,t]*PASSENGERS[i,j] <= PASSENGERS[i,j];

s.t. peoplemoved{i in ORIGIN, j in DESTINATION}:
	sum {p in PLANES, t in TIMESLOTS} m[i,j,p,t] <= PASSENGERS[i,j];