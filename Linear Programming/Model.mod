set TIMESLOTS; #time
set TIMESLOTS1;
set ORIGIN;
set DESTINATION;
set K;
param SEATS; #number of seats
param AIRTIME {i in ORIGIN, j in DESTINATION};
param TIME; #sum {j in FLIGHTS} AIRTIME[j]; #total time elapsed = sum of airtimes
param PASSENGERS {i in ORIGIN, j in DESTINATION};

var x {i in ORIGIN, j in DESTINATION, t in TIMESLOTS} binary; #x[i,j,t]=1 if plane travels from i to j at timeslot t
#var landed {j in TIMESLOTS}; #finishing time of flight j

maximize profit: #number of filled seats*flytime*if flight occured
	sum {i in ORIGIN, j in DESTINATION, t in TIMESLOTS} PASSENGERS[i,j]*AIRTIME[i,j]*x[i,j,t];

s.t. maxflights: #cannot take more flights than timeslots
    sum {i in ORIGIN, j in DESTINATION, t in TIMESLOTS} x[i,j,t] <= 3;

s.t. time: #cannot exceed deadline
	sum {i in ORIGIN, j in DESTINATION, t in TIMESLOTS} x[i,j,t]*AIRTIME[i,j] <= TIME;

s.t. origin {j in DESTINATION, t in TIMESLOTS1}: #next flight must leave from previous destination #needs fixing 
	sum {i in ORIGIN} x[i,j,t] - sum {k in DESTINATION} x[j,k,t+1] = 0;

s.t. oneflight {t in TIMESLOTS}:
	sum {i in ORIGIN, j in DESTINATION} x[i,j,t] <= 1;

s.t. norepeats {i in ORIGIN, j in DESTINATION}:
	sum {t in TIMESLOTS} x[i,j,t] <= 1;