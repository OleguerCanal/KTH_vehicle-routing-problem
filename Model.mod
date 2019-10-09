set TIMESLOTS; #time
set TIMESLOTS1;
set ORIGIN;
set DESTINATION;
set PLANES;
set K;
param SEATS; #number of seats
param AIRTIME {i in ORIGIN, j in DESTINATION};
param TIME; #sum {j in FLIGHTS} AIRTIME[j]; #total time elapsed = sum of airtimes
param PASSENGERS {i in ORIGIN, j in DESTINATION};

var x {i in ORIGIN, j in DESTINATION, p in PLANES, t in TIMESLOTS} binary; #x[p,i,j,t]=1 if plane p travels from i to j at timeslot t

var m {i in ORIGIN, j in DESTINATION, p in PLANES, t in TIMESLOTS} <= SEATS,>=0; 

maximize profit: #number of filled seats*flytime*if flight occured
	sum {i in ORIGIN, j in DESTINATION, p in PLANES, t in TIMESLOTS} (AIRTIME[i,j]*m[i,j,p,t]*x[i,j,p,t]);

s.t. maxflights{p in PLANES}: #cannot take more flights than timeslots
    sum {i in ORIGIN, j in DESTINATION, t in TIMESLOTS} x[i,j,p,t] <= 3;

s.t. time{p in PLANES}: #cannot exceed deadline
	sum {i in ORIGIN, j in DESTINATION, t in TIMESLOTS} x[i,j,p,t]*AIRTIME[i,j] <= TIME;

s.t. origin {j in DESTINATION, p in PLANES, t in TIMESLOTS1}: #next flight must leave from previous destinations
	sum {i in ORIGIN} x[i,j,p,t] - sum {k in K} x[j,k,p,t+1] = 0;

s.t. oneflight {p in PLANES, t in TIMESLOTS}:
	sum {i in ORIGIN, j in DESTINATION} x[i,j,p,t] <= 1;

s.t. norepeats {i in ORIGIN, j in DESTINATION, p in PLANES}:
	sum {t in TIMESLOTS} x[i,j,p,t] <= 1;

s.t. peoplemoved{i in ORIGIN, j in DESTINATION}:
	sum {p in PLANES, t in TIMESLOTS} m[i,j,p,t] <= PASSENGERS[i,j];

s.t. solve {t in TIMESLOTS, p in PLANES}:
	sum {i in ORIGIN, j in DESTINATION} m[i,j,p,t] >= 1;
	
s.t. differentflights {i in ORIGIN, j in DESTINATION}:
	sum {p in PLANES, t in TIMESLOTS} x[i,j,p,t]*PASSENGERS[i,j] <= PASSENGERS[i,j];

#s.t. xvar:
#	sum {i in ORIGIN, j in DESTINATION, t in TIMESLOTS} m[i,j,t]*x[i,j,t] 
#	= sum {i in ORIGIN, j in DESTINATION, t in TIMESLOTS} m[i,j,t];

#s.t. capacity {i in ORIGIN, j in DESTINATION, t in TIMESLOTS}:
#	m[i,j,t] <= 26;
	
#s.t. differentflights {i in ORIGIN, j in DESTINATION, t in TIMESLOTS}:
#	 sum {p in PLANES} x[p,i,j,t] <= PASSENGERS[i,j];
